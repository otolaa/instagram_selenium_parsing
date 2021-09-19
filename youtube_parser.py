# selenium parser youtube
import sys, os, time, requests, json
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# the decorator for time
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Lead time: {} seconds.'.format(round(end-start, 1)))
    return wrapper

def write_json(data, path):        
    with open(path, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(path):
    try:  
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        # print(sys.exc_info()[1])
        return False

def get_dir(path_folder_name):
    try:
        os.mkdir(path_folder_name)
        return path_folder_name
    except Exception as e:
        print(sys.exc_info()[1])
        return False

def get_slug(src):    
    return str(src.split('?v=')[1])

def get_url_name(url):
    get_url = url.split('?')     
    arr_url = list(filter(None, get_url[0].split('/')))
    return str(arr_url[len(arr_url)-2] + ".webp")

def get_files_url(url, pth = None):
    pth = 'img' if pth is None else pth    
    files_img_path = str(pth + '/' + get_url_name(url))
    # if files is it then return
    if os.path.isfile(files_img_path):
        return files_img_path
    # else add files in path
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(files_img_path,'wb') as f:
                f.write(response.content)
        return files_img_path
    except Exception as e:
        print(sys.exc_info()[1])
        return False

# add list in the alt_url.json
def set_add_json(data, dir_path_filename):
    primary_data = load_json(dir_path_filename)
    if primary_data is not False:
        arr_file_name = [x['slug'] for x in primary_data if x['slug'] is not None]
        for f in data:            
            if f['slug'] in arr_file_name:
                continue
            primary_data.append(f)
        if os.path.isfile(dir_path_filename):
            os.remove(dir_path_filename)
    else:
        primary_data = data
    write_json(primary_data, dir_path_filename)

# returm array photos in pages
def get_list_video(driver, *args):
    primary = driver.find_element_by_id('primary')  
    elem = primary.find_element_by_id('contents')
    items_ = elem.find_element_by_id('items')    
    video = items_.find_elements_by_tag_name("ytd-grid-video-renderer")   
    
    list_video = []
    for i, tag in enumerate(video):
        img_ = tag.find_element_by_tag_name('img')
        img_src = img_.get_attribute('src')
        h3 = tag.find_element_by_tag_name('h3')
        href = h3.find_element_by_tag_name('a')
        src_ = href.get_attribute('href')
        span_ = list(filter(None, [s.text.strip() for s in tag.find_elements_by_tag_name('span') if s is not None]))        
        # ---- add list
        list_video.append({"slug":get_slug(src_), 'title':href.text.strip(), 'href':src_, 'img':img_src, 'text':span_})
        # ---- add photo files ----
        if img_src is not None:
            get_files_url(img_src, dir_path_img)
    return list_video

# the main function parsin for instagram
@benchmark
def main(http_url_page, dir_path, dir_path_img, *args):
    """A method for scrolling the page."""

    # Specify the full path to geckodriver.exe for Windows
    options = Options()
    options.headless = False 
    driver = Firefox(options=options, executable_path=r'.\geckodriver.exe')    
    driver.get(http_url_page)
    
    # stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
    # Get scroll height
    last_height = driver.execute_script("return document.getElementById('content').scrollHeight")

    while True:        
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.getElementById('content').scrollHeight);")
        time.sleep(1)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.getElementById('content').scrollHeight")
        if new_height == last_height:
            print("is break")    
            break
        last_height = new_height

    # add json
    data_video = get_list_video(driver, dir_path_img)
    set_add_json(data_video, str(dir_path + '/video.json'))
    
    # print log
    print(driver.title)    
    print('{} video'.format(len(data_video)))
    print('{} height document windows'.format(last_height))

    driver.close()    
    driver.quit()

if __name__ == '__main__':
    user_ = "zaemiel"
    url_ = str("https://www.youtube.com/user/"+user_+"/videos")
    dir_main = "youtube"
    dir_path = str(dir_main + "/" + user_)
    dir_path_img = str(dir_path +'/images')
    get_dir(dir_main)
    get_dir(dir_path)
    get_dir(dir_path_img)
    main(url_, dir_path, dir_path_img)