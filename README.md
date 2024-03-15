# Getting Started with Bedrock Basics

## How to install Pip3

1. First check your python version, it should be greater than 3.0. `python3 --version`
2. Update your linux environment using `sudo apt update` and `sudo apt upgrade`.
3. Install pip via `sudo apt-get install python3-pip`
4. Confirm using `pip3 --version`.

## Add to Path

If you need to add the installation path to PATH, you can do in following way:

Like I want to add following path to PATH: /home/dsm/.local/bin/

`export PATH=$PATH:/home/dsm/.local/bin/`  This is temporary change. For permenant change, you need to add this command to `~/.bashrc`.


## Create a virtual enviornment

First, we should create a virtual environment to keep your global enviornment clean. 

**In Windows System**

1. Install virtualenv using pip `pip install virtualenv`
2. Create a virtual environment using `python3 -m venv my_env`
3. To activate your virtual envionrment use `my_env\Scripts\activate`
4. `my_env\Scripts\deactivate` simply to deactivate

**In Linux System**

The first step and 2nd steps are same as windows system
1. To start the your newly created virtual environment use `source my_env/bin/activate`.
2. and to deactivate simply type `deactivate`

Install everything inside your virtual environment, without any risk of breaking your other installations.
