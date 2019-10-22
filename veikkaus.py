from selenium import webdriver
driver = webdriver.Chrome('c://pythonprojects//veikkaus//chromedriver')
driver.maximize_window()
driver.get("https://www.veikkaus.fi/fi/tulokset#!/tulokset/lotto")
driver.implicitly_wait(5)
f = open("lotto7jackpot.txt","w")
row_number= 1
end_date = "4.12.2016"
drange = driver.find_element_by_css_selector(".date-range").text
while drange[-9:] != end_date:
    numbers = []
    for number_index in range(1,8):
        numbers.append(driver.find_element_by_css_selector(".lotto-correct-primary-numbers > li:nth-child("+str(number_index)+")").text)
    date1 = driver.find_element_by_css_selector(".selected-week")
    jackpot = driver.find_element_by_css_selector(".table:nth-child(2) .prize-tier:nth-child(1) > .prize-tier-share-count").text
    f.write( str(row_number ) + ",")
    for number_index in range(0,7):
        f.write(numbers[number_index] + "," )
    jackpot = jackpot[0:1]
    try:
        val = int(jackpot)
        f.write(jackpot)
    except ValueError:
        f.write("0")
    f.write("\n")
    driver.find_element_by_css_selector(".i-chevron-left").click()
    drange = driver.find_element_by_css_selector(".date-range").text
    row_number +=1
    driver.implicitly_wait(1)
f.close

with open ("lotto7jackpot.txt") as fi, open("lotto7jackorder.txt", 'w') as fo:
    line1 = reversed(fi.readlines())
    print (line1)
    fo.writelines(line1) 
fi.close()
fo.close()
driver.close()
