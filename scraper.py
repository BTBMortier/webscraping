import os 
import sys
import time 
import argparse
import itertools
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException , NoSuchElementException



class scraper:
    
    def __init__(self,mail,password,uastring):
        self.mail = mail
        self.password = password
        self.uastring = uastring
        options = Options()
        options.add_argument("user-agent="+self.uastring)
        #options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        print("Logging in...")
        self.driver.get("https://www.instagram.com")
        cookies_prompt = self.driver.find_elements_by_xpath("//button[@tabindex='0']")
        cookies_prompt[0].click()
        time.sleep(3)
        user_field = WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
        pass_field = self.driver.find_element_by_xpath("//input[@name='password']")
        user_field.send_keys(self.mail)
        pass_field.send_keys(self.password)
        pass_field.send_keys(Keys.ENTER)
        try:
            not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
            not_now2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        except NoSuchElementException:
            print("Bad credentials!")
            os.exit(1)

    def get_followers(self,page):
        print(f"Scraping followers from \"{page}\"...")
        self.driver.get(f"https://www.instagram.com/{page}/")
        try:
            self.driver.find_element_by_xpath(f"//a[@href= '/{page}/followers/']").click()
        except NoSuchElementException:
            print("Account is private or does not exist")
            os.exit(1)

        dialog = WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]")))
        followers = WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.XPATH,f"//a[@href= '/{page}/followers/']//span")))
        followers = self.driver.find_element_by_xpath(f"//a[@href= '/{page}/followers/']//span").get_attribute("title")
        followers = followers.replace(",","")
        followers = int(followers)
        print(f"Found {followers} followers...")
        print("Scraping followers...")
        
        count = 0

        while count < followers :
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            count = len(self.driver.find_elements_by_xpath("//div[@role='dialog']//li"))
            progress = ((count/followers)*100)
            print(f"Progress : {count}/{followers} ({progress:.2f}%)",end="\r")
        
        print("Done scraping followers !")
        print(f"Writing to {page}.txt ...")
        
        with open(f"{page}.txt", "a+") as file:
            for i in range(1,followers+1):
               follower_tag = f"/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a"
               follower = self.driver.find_element_by_xpath(follower_tag).get_attribute("href")
               follower = f"{follower[26: -1]}\n"
               file.write(follower)
        print("All Done!")


def main():
    uas = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    
    worker = scraper("ezri_jklm","Karl-Anthony51",uas)
    target = args.page
    worker.login()
    worker.get_followers(args.page)
    

if __name__ == "__main__":
    parser = parser = argparse.ArgumentParser()
    parser.add_argument(
            "page",
            help="Instagram page to scrape,quotation marks required",
            type=str)
    args = parser.parse_args()
    main()
