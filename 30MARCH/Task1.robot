#Task1
#Navigate to website
#scroll popup window
#click on it
#switch to the window and return me the title
#switch back to the parent window and assert the heading of the page

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Windows Practice
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    id = PopUp
    Sleep    2s
    Click Element    id=PopUp
    Sleep    2s
    @{windows}  Get Window Handles
    @{titles}   Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW
    Sleep    3s
    ${title}  Get Title
    Log To Console    ${title}


    Switch Window  ${windows}[0]
    Sleep    2s

    Page Should Contain   Automation Testing Practice
    Sleep    2s

    Close Browser
