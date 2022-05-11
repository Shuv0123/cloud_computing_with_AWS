# Highly Available and scalability multi AZs deployment
## What is Load Balancing and its benefit
-  Load balancing is the process of distributing network traffic across multiple servers. This ensures no single server bears too much demand. 

Benefits of spreading the work evenly:
- improves application responsiveness
- increases availability of applications and websites for users.
## Listener Groups
- A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

Listeners support the following protocols and ports:
- Protocols: HTTP, HTTPS
- Ports: 1-65535

## ASG?

- An Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

## Launch Template for ASG 
- A launch Template for Auto Scaling group (ASG) contains information that specify the necessary information to configure the Amazon EC2 instances, the Availability Zones and VPC subnets for the instances, the desired capacity, and the minimum and maximum capacity limits.

- you can create a new version of the launch template. After you change the launch template for an Auto Scaling group, any new instances are launched using the new configuration options, but existing instances are not affected. To update the existing instances, terminate them so that they are replaced by your Auto Scaling group, or allow auto scaling to gradually replace older instances with newer instances based on your termination policies.

## launch config vs launch template
- Launch template is similar to launch configuration which usually Auto Scaling group uses to launch EC2 instances. However, defining a launch template instead of a launch configuration allows you to have multiple versions of a template.

- recommend that we should use launch templates instead of launch configurations to ensure that we can leverage the latest features of Amazon EC2, such as T2 Unlimited instances.

- launch configurations are used with Auto Scaling Groups. While launch templates are used when you launch an instance using the aws EC2 console, an AWS SDK, or a command line tool.

- Launch templates enable you to store the parameters (AMI, instance type, security groups, and key pairs etc.) so that you do not need to define these parameters every time you launch a new instance.

## why should we create auto scaling group
- The Auto Scaling group continues to maintain a fixed number of instances even if an instance becomes unhealthy. If an instance becomes unhealthy, the group terminates the unhealthy instance and launches another instance to replace it. For more information, see Health checks for Auto Scaling instances.

## Setting up Instance- Launch Template
- go to your instances
- on left side scroll and click Instances - Launch Template 
- Create Launch Template
- Launch Template Name - "eng110-shuvo-asg-launch-template"
- Description - "eng110-shuvo-asg-launch-template"
- select "Provide guidance to help me set up a template that I can use with EC2 Auto Scaling"
- add template tag - "Name" "eng110-shuvo-asg-launch-template"
- on Application and OS Images (Amazon Machine Image)
   - select the machine you want to use 
- select key pair log in - eng119.pem
- launch app instance