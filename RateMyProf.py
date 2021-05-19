import time, sys, argparse
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.chrome.options import Options
from os import path
from selenium.webdriver.common.by import By


# To block the ads in the website, I install adblocker every time I run the code.
# I will find a better, efficient way to handle this
path_to_extension = r'C:\Users\YOUR_USER_NAME\Desktop\1.9.0_0'
chop = webdriver.ChromeOptions()
chop.add_extension(path.abspath('C:\\Users\\Cagri\\Desktop\\Python\\gighmmpiobklfepjocnamgkkbiglidom-4.33.0-Crx4Chrome.com.crx'))
driver = webdriver.Chrome(options = chop)

#driver = webdriver.Chrome('./chromedriver')

# Go to the all York Professors page, wait 1 second and close the pop-up
driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1495")
sleep(1)
driver.find_element_by_xpath("//*[contains(text(), 'Close')]").click()

# Profs with ratings over 4 has this class name
NumRatingOver4 = 'div[@class="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 kMhQxZ"]'

# Click Show More as many times as stated below
#while driver.find_element_by_xpath("//button[contains(text(), 'Show More')]"):
for i in range(10):
    driver.find_element_by_xpath("//button[contains(text(), 'Show More')]").click()
    sleep(0.4)

# Get all ratings over 4
Ratings = driver.find_elements_by_xpath('//%s'%NumRatingOver4)
#Ratings = driver.find_elements_by_xpath('//div[@class="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 kMhQxZ"]/div[@class="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK"]')

# I am printing the found elements for now. They will be used differently in the future
for x in range (len(Ratings)):
    rating = Ratings[x]
    numOfRatings = rating.find_element_by_xpath("./following-sibling::div")

    parent = rating.find_element_by_xpath('./../..') # wrapper of Rating
    allInfo = parent.find_element_by_xpath("./following-sibling::div")
    name = allInfo.find_element_by_xpath("./div[contains(@class, 'CardName__StyledCardName')]")
    department = name.find_element_by_xpath("./following-sibling::div/div[contains(@class, 'CardSchool__Department')]")
    university = name.find_element_by_xpath("./following-sibling::div/div[contains(@class, 'CardSchool__School')]")

    # Other information to be obtained
    #takeAgain = allInfo.find_element_by_xpath("./div[contains(@class, 'CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf')]").text
    #difficulty = allInfo.find_element_by_xpath("./div[contains(@class, 'CardSchool__Department')]").text
    
    # Print the obtained info in a format
    print("Professor:\t\t"+name.text)
    print("Rating:\t\t\t"+Ratings[x].text)
    print("Number of Ratings is:\t"+numOfRatings.text)
    print("School:\t\t\t" + university.text)
    print("Department:\t\t"+ department.text)
    print()
