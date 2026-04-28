*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}  https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=   Load Json From File    ${CURDIR}/../data/add_pet.json
    
    
    ${response}=    POST On Session    petapi    /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Update pet details
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=   Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=    PUT On Session    petapi    /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

GET pet by ID
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=    GET On Session    petapi    /pet/79

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Find pet by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=    Create Dictionary
    ...    status=available

    ${response}=    GET On Session    petapi    /pet/findByStatus  params=${qp}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Upload an image
    Create Session    petapi    ${BASE_URL}  verify=True
    
    ${form_data}=    Create Dictionary
        ...    additionalMetadata=Jerry's image
    ${file_path}=  Set Variable    ${CURDIR}/../data/img.png
    ${file}=  Evaluate    {'file': open($file_path, 'rb')}

    ${response}=    POST On Session    petapi    /pet/79/uploadImage  
        ...   data=${form_data}
        ...   files=${file}

    Should Be Equal As Integers    ${response.status_code}    200

Post using form data
    Create Session    petapi    ${BASE_URL}  verify=True

    ${form_data}=    Create Dictionary
        ...    name=Jerry
        ...    status=available

    ${response}=    POST On Session    petapi    /pet/79
        ...   data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200

Delete pet by ID
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=    DELETE On Session    petapi    /pet/79

    Should Be Equal As Integers    ${response.status_code}    200
