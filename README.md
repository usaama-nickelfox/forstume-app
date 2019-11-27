### How to create a nested stack:
The AWS::CloudFormation::Stack type nests a stack as a resource in a top level template.
We can add output values from a nested stack within the root stack.
We use intrinsic function  Fn::GetAtt function with nested stack logical name and the name of the output value in nested stack.
Syntax: VpcId: !GetAtt NestedStackName.Outputs.NestedStackOutputName
> Note: Restrict the stack from deletion, do not make any changes to the stack from console.
> Remommended Approach:Always perform updates from root stack
> We can have maximum 200 stack per account, To move more than 200 stack, then we can use stacksets using the global template.


### Implementation of nested stack.
Nested stack are treated just like any other resource in the cloudformation template. Nested stack resource to be created and managed like any other resource.
Nested stack have a root or base stack, which contains all the shared resource and child stacks refrences those resource. so, as to save resource on each API endpoint.

Typically each ApiEndpoint used to consume 5-8 resouces, And an stack can have at most 200 resources per stack, which mean that a stack can have 24-39 API Endpoints.

*Steps*:
1) Create a template.yaml file in the root folder, and put all the shared resources in this template.
2) Create a resouce of stack type (AWS::CloudFormation::Stack) with the templateUrl and parameters, You can share the parameters like share resources ARN etc. Template URL is a template.yaml file path, put the template.yaml file in each directory which is going to be  a nested stack.
3) Each nested stack ships with own ApiGateway, To map them with a single domain, we need to integrate the custom domain name.
4) Add the base path mapping of the ApiGateway with base path(Eg: patient, provider, report). So, the heavy lifting work in done by AWS gateway service.
5) Deploy the root stack, which will create and update the root and child stack. If there are some that depends on another stack, then use cloudformation intrinsic function GetAtt or DependsOn attribute.


*How to efficently utilize the resources*:
1) Each lambda function should create an instance of the Service class (Report class), Each class should inherit the Base Service class which have methods for get, post, patch, delete and put. these function needs to be overriden depends on the requirement. By default these methods return the NotImplemented Error.
2) This approach uses the object oriented features and reduces the resources by:
Suppose: Add patient, Get list and detail patient, update patient profile, delete patient profile
The current approac will take resource from (5*5) to (5*8) = 25 to 40
But above approach will take (2*5) to (2 to 8) = 10 to 16
3) Use method as any. ApiGateway donot offer the optional parameter, other this can be reuuced to half.

*Note*: We don't have to chnage much in codepipeline, need to include capability CAPABILITY_AUTO_EXPAND.

For reference and examples, please visit this repository: <pending>

*Template Hierarchy*:
> Root Stack Template
```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  Forstume-app

  Nested stack server-less micro-service architecture.

# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Timeout: 3

Resources:
  BlogNestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: blog/template.yaml

  AuthenticationNestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: authentication/template.yaml

```
Description: This template have 2 resources of cloudformation stack type. BlogNestedStack and AuthenticationStack. And common resource will go in root stack.
You can also pass parameters to each stack using *Parameter* attribute.

> Authentication Template: 
```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  Authentication-app

  Authentication app handles user sign-up, login, forgot-password, reset-password, account activation.

# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Timeout: 3

Resources:
  LoginFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: user
      Handler: login.lambda_handler
      Runtime: python3.6
      Events:
        Authentication:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /login
            Method: post

  SingupFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: user
      Handler: singup.lambda_handler
      Runtime: python3.6
      Events:
        Authentication:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /signup
            Method: post

  ForgotPasswordFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: user
      Handler: forgot_password.lambda_handler
      Runtime: python3.6
      Events:
        Authentication:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /forgot-password
            Method: post

Outputs:
  # ServerlessRestApi is an implicit API created out of Events key under Serverless::Function
  # Find out more about other implicit resources you can reference within SAM
  # https://github.com/awslabs/serverless-application-model/blob/master/docs/internals/generated_resources.rst#api
  LoginApi:
    Description: "API Gateway endpoint URL for Prod stage for Login function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/login/"
  LoginFunction:
    Description: "Login Lambda Function ARN"
    Value: !GetAtt LoginFunction.Arn
  LoginFunctionIamRole:
    Description: "Implicit IAM Role created for Login function"
    Value: !GetAtt LoginFunctionRole.Arn
  SignupApi:
    Description: "API Gateway endpoint URL for Prod stage for Signup function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/singup/"
  SignupFunction:
    Description: "Signup Lambda Function ARN"
    Value: !GetAtt SingupFunction.Arn
  SignupFunctionIamRole:
    Description: "Implicit IAM Role created for Signup function"
    Value: !GetAtt SingupFunctionRole.Arn
  ForgotPasswordApi:
    Description: "API Gateway endpoint URL for Prod stage for Forgot password function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/forgot-password/"
  ForgotPasswordFunction:
    Description: "Login Lambda Function ARN"
    Value: !GetAtt ForgotPasswordFunction.Arn
  ForgotPasswordFunctionIamRole:
    Description: "Implicit IAM Role created for forgot password function"
    Value: !GetAtt ForgotPasswordFunctionRole.Arn
```
Description: Authentication app contains 3 rest services for login, signup and forgot-password.

This is how we will have stack for each entity. And each enity will have a base path mapping.
