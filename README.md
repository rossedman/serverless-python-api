# Servless Python API
This is a simple python API to showcase how to deploy an API through Serverless
using AWS Lambda and API Gateway.

## Install
```sh
# install serverless
npm install serverless -g

# install python libraries
cd api && pip install -t vendored/ -r requirements.txt

# deploy this project
sls project init
sls dash deploy
```

### Homebrew Fix
There are strange problems with Homebrew installed python, check [here](https://github.com/Homebrew/brew/blob/master/share/doc/homebrew/Homebrew-and-Python.md) for way to fix and resolve.

### Resources

- [Serverless & Python](https://serverlesscode.com/post/python-on-serverless-intro/)
- [Serverless Python Basics](http://cloudacademy.com/blog/serverless-framework-aws-lambda-api-gateway-python/)
