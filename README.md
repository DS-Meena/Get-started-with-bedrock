# Amazon Bedrock 🪨

Amazon Bedrock is a fully managed service that provides access to a range of high-performing foundation models (FMs) from leading AI companies and Amazon itself. It's designed to simplify the process of building and scaling generative AI applications.

Key features of Amazon Bedrock includes: 🔑

1. **Unified API:** It offers access to various foundation models thorugh a single API, making it easier for developers to experiment with and integrate different models.
2. Model selection
3. **Customization Options:** Amazon Bedrock allows users to customize models privately with their own data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG).
4. Security and Privacy
5. Serverless Experience
6. **Compreshensive Capabilities:** It offers tools for experimenting with prompts, augmenting responses with data sources, creating agents, and implementing safeguards.
7. Integrationi with AWS Services

## Set up AWS account 📐

First you need to set up your IAM role credentials.

1. Install aws cli `pip3 install awscli --upgrade` and confirm using `aws --version`
2. Run `aws configure` command.
3. Enter your access key, secret key and region [optional].

This creates a credentials file at `~/.aws/credential` location.

## Create a virtual enviornment 🗺️

First, we should create a virtual environment to keep your global enviornment clean. 

**In Windows System** 🪟

1. Install virtualenv using pip `pip install virtualenv`
2. Create a virtual environment using `python -m venv my_env`
3. To activate your virtual envionrment use `my_env\Scripts\activate`
4. `my_env\Scripts\deactivate` simply to deactivate

**In Linux System**

The first step is same as windows system
1. Use `virtualenv my_env` to create a virtual environment.
2. To start the your newly created virtual environment use `source my_env/bin/activate`.
3. and to deactivate simply type `deactivate`

