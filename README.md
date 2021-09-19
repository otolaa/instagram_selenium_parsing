# Selenium parser instagram && youtube
selenium parsing for instagram && youtube in Windows or Linux (geckodriver.exe is driver Firefox)

## Installing Selenium-WebDriver for Python
```python
# 1 - update
pip3 install --upgrade pip
# 2 - terminal Windows, Linux or Mac
pip3 install selenium
# 3 - Installing the geckodriver driver for Firefox Selenium
# Download geckodriver for Linux, Windows and Mac https://github.com/mozilla/geckodriver/releases/
# Installing geckodriver on Ubuntu, Debian and ArchLinux 
wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
tar -xvzf geckodriver*
sudo chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
```

## Program start /instagram_parser.py
return photos for instagram.com/nasa/

```python
/instagram_parser.py  # main scroll for scrapp
/parsing  # all folders accounts 
/parsing/nasa/images # the folder photo
/parsing/nasa/alt_url.json  # it's json photo list
```

![69 photos](https://github.com/otolaa/instagram_selenium_parsing/blob/master/img/return.jpg "69 photos")

## 🛸👽 parsing example instagram.com/nasa/
Photo by NASA on September 10, 2021.

![Photo by NASA on September 10, 2021.](https://github.com/otolaa/instagram_selenium_parsing/blob/master/parsing/nasa/images/241698339_280602086901951_2643544708970367929_n.jpg "Photo by NASA on September 10, 2021.")

Photo shared by NASA on July 31, 2021 tagging @nasasolarsystem. May be an image of planet.

![Photo shared by NASA on July 31, 2021 tagging @nasasolarsystem. May be an image of planet.](https://github.com/otolaa/instagram_selenium_parsing/blob/master/parsing/nasa/images/226906578_193270329486578_4570034023208063196_n.jpg "Photo shared by NASA on July 31, 2021 tagging @nasasolarsystem. May be an image of planet.")

## 🚗 parsing example instagram.com/teslamotors/
/parsing/teslamotors/images # the folder photo

![teslamotors photos](https://github.com/otolaa/instagram_selenium_parsing/blob/master/img/return_teslamotors.jpg "teslamotors photos")

Photo by Tesla on April 15, 2021. May be an image of outdoors.

![Photo by Tesla on April 15, 2021. May be an image of outdoors.](https://github.com/otolaa/instagram_selenium_parsing/blob/master/parsing/teslamotors/images/173615457_1172281306533433_4705995220569385300_n.jpg "Photo by Tesla on April 15, 2021. May be an image of outdoors.")

📷: @evoluciontesla

![evoluciontesla](https://github.com/otolaa/instagram_selenium_parsing/blob/master/parsing/teslamotors/images/50116130_936227483238953_6459376269299057380_n.jpg "evoluciontesla")


## Program start /youtube_parser.py
selenium parsing for youtube