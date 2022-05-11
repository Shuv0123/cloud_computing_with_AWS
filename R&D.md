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


# what is VPC
VPC is the networking layer for Amazon Elastic Compute Cloud (Amazon EC2) and provides a private, isolated section of the AWS Cloud where you can launch AWS services and other resources in a virtual network.

## Iternet gateway
A computer that sits between different networks or applications. The gateway converts information, data or other communications from one protocol or format to another. A router may perform some of the functions of a gateway. An Internet gateway can transfer communications between an enterprise network and the Internet.

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. An internet gateway enables resources (like EC2 instances) in your public subnets to connect to the internet if the resource has a public IPv4 address or an IPv6 address. Similarly, resources on the internet can initiate a connection to resources in your subnet using the public IPv4 address or IPv6 address. For example, an internet gateway enables you to connect to an EC2 instance in AWS using your local computer.

An internet gateway serves two purposes: to provide a target in your VPC route tables for internet-routable traffic, and to perform network address translation (NAT) for instances that have been assigned public IPv4 addresses. For more information, see Enable internet access.

An internet gateway supports IPv4 and IPv6 traffic. It does not cause availability risks or bandwidth constraints on your network traffic. There's no additional charge for having an internet gateway in your account.


## Routing table
A route table contains a set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.

## WHat is a subnet
A subnet, or subnetwork, is a network inside a network. Subnets make networks more efficient. Through subnetting, network traffic can travel a shorter distance without passing through unnecessary routers to reach its destination.

## WHat is CIDR block (Classes inter Domain Routing)
The CIDR block is a fixed prefix length of /56

## Sub-mask
A subnet mask is a 32-bit number created by setting host bits to all 0s and setting network bits to all 1s. In this way, the subnet mask separates the IP address into the network and host addresses.

Every device has an IP address with two pieces: the client or host address and the server or network address. IP addresses are either configured by a DHCP server or manually configured (static IP addresses). The subnet mask splits the IP address into the host and network addresses, thereby defining which part of the IP address belongs to the device and which part belongs to the network.

## what is an IP
- IP is short for internet protocol. An internet protocol is essentially a set of predetermined rules that structure and format the data we send over internet networks. 

- IP is fundamental to allowing our devices to communicate with each other. It is the IP address that acts as the identifier and differentiates each individual device connected to a network.

- Each computer, smartphone, tablet, laptop, IP PBX, or router has its own unique IP address. This is a unique string of numbers separated by decimals. Each decimal number is called an Octet. 

## IP-network

- An IP network refers to any group of devices, each with their own unique IP addresses, connected under the same network topology. Devices connected to a shared IP network can send and receive information. 

- A private IP network allows data to be shared between connected devices securely, by enforcing password protected connectivity that allows only those devices in your office or home to access the IP network

## NACL
- A network access control list (NACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. 
