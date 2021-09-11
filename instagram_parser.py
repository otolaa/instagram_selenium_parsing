# selenium parser instagram
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

def get_url_name(url):
    get_url = url.split('?')     
    arr_url = list(filter(None, get_url[0].split('/')))
    return arr_url[len(arr_url)-1]

def get_files_url(url, pth = None):
    pth = 'img' if pth is None else pth    
    files_img_path = str(pth + '/' + get_url_name(url))
    # if files is it then return
    if os.path.isfile(files_img_path):
        return files_img_path
    # else add files in path
    response = requests.get(url)
    if response.status_code == 200:
        with open(files_img_path,'wb') as f:
            f.write(response.content)
    return files_img_path

def get_dialog(browser, *args):
    try:
        button = browser.find_element_by_css_selector('._1XyCr')
        if button is not None:
            return True
    except Exception as e:
        # print(sys.exc_info()[1])
        return False

def get_buttom(browser, *args):
    try:
        button = browser.find_element_by_css_selector('.tCibT.qq7_A.z4xUb.w5S7h')
        if button is not None:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            button.click()
            time.sleep(2)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            return True
    except Exception as e:
        print(sys.exc_info()[1])
        return False

# add list in the alt_url.json
def set_add_json(data, dir_path_filename):
    primary_data = load_json(dir_path_filename)
    if primary_data is not False:
        arr_file_name = [x[2] for x in primary_data if x[2] is not None]        
        for f in data:            
            if f[2] in arr_file_name:
                continue
            primary_data.append(f)        
        if os.path.isfile(dir_path_filename):
            os.remove(dir_path_filename)
    else:
        primary_data = data
    write_json(primary_data, dir_path_filename)

# returm array photos in pages
def get_list_photo(browser, *args):
    elem = browser.find_element_by_tag_name("main")    
    article = elem.find_element_by_tag_name("article")
    imgs = article.find_elements_by_tag_name('img')
    
    list_photo = []
    for i, tag in enumerate(imgs):
        src_ = tag.get_attribute('src')
        list_photo.append([i, tag.get_attribute('alt'), get_url_name(src_), src_])
        # ---- add photo files ----
        get_files_url(src_, dir_path_img)
    return list_photo

# the main function parsin for instagram
@benchmark
def main(http_url_page, dir_path, dir_path_img, *args):

    # Specify the full path to geckodriver.exe for Windows
    options = Options()
    options.headless = False 
    driver = Firefox(options=options, executable_path=r'D:\OSPanel\domains\python\instagram_selenium_parsing\geckodriver.exe')    
    driver.get(http_url_page)

    # click button more
    # stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
    # selenium-python.readthedocs.io/waits.html
    # _4emnV  -- the class select in ajax indicator
     
    if get_buttom(driver) is True:         
        for i in range(10):            
            if get_dialog(driver) is True:
                # print(i)
                break
            else:
                # print(i)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            # add photo json
            set_add_json(get_list_photo(driver, dir_path_img), str(dir_path + '/alt_url.json'))   
 
    print(driver.title)  
    print('{} photos'.format(len(load_json(str(dir_path + '/alt_url.json')))))

    driver.close()
    # driver.quit()

if __name__ == '__main__':
    dir_main = "parsing"
    url_ = "https://www.instagram.com/nasa/?hl=ru"
    dir_path = str(dir_main + "/" + get_url_name(url_))
    dir_path_img = str(dir_path +'/images')
    get_dir(dir_main)
    get_dir(dir_path)
    get_dir(dir_path_img)
    main(url_, dir_path, dir_path_img)
