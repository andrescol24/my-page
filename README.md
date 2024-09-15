# My Page

## Minecraft
This project contains a minecraft subpage to start the service and see the current public IP. The scope of this is reduce expenses in AWS running the server 
only when it is neccesary. This functionality has a frontend which is in this project and AWS services:

### AWS Services

#### Certificate Manager
I created a Certificate Manager to enable the HTTPS in the CloudFront

#### Route 53
I have paid a domain in namecheap.com and I have create the Route 53 hosted zone to get the DNS service and make the domain pointing to CloudFront. Also I created
A and AAAA records for IPv4 and IPv6

#### CloudFront
I created a a distribution to show the S3 information. Important configurations:
- Error Page: as the S3 has a SPA (ReactJS) using other internal paths, I had to configure the error path to index.html because using internal paths like /minecraft it is detected as a wrong path.
- NoCache policy: as I am writing the public IP in S3 file I have disable the cache optimization.

#### S3
Normal S3 configured to host a static web app. Important things to have in mind:
- it is prefered to have the same domain name as the name of the S3 bucket
- We can create another S3 bucket to redirect trafic from www.superandres.com to superandres.com but in this case I did not do that, not neccesary.

### Lambda Functions
I created 2 lambda functions 1 to start the server and save the public IP in the S3 file and another one to stop the server and deleted the public IP. I am using Lambda URLs to avoid creating a API Gateway.