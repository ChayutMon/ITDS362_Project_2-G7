*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test Incorrect Username & Password input
    Open Browser    http://45.136.236.146:8081    chrome
    Sleep    2s
    Click Button    css:.item-logIn .Button--link   # คลิกปุ่ม Login
    Sleep    2s
    Input Text      name:identification    kitipoom   # Incorrect username  input
    Input Text      name:password          0972987595   # password input
    Click Button    css:.Button--primary.Button--block  # Adjusted to target the login submit button
    Sleep    2s
    Close Browser

Test Incorrect Email & Password input
    Open Browser    http://45.136.236.146:8081    chrome
    Sleep    2s
    Click Button    css:.item-logIn .Button--link   # คลิกปุ่ม Login
    Sleep    2s
    Input Text      name:identification    Kitipoom@gmail.com   # Incorrect email  input
    Input Text      name:password          0972987595   # password input
    Click Button    css:.Button--primary.Button--block  # Adjusted to target the login submit button
    Sleep    2s
    Close Browser

Test Correct Username & Incorrect Password input
    Open Browser    http://45.136.236.146:8081    chrome
    Sleep    2s
    Click Button    css:.item-logIn .Button--link   # คลิกปุ่ม Login
    Sleep    2s
    Input Text      name:identification    u6587003   # correct username  input
    Input Text      name:password          kitipoom   # Incorrct password input
    Click Button    css:.Button--primary.Button--block  # Adjusted to target the login submit button
    Sleep    2s
    Close Browser

Test Correct Email & Incorrect Password input
    Open Browser    http://45.136.236.146:8081    chrome
    Sleep    2s
    Click Button    css:.item-logIn .Button--link   # คลิกปุ่ม Login
    Sleep    2s
    Input Text      name:identification    ninepulin.mon@student.mahidol.edu   # correct email  input
    Input Text      name:password          kitipoom   # Incorrct password input
    Click Button    css:.Button--primary.Button--block  # Adjusted to target the login submit button
    Sleep    2s
    Close Browser

Test Incorrect Email & Incorrect Password input
    Open Browser    http://45.136.236.146:8081    chrome
    Sleep    2s
    Click Button    css:.item-logIn .Button--link   # คลิกปุ่ม Login
    Sleep    2s
    Input Text      name:identification    Kitipoom@gmail.com   # Incorrct email  input
    Input Text      name:password          kitipoom   # Incorrct password input
    Click Button    css:.Button--primary.Button--block  # Adjusted to target the login submit button
    Sleep    2s
    Close Browser