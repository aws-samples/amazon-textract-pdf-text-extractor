# Amazon Textract PDF Text Extractor

Continuously improving AWS translate results using AI to augment parallel data
with humans in the loop. The end goal is to provide customized and accurate
domain specific translation results.

# Solution Architecture

![Solution Architecture](images/solution_architecture.png)

## Prerequisites

You can either use AWS Cloud9 or your local to deploy this solution.

## Prerequisites for local setup
1. Download and install the latest version of Python for your OS from [here](https://www.python.org/downloads/). We will be using Python 3.8+.

2. You will need to install version 2 of the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) as well. If you already have AWS CLI, please upgrade to a minimum version of 2.0.5 follwing the instructions on the link above.

3. AWS CDK

4. Docker

## Deployment Instructions

1. Clone this repo to your local or Cloud9.

2. Run the following commands:
   pip install -r requirements.txt

   cdk bootstrap

   cdk deploy SimpleAsyncWorkflow



## Execution Instructions

   Follow the instructions in blog post.


## Further Reading:

## License

   This library is licensed under the [MIT-0 License](https://github.com/aws/mit-0).
