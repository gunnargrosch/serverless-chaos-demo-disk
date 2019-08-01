# Serverless Chaos Engineering Demo - Disk space failure

This example demonstrates how to use Adrian Hornsby's Failure Injection Layer (https://github.com/adhorn/FailureInjectionLayer) to perform chaos engineering experiments on a serverless environment with disk space failure injection.

## Description

 The demo application consists of a simple serverless app containing one functions behind an API Gateway. The function stores a text file in /tmp, reads the same text file back and lists the contents of /tmp. By using the failure injection layer you are able to inject disk space failure to the function and see what happens.

## Video showing demo

* https://www.youtube.com/watch?v=U8o6-jxkPns

## How to install

This is prepared to be installed using the Serverless Framework (https://serverless.com). Make sure to have the Failure Injection Layer installed in your account (https://github.com/adhorn/FailureInjectionLayer).

1. Clone the repository.
2. Install Serverless Framework (if you don't already have it installed).
```bash
npm install -g serverless
```
3. Create an env.yml file in the root folder based on the env.yml.template contents.
```bash
account: <your account number>
layer: <arn of the lambda layer>
failure_conf: '{"isEnabled": false, "delay": 400, "error_code": 404, "exception_msg": "I failed", "file_size": 100, "rate": 1}'
```
4. Deploy the serverless application using Serverless Framework.
```bash
sls deploy --region YOUR_PREFERRED_REGION --stage YOUR_PREFERRED_STAGE
```
5. Try it out!

## Changelog

### 2019-08-01 v0.1

* Initial release

## Authors

**Gunnar Grosch** - [GitHub](https://github.com/gunnargrosch) | [Twitter](https://twitter.com/gunnargrosch) | [LinkedIn](https://www.linkedin.com/in/gunnargrosch/)
