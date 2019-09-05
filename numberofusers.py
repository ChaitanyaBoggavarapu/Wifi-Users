 numberofusers = 0
    driver = webdriver.Chrome()
    #driver.get("http://www.python.org")
    driver.get("http://admin:Chennaisuperkings7@routerlogin.net/")
    
    #a = driver.find_element_by_id("AttachedDevices-condition")
    
    driver.switch_to.frame("page")
    
    b = driver.page_source
    
    result = b.find('<span id="AttachedDevices-condition" class="Condition-normal">')
    print(b[result+62])
    if (b[result+63]!='<'):
        result1 = b[result+63]
        numberofusers = str(result)+str(result1)
    else:
        numberofusers = str(result)
    #print(b[result+63])
    #print(b[result+64])
    print(numberofusers)
    driver.implicitly_wait(15)
    
    driver.quit()
