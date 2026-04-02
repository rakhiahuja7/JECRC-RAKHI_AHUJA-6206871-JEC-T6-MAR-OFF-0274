*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${url}  https://the-internet.herokuapp.com/
${url}   https://testautomationpractice.blogspot.com/


*** Test Cases ***
implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s

   ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Input Text    id=name    dskdsldm



    Close Browser
