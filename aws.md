# Collection of How To walkthroughs of various Amazon Services
# How to Host a Static Website with Amazon S3
https://medium.com/@austinlasseter/how-to-host-a-static-website-on-an-amazon-s3-bucket-be25a613586a
https://lambdaschool.zoom.us/rec/share/y5FeaJH9rUpJeJXWyWblaIAlP4i-eaa81iUY__NYmknfxBknGMVEcHTiGEAiMFOT

*Bucket Policy for Tutorial*
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid":"PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": ["arn:aws:s3:::<YOURWEBSITEBUCKETHERE>/*"]
        }
    ]
}

# Deploying a Dash App with Elastic Beanstalk
https://medium.com/@austinlasseter/deploying-a-dash-app-with-elastic-beanstalk-console-27a834ebe91d
https://lambdaschool.zoom.us/rec/share/xvBuJvbcznhOXqvdyU76WYUPG6PdT6a80SkZ-PNZxR1rS0DmWSCeH-Ei4Q7dYhIb

# AWS SageMaker Introduction
https://aws.amazon.com/getting-started/tutorials/build-train-deploy-machine-learning-model-sagemaker/
https://github.com/austinlasseter/sagemaker_tutorials/blob/master/xgboost-tutorial.ipynb
https://aws.amazon.com/blogs/machine-learning/deploying-machine-learning-models-as-serverless-apis/

# AWS Lambda and CloudFront
https://medium.com/@austinlasseter/build-a-password-protected-website-using-aws-lambda-and-cloudfront-3743cc4d09b6
https://lambdaschool.zoom.us/rec/share/zMMuA7iu-XFJUKfkuGPBeI4_Gp_7X6a8gXMW-KUOmUtGhT7Pai50gC3nr3RRN0Y4

# High Availability
https://docs.google.com/document/d/1VWhsH47UVoHPL47KbgIcht0SnITa_dnWh2QTnoP1F2w/edit?usp=sharing

# AWS Lambda Functions and Autoscaling
https://docs.google.com/document/d/1K8XQhXQhNJSTlIM2FrO5pktcMRk382pjpdVmLjpSuqc/edit?usp=sharing
https://www.youtube.com/watch?v=CPCJAhYk2FE

# Deployment with AWS CloudFormation
https://blog.shikisoft.com/11-reasons-to-use-aws-cloudformation-for-provisioning-your-architecture/
https://docs.google.com/document/d/14eoraewD3PAillIwbzO7u_q7Z8yLBN_U_ou1QqR9Vys/edit?usp=sharing
https://lambdaschool.zoom.us/rec/share/1MNfMO3Iz0lLZIXrzmuFYbcdP6PBX6a8hiQa_KBfxUkqV_9vm2OJhnVO8Z7PKtxT
Access Password: a5?52.X$

# Implementing a Serverless Architecture with AWS Managed Services
https://drive.google.com/file/d/1t66QBGgLT1IIddcjh35hRXxvUviRO8kR/view?usp=sharing
https://docs.google.com/document/d/1aPhMweSMV1jh0xA7jt_ya1mOhzuUFmVcqy1glDGUJ5U/edit?usp=sharing
https://youtu.be/c6ugWCfJFc0

# CloudFront, Lambda and S3
https://medium.com/@austinlasseter/build-a-password-protected-website-using-aws-lambda-and-cloudfront-3743cc4d09b6
https://docs.google.com/presentation/d/106md4vzr9buRBIIrcJ455ynIvfC7ZRdAGzV3JhoatXA/edit?usp=sharing
https://github.com/austinlasseter/simple-website
https://youtu.be/lfwyX_9UE58

# Resize an Image with S3 and Lambda
https://medium.com/@austinlasseter/resize-an-image-using-aws-s3-and-lambda-fda7a6abc61c

# Deploying a Python App with Elastic Beanstalk
https://medium.com/@austinlasseter/deploying-a-dash-app-with-elastic-beanstalk-console-27a834ebe91d
https://youtu.be/J7wSZZjPbZs

# Additional Resources
https://github.com/open-guides/og-aws

