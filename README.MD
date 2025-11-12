# ***Follower Controller***

---
<br>

## ![a.png](images/a.png) **Table of Contents**
- ### [Decription](#bpng-description) 
- ### [Key Features](#cpng-key-features) 
- ### [Setup](#fpng-setup) 
- ### [Usage](#epng-usage) 
- ### [Third Party License](#fpng-third-party-licenses) 

---
<br>

## ![b.png](images/b.png) **Description**
- The purpose of this project is to be a bot that controls followers and following users. If you often check your followers and following list, this bot does it automatically for you.

---
<br>

## ![c.png](images/c.png) **Key Features**
- The project has two main functions:
    <br>
    - First, it has a follower notification system. In this system, people who recently followed you are sent to you in an email with their names and details.
    <br>

    - Second, it filters the users you follow who do not follow you back. After filtering, it can automatically unfollow unwanted users. 

---
<br>

## ![f.png](images/d.png) **Setup**
- ### ![x.png](images/x.png) *Installing the Modules*
    - The application uses 4 modules that are not built-in. If one or more of them are missing from your computer, you can install them with the following pip commands:
    ```
    pip install pyinstaller
    pip install pandas
    pip install selenium
    pip install yagmail
    ```
    
    >***Note***: To run these commands, PIP (Python Package Installer) must be installed on your system.

<br>

- ### ![x.png](images/x.png) *Downloading Source Files*
    - The application needs 3 main components to work:
        - <ins>Source Codes</ins>: All source files are inside the src folder.
        > src/
        
        <br>
        
        - <ins>Driver</ins>: To connect the app with Chrome, you need a driver. You can download it from the internet or use the one included in the folder below:
        > driver/

        <br>
        
        - <ins>Required Data</ins>:  You must download the folder that contains the necessary data. This folder includes the follower/following list and the JSON files required for the app to run
        >Datas/
    
    - You can download all of them directly to your computer by cloning the repository


    ```
    git clone https://github.com/AlgorithmXplorer/Follower_Controller 
    ```
    

---
<br>

## ![e.png](images/e.png) **Usage**

- ### ![y.png](images/y.png) *Normal Usage*
    - For normal use, the driver, data, and source files should be arranged as follows:
    ```
    app/
    |── main.py
    |── bot.py
    |── file_funcs.py
    |── mail_funcs.py
    |── timer.py
    |
    |──  datas/
    |   |── users.json
    |   └── datas.json
    |
    └── chromedriver.exe
    ```
    - Once you have everything organized as above, just run the <ins>main.py</ins> file to start the application 

<br>

- ### ![y.png](images/y.png)*Usage with Exe File*
    - If you want to use it as an exe file, you only need to convert the source files into an exe file with <ins>pyinstaller</ins>. Run the following command in the <ins>**Git Bash**</ins> terminal.<br><br>

    ```
    pyinstaller --onefile --hidden-import="selenium;email;pandas;yagmail;imaplib;" main.py
    ```
    >Note: The Git Bash terminal must be opened in the same location as your source files. 
    <br>

    - After completing this process, there should be a folder named **dist**. Take your ***main.exe*** file from there and follow the same steps as in [Normal Usage](#normal-usage), but use your exe file instead of the source files.

---
<br>

## ![f.png](images/f.png) **Third Party Licenses**

-   ### ![g.png](images/g.png) Yagmail
    - **License**: <ins>MIT License</ins> → This license is very permissive; you can use, modify, and distribute the code without restriction, as long as you keep the license and copyright notice.
    - **Link**: https://pypi.org/project/yagmail
<br>

-   ### ![g.png](images/g.png) Selenium
    - **License**: <ins>Apache License 2.0</ins> → Under this license, you can freely use the software for commercial or open-source projects; the only requirement is to keep the copyright and license notices.
    - **Link**: https://pypi.org/project/selenium
<br>

-   ### ![g.png](images/g.png) Pandas
    - **License**: <ins>BSD 3-Clause License</ins> → This license allows you to use and distribute the software widely, as long as you retain the source code notices.
    - **Link**: https://pypi.org/project/pandas
<br>

-   ### ![g.png](images/g.png) Pyinstaller
    - **License**: <ins>GNU General Public License v2 (GPLv2) […with an exception that allows you to build commercial applications with it]</ins> → With this license, you can distribute executable packages built with PyInstaller under your own license; but if you distribute changes made to PyInstaller’s source code, they must comply with GPL v2 terms.
    - **Link**: https://pypi.org/project/pyinstaller




