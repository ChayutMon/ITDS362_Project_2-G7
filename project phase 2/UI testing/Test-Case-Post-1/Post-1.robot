*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${URL}              http://45.136.236.146:8081
${BROWSER}          chrome
${USERNAME}         G7testS
${PASSWORD}         12345678
${HEADER}           Group7TestThis
***Test Cases ***
Test Login with valid Account
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    css:.Button--primary    10
    Click Button    css:.Button--primary
    Wait Until Element Is Visible    css:.Form.Form--centered    10
    Input Text      name:identification    ${USERNAME}
    Input Text      name:password          ${PASSWORD}
    Click Button    css:.Button--primary.Button--block
    Wait Until Element Is Visible    css:.Button--user    10
    Element Text Should Be    css:.username    G7testS
    Close Browser

Test Post discussion with valid Account
    Open Browser    ${URL}    ${BROWSER}
    Click Button    css:.Button--primary
    Wait Until Element Is Visible    css:.Form.Form--centered    10
    Input Text      name:identification    ${USERNAME}
    Input Text      name:password          ${PASSWORD}
    Click Button    css:.Button--primary.Button--block
    Wait Until Element Is Visible    css:.Button--user    10
    Element Text Should Be    css:.username    G7testS


    Click Button    css:.Button--primary.IndexPage-newDiscussion
    Wait Until Element Is Visible    css:.Composer-content    10

    Wait Until Element Is Visible    css:.FormControl    10
    Input Text    xpath://input[@placeholder='Discussion Title']    ${HEADER}
    Input Text    css:.Composer-flexible.TextEditor-editor   This is test fr
    Click Element    css:.item-submit.App-primaryControl

    Wait Until Element Is Visible    css:.TagDiscussionModal-list.SelectTagList
    Click Element    xpath://ul[@class='TagDiscussionModal-list SelectTagList']/li[span[text()='General']]
    Wait Until Element Is Visible    xpath://li[@class='pinned colored selected active']    10
    Wait Until Element Is Not Visible    xpath://button[@class='Button Button--primary hasIcon disabled']
    Click Element    xpath://button[@class='Button Button--primary hasIcon']/span[text()='OK']
    Wait Until Element Contains    css:.DiscussionListItem-title    ${HEADER}
    Click Element    xpath://h3[text()='${HEADER}']


    Close Browser 