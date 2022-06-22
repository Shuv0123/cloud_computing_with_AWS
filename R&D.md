
## Listener Groups
- A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

Listeners support the following protocols and ports:
- Protocols: HTTP, HTTPS
- Ports: 1-65535



## Launch Template for ASG 
- A launch Template for Auto Scaling group (ASG) contains information that specify the necessary information to configure the Amazon EC2 instances, the Availability Zones and VPC subnets for the instances, the desired capacity, and the minimum and maximum capacity limits.

- you can create a new version of the launch template. After you change the launch template for an Auto Scaling group, any new instances are launched using the new configuration options, but existing instances are not affected. To update the existing instances, terminate them so that they are replaced by your Auto Scaling group, or allow auto scaling to gradually replace older instances with newer instances based on your termination policies.

## launch config vs launch template
- Launch template is similar to launch configuration which usually Auto Scaling group uses to launch EC2 instances. However, defining a launch template instead of a launch configuration allows you to have multiple versions of a template.

- recommend that we should use launch templates instead of launch configurations to ensure that we can leverage the latest features of Amazon EC2, such as T2 Unlimited instances.

- launch configurations are used with Auto Scaling Groups. While launch templates are used when you launch an instance using the aws EC2 console, an AWS SDK, or a command line tool.

- Launch templates enable you to store the parameters (AMI, instance type, security groups, and key pairs etc.) so that you do not need to define these parameters every time you launch a new instance.




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
- A network access control list (NACL) is an added layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. 

- what is the difference between NACL and a security group
- security group works at instance level
- NACL controls the in and out rules 


# What is CI-CD-CDE

- CI-CD is the backbone of DevOps practices and automation for faster software release.

- Continuous integration (CI) - Continuous merging/commiting of branches to the master branch, automated build and test process.

- Continuous delivery (CD) ectension of CI, it provides continuous release of new changes to customer in a sustainable way. in CD deployment is manual.

- Continuous deployment (CDE) is the whole process of coding, testing and deployment is continuos 

# what is the difference between CD & CDE
- in CD everything is continuous except for the the deployment, which is manual whereas in CDE the whole process starting from sourcing till production is continuos

# What is jenkins, what are the benefits?
- Jenkins is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration and continuous delivery. It is a server-based system that runs in servlet containers such as Apache Tomcat.

benefits 
- it is an open-source tool with great community support.
- It is easy to install.
- It has 1000+ plugins to ease your work. If a plugin does not exist, you can code it and share it with the community.
- It is free of cost.
- It is built with Java and hence, it is portable to all the major platforms.
# What is the SDLC using Jenkins stages


lunch configuration immutable
lunch template is mutable



ami replicas immutable

scale out multi azs