import time
import json
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#========================= json file fr changing username 

f = open('accounts.json',)
datas = json.load(f)

#=========================== json file for tags 

with open("tags.txt",'r') as f:
    tags = [line.strip() for line in f]


def dosent_exist(driver,xpath):
    try:
        driver.find_element(By.XPATH , f"{xpath}")
    except NoSuchAttributeException:
        return True

    else:
        return False

#==============================

def randomcomment():
    with open("comments.txt",'r') as f:
        comments = [line.strip() for line in f]
    comment =  random.choice(comments)
    return comment 


#=========================== insta function start

def main(data):

    PATH = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

    options = webdriver.ChromeOptions()

    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/109.0.5414.120 Mobile Safari/535.19" }
    
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(chrome_options = options , service=PATH)
    driver.set_window_size(500,950)

    driver.get("https://www.instagram.com/")
    #=========================================================

    #login Section--------------------
    time.sleep(5)
    print("\n\n Logging In........\n\n")

    #driver.find_element(By.XPATH, '//*[@id="mount_0_0_BZ"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/div[3]/button[1]/div').click()
    driver.find_element(By.XPATH, "//div[normalize-space()='Log in']").click()
    time.sleep(3)

    username_field = driver.find_element(By.NAME , 'username')
    username_field.send_keys(data["username"])
    time.sleep(1)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(data["password"])
    time.sleep(1)

    #login_btn = driver.find_element(By.XPATH, "//body/div[@id='mount_0_0_I0']/div/div/div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z')]/div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z')]/div[contains(@class,'x78zum5 xdt5ytf x1n2onr6 x1ja2u2z')]/div[contains(@class,'x78zum5 xdt5ytf x1n2onr6')]/div[contains(@class,'x78zum5 xdt5ytf x1n2onr6 xat3117 xxzkxad x4m6w61')]/div[contains(@class,'x78zum5 xdt5ytf x10cihs4 x1t2pt76 x1n2onr6 x1ja2u2z')]/section[contains(@class,'x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x10wlt62 x1wjobn4')]/main[contains(@role,'main')]/article[contains(@class,'x1qjc9v5 x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x78zum5 x1q0g3np x1iyjqo2 x2lah0s xk390pu xl56j7k xg87l8a xkrivgy xat24cr x1gryazu x1ykew4q xexx8yu x4uap5 x1gan7if xkhd6sd x11njtxf xh8yej3 x1d2lwc3 x1n2onr6')]/div[contains(@class,'_ab1y _ab1-')]/div[contains(@class,'_ab21')]/div[contains(@class,'_ab3a')]/form[@id='loginForm']/div[contains(@class,'_abc2 _abcm')]/div[1]")
    login_btn = driver.find_element(By.XPATH, "(//div[contains(@class,'_abak _abb8 _abbq _abb- _abcm')])[2]" )
    login_btn.click()
    time.sleep(6)

    print("\n\n Logged In........\n\n")



    #=======================================================

    # fetching posts======================================



    tag =random.choice(tags)
    print("\n\n Fetching Posts for " +tag + "........\n\n")
    link = "https://www.instagram.com/explore/tags/" +tag

    driver.get(link)

    time.sleep(4)

    #================================== selecting row
    for i in range(1):
        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(2)

    time.sleep(4)
    #row1 = driver.find_element(By.XPATH ,'//*[@id="mount_0_0_KN"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]')
    row1 = driver.find_element(By.XPATH, "(//div[@class='_ac7v _aang'])[4]")
    time.sleep(2)
    #row2 = driver.find_element(By.XPATH ,'//*[@id="mount_0_0_KN"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[2]')
    row2 = driver.find_element(By.XPATH, "(//div[@class='_ac7v _aang'])[5]")
    
    #==================================== getting links

    r_link1 =row1.find_elements(By.TAG_NAME, 'a')
    r_link2 =row1.find_elements(By.TAG_NAME, 'a')
    links = r_link1 +r_link2

    urls=[]

    for i in links:
        if i.get_attribute('href') != None:
            urls.append(i.get_attribute('href'))

    print(urls)


    #=========================================

    #comments================================

    for url in urls:
        print("\n\n Commenting to this post ----> "+ url + "\n\n")
        comment = randomcomment()
        driver.get(url)
        driver.implicitly_wait(1)

        time.sleep(3)

        driver.find_element(By.XPATH, "//span[@class='_aamx']//button[@type='button']").click()
        time.sleep(10)
        if dosent_exist(driver , "//div[@class='_aaof']"):
            print('Skiped - Comment dissabled')
        else:
            find_textarea = (By.XPATH, "//textarea[@placeholder='Add a comment…']")
            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located(find_textarea)
            )
            comment_box = driver.find_element(*find_textarea)
            WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable(find_textarea)
            )
            comment_box.click()
            comment_box.send_keys(comment)

            time.sleep(2)

            find_button = (By.XPATH, "//div[contains(text(),'Post')]")
            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located(find_button)
            )
            button = driver.find_element(*find_button)
            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located(find_button)
            )
            button.click()

            time.sleep(random.randint(1 ,10))




    driver.close()





for data in datas:
    main(data)



###### if want to contuine promgram in infinite loop

""" while True:
    for data in datas:
        main(data) """