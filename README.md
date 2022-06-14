# Cloud Computing with AWS 

![](images/download.png)

### Keywords:
- AWS `Amazon Web Services`
- EC2 `Elastic Compute sercise`
- IAM `Identity Access Management`
- AZs `Availability Zones`
- prim `local host/ physical building`
- CAPEX `capital expenditure`
- OPEX `operational expenditure`
- EBS `Elastic Block Storage`

## What is Cloud Computing?
- They are services offered by third party companies to run virtual instances of physical hardware as a service that you as customer, organization or individual can use instead of using your own hardware and operating system. It allows flexibility and cost effectiveness, by allowing the user to choose and configure their own operating system, RAM, storage. Cloud computing is a pay as you go services.
## Why Cloud Compting (benefits)?

- Security 
- Cost
- scalability 
- reliability 
- accessability

the key benefit of Cloud Computing in terms of cost element is, you can never 100% predict the traffic.

e.g.(how is it cost effective)
Usually in Retail, yearly, it is expected that there will be a 10% increase in traffic. They have 2 servers, lets say the servers can handle 100M users. Therefore, if there is an increase in number of users, the comapny will buy upfront a new server/ building/ machine to host the new number of customers. For that building, they have to have a security guard, lock, electricity etc... so no return yet. So they invested that money in and they succesfully served all the new customers. During december they have high volume due to Xmas. However, when January comes the number of customer decreases drastically, but the hardware that was purchased is not being fully used. However, the cost in running is still there you still have to pay for security, electicity etc.. so it is not cost effective. So instead of investing on physical infrastructure, we take it on cloud we can increase the number of servers in demand and decrease it when this is less demand, which makes it cheaper. Nothing had to be built or bought, we just rented space that someone else has built.
Did not need to buy firewall, making it secure.

## CapEx vs OPEx
- CapEx is capital expenditure, its when a private company purchases all the physical hardware and infrastracture. So they are paying upfront for all the hardware. Wheras, OpEx operational expenditure, which is the infrastructre provided by AWS or google, so the company has to pay/rent those servers for operation.

## Security
Three types of security:
- On Prem (my responsability)
- Public Cloud (AWS responsability)
- Data in Transit (shared between me and AWS)

## Gov regions and security
- The Gov, NASA, CIA etc... they were all reluctant to go on cloud due to security reasons so special regions with special AZs only built for them and only them can access were created and used.

- Hybrid regions/AZ, Financial sector use Hybrid. We all have Bank accounts, and in that bank they have all our confidential information details, so they have to secure that data. They also have lots of data that they need to make publicly available, such as how to apply for an account, how to apply for morgatege, loan etc... On prem is expensive, cloud is cost effective. So they came up with this hybrid architecture. The banks have they have their physical data center where they keep all the confidential stuff they put in their own data center which they are directly responsible for from building to security etc... anything publicly available they store it in cloud. This way they have achieved Cost effectiveness scalabilty as well as security.

## Difference between Regions and AZ.
- one region must have at least 2 availability zones minimum. Regions are geographical location where Amazon/ microsoft store their Data Centers which they use to provide their services. 

https://aws.amazon.com/about-aws/global-infrastructure/

## High availabilty, why use multiple AZs?
- Let's say I am deploying an app in Ireland but I am only using 1 AZ and becasue of natural disaster, that physical data center got floded, my app will go down and disasters are hard to predict. So the way around it is to deploy my app in multiple AZs lets say in 1 and 2. Therfore if one goes down AWS services will check the status API status code 200 as soon as the satus code is not 200, the  traffic will be immediately redirected to the healthy instance/AZ. As soon as the instance in the othe AZ becomes availbale, AWS will divide the resources in between the instances. The app can also be deployed in multiple regions too then it comes down to cost, because the app will be running 24/7 so you have to look at the cost benefit analysis.

## How to choose AZs
- When chossing the region we have to think about the end user. The app should be deployed in a region closer to the end user region, so we should rent sapce nearest to the users. This is so we can prevent any lettency, up time, the repsonse time can be faster and easily achieved.

## Create a service (create a virtual machine online on a public cloud) 


![](images/AWS.png)

## Why do you want to refactor the monolythic architecture into a 2-tier architechture?
- how it will benefit the business?
- flexible? faster to use? scalable? higly available?

>[2-Tier Architecture Set-up](EC2_set_up.md) 

>[Amazon Machine Image(AMI) Set-Up](AMI_set_up.md)

>[Simple Storage Service S3](S3.md)

## Scale in/out vs Scale up/down
- Scale in/out is when you increse or decrease the number of instances/servers running. Whereas Scale up/down is when you increse the capacity of the instance or server how big the server is (storage)

>[Auto Scalling using Load Balancing](documentation/multi_AZs-autoscalling_group_with_LB_SETUP.md)



every product must have a disaster recovery plan
