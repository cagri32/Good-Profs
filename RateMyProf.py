import time, sys, argparse
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.chrome.options import Options
from os import path
from selenium.webdriver.common.by import By
import json
import time

# Take a start time to calculate the running time
start_time = time.time()

# To block the ads in the website, I install adblocker every time I run the code.
# I will find a better, efficient way to handle this
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
database = {}
i = 0
try:
    # Click Show More as many times as stated below
    while driver.find_element_by_xpath("//button[contains(text(), 'Show More')]"):
    #for i in range(3):
        driver.find_element_by_xpath("//button[contains(text(), 'Show More')]").click()
        sleep(1)
        # To see the progress of the scraping process
        i += 1
        if(i%25 == 0):
            print(database)
# Catch NoSuchElementException error at the end of the loop that looks for "Show More" button
except NoSuchElementException:
    print("done")
    print("Clicked %d times" %i)
    
    # Get all ratings over 4
    Ratings = driver.find_elements_by_xpath('//%s'%NumRatingOver4)

    # Store the found values in a dictionary
    for x in range (len(Ratings)):
        rating = Ratings[x]
        numOfRatings = rating.find_element_by_xpath("./following-sibling::div")

        parent = rating.find_element_by_xpath('./../..') # wrapper of Rating
        allInfo = parent.find_element_by_xpath("./following-sibling::div")
        name = allInfo.find_element_by_xpath("./div[contains(@class, 'CardName__StyledCardName')]")

        schoolcard = name.find_element_by_xpath("./following-sibling::div")
        department = schoolcard.find_element_by_xpath("./div[contains(@class, 'CardSchool__Department')]")
        university = schoolcard.find_element_by_xpath("./div[contains(@class, 'CardSchool__School')]")
        
        # More information obtained
        ratingcard = schoolcard.find_element_by_xpath("./following-sibling::div")
        takeAgain = ratingcard.find_elements_by_xpath("./div/div[contains(@class, 'CardFeedbackNumber')]")[0]
        difficulty = ratingcard.find_elements_by_xpath("./div/div[contains(@class, 'CardFeedbackNumber')]")[1]
        #link = parent.find_element_by_xpath('./..').get_attribute('href')
        
        # Keep this method here to reference it later
        #difficulty = takeAgain.find_element_by_xpath("./../following-sibling::div/following-sibling::div/div[contains(@class, 'CardFeedbackNumber')]")
        
        database[name.text] = {}
        database[name.text]['Name'] = name.text
        database[name.text]['Rating'] = Ratings[x].text
        database[name.text]['NumberofRatings'] = numOfRatings.text
        database[name.text]['School'] = university.text
        database[name.text]['Department'] = department.text
        database[name.text]['Take Again'] = takeAgain.text
        database[name.text]['Difficulty'] = difficulty.text
        #database[name.text]['Link'] = link

    # Dump the dictionary to a json file
    with open('result.json', 'w') as fp:
        json.dump(database, fp)
    
    sleep(5)
    driver.quit()
    # Calculate elapsed time
    print("--- %s seconds ---" % (time.time() - start_time))
