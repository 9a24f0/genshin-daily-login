# Genshin Daily Login Tool
This tool helps you to automatically claim daily reward at [HoyoLab](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=vi-vn) when you boot into Windows.

## Dependencies
This tool requires Python and some Python packages in order to functions

### Install Python
Go to [Python's official page](https://www.python.org/downloads/windows/) and download
Python 3 installer. Please kindly check whether your system is 64-bit or 32-bit to download correct version.

> How to determine if you have a 32-bit or 64-bit CPU?
1. Open a File Explorer by pressing `Windows` + `E`.
2. Right click on `This PC`.
3. Select `Properties`.
4. In the *System Properties* window, under `System` section, find `System type`.

### Install Python package manager
Pip is already installed when you install Python >=3.4 as stated in PyPa Pip's documentation:
> pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or venv. Just make sure to upgrade pip.
To check whether you have pip, open Windows PowerShell and run:
```
py -m pip --version
```
If the result is `pip X.Y.Z from ...\site-packages\pip (python X.Y)`, please proceed to the next section.
If pip is not found, then run these commands:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py get-pip.py
```

### Install dependencies
After cloned or downloaded this repo, open the repo's folder in File Explorer and copy the path,
then in your PowerShell, run these commands:
```
cd YOUR_COPIED_PATH
pip install -r requirements.txt
```

## Setup your batch file
Right click on `startup.bat`, select `Open with...` and select Notepad. You will get the content of the file as:
```
"Path where your Python exe is stored\python.exe" "YOUR_COPIED_PATH\main.py"
pause
```
First thing to do is to replace `YOUR_COPIED_PATH` with the path to the repo's folder which you are just copied from the step above.

Secondly, back to PowerShell and run:
```
where python
```
The result should look like this:
```
C:\Users\(Your logged in User)\AppData\Local\Programs\Python\Python(version)\python.exe
```
Then replace `Path where your Python exe is stored\python.exe` in your batch file with the result


## Make your batch file automatically run on start up
Copy your batch file into `C:\Users\(Your logged in User)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. It will automatically run the script next time you boot into Windows.
