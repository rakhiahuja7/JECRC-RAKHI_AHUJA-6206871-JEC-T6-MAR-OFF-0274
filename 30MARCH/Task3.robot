#Task 3
#
#Navigate to amazon
#Click on electronic in tab
#Check on 'boat' checkbox
#click on any product before clicking store the name of product
#switch to new window
#assert the product name is present in the new window
#print the actual price, discounted price and the percentage
#scroll to add to cart and click on the button
#click on cart icon on top right corner
#check if same product has been added

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    5s

    Click Element    xpath=//a[@data-csa-c-content-id="nav_cs_electronics"]
    Sleep    2s

    Scroll Element Into View    xpath=(//span[text()="boAt"])[2]
    Sleep    2s

    Click Element   xpath=(//span[text()="boAt"])[2]
    Sleep    2s

    Scroll Element Into View    xpath=//img[@src="https://m.media-amazon.com/images/I/71UdDIKDlEL._AC_UL320_.jpg"]
    ${product_name}  Get Text  xpath=(//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]/descendant::span)[6]

    Click Element    xpath=(//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"])[6]
    Sleep    3s

    Switch Window  NEW
    Sleep    2s

    Page Should Contain    Boat Wave Call 3 Smartwatch 1.83
    Sleep    2s

    ${prices}  Get Text    xpath=//div[@id="corePriceDisplay_desktop_feature_div"]
    Log To Console    ${prices}
    Sleep    2s

    Scroll Element Into View    xpath=(//span[text()="Add to cart"])[3]
    Sleep    3s
    Click Button    xpath=(//span[text()="Add to cart"])[3]/preceding-sibling::input
    Sleep    3s

    Click Element    id=nav-cart-count
    Sleep    2s

    Page Should Contain     ${product_name}
    Sleep    2s

    Close Browser