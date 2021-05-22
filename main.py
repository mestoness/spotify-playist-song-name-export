from selenium import webdriver
from random import randint
import time
options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
print("https://github.com/mestoness/spotify-playist-song-name-export")
print()
print()

print("Playist ID nizi giriniz")
url = input()

if url != "":
            browser = webdriver.Chrome(options=options,executable_path="chromedriver.exe")

            browser.get(f"https://open.spotify.com/embed/playlist/{url}")
            time.sleep(4)
            adet = len(browser.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/div/table/tbody/tr'))

            for render in range(adet):
                    try:
                        browser.switch_to.window(browser.window_handles[0])
                        linksss = f'//*[@id="main"]/div/div/div[2]/div/table/tbody/tr[{render}]/td[2]/div/div[1]/span'
                        print(browser.find_element_by_xpath(linksss).text)
                        link22 = f'//*[@id="main"]/div/div/div[2]/div/table/tbody/tr[{render}]/td[2]/div/div[2]/span'
                        print(browser.find_element_by_xpath(link22).text)
                        print("-----------------------")
                    except:
                        time.sleep(1)
            browser.quit()            
