# Getting Started with Bedrock Basics

## Create a virtual enviornment

First, we should create a virtual environment to keep your global enviornment clean. 

**In Windows System**

1. Install virtualenv using pip `pip install virtualenv`
2. Create a virtual environment using `python -m venv my_env`
3. To activate your virtual envionrment use `my_env\Scripts\activate`
4. `my_env\Scripts\deactivate` simply to deactivate

**In Linux System**

The first step is same as windows system
1. Use `virtualenv my_env` to create a virtual environment.
2. To start the your newly created virtual environment use `source my_env/bin/activate`.
3. and to deactivate simply type `deactivate`


# Troubleshooting

**Issue with pydantic**
error: 
pydantic.errors.PydanticUserError: If you use `@root_validator` with pre=False (the default) you MUST specify `skip_on_failure=True`. Note that `@root_validator` is deprecated and should be replaced with `@model_validator`.

*ImportError: cannot import name 'hub' from 'langchain'*
To resolve this error use latest version of langchain and pydantic.
`pip install --upgrade langchain pydantic`

