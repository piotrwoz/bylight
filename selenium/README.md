# Selenium how to (our script version)

If you're using WSL on Windows machine: Clone ur repo on your windows host and work on windows ;)

## Prerequisites 
0. Set up Powershell
    1. Run Powershell as Administrator
    2. 
    ```bash
    cd ~ # redirect to PS C:\Users\whatsyoface
    Set-ExecutionPolicy -Scope CurrentUser
    # PowerShell will then prompt us to provide an execution policy, type:
    RemoteSigned
    #check if all is correct
    Get-ExecutionPolicy -List
    #        Scope ExecutionPolicy
    #            ----- ---------------
    #    MachinePolicy       Undefined
    #    UserPolicy       Undefined
    #        Process       Undefined
    #    CurrentUser    RemoteSigned
    #    LocalMachine       Undefined
    ```

1. Chocolatey
    ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; `iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    #Answer Yes when prompted. Close and reopen an elevated PowerShell window to start using choco
    ```

2. Python 3 & pip
    ```bash
    choco upgrade chocolatey
    choco install -y python3
    refreshenv # or reopen PowerShell
    python -V # output Python 3.7.0
    python -m pip install --upgrade pip
    ```

3. Setting Up a Virtual Environment
    ```bash
    python -m venv selenvenv
    selenvenv\Scripts\activate # to turn on your virtual env
    pip install selenium
    pip3 freeze > requirements.txt
    selenvenv\Scripts\deactivate # to turn off
    ```
    Alternatively just intall it without virtual env
    
    ```bash
    pip install selenium
    ```

4. Driver (Chrome in our case)
    1. Check which version of Chrome you have (those three dots in right upper corner > Settings > Chrome -information)
    2. Go to [Chrome driver downloads page](https://chromedriver.chromium.org/downloads) and download driver that is suitable for your Chrome version
    3. Unpack it and pass the path to your chrome driver in your script like so
        `webdriver.Chrome("C:\\chromedrivers\\win\\chromedriver.exe")`

## Credits 
[digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)
[jcutrer](https://jcutrer.com/windows/install-chocolatey-choco-windows10)
[codeboxsystems](https://codeboxsystems.com/tutorials/en/how-to-install-python-and-selenium-for-browser-automation/)
