## VPC SET-UP - analogy (land postcode)
- Go on VPC
- Select Your VPCs from the left window
- Create VPC 
  - select VPC only
  - Name tag "eng110-shuvo-vpc"
  - IPv4 CIDR - used "10.0.0.0/16" but it is calculated using subnet sizing
  - Click on Create VPC

Now we have an isolated empty space in the irland region with a validated address, which means we can start adding components in it. Next thing to do is to provide the Virtual Private Cloud (VPC) with internet, so we are gonna create an internet gateway.

## Internet Gateway SET-UP
- Select from the left VPC - Internet Gateways
- Create Internet Gateway
  - Name tag - "eng110-shuvo-ig"
- Click on Create Internet Gateway

Now we have the internet gateway somewhere, this IG does not know which VPC to provide internet to. so we have to attach this IG to our created VPC.

## Connect IG to VPC
- Select "Internet Gateways" from the left scroll down menu
- Search and select your IG "eng110-shuvo-ig
- Click on Action
   - Attach to VPC
   - Search and select your VPC
   - Click on Attach Internet gateway

Now that the internet is set up, it needs a routing table that routes the traffic to our subnets. So we first set up our subnet and then a route table.

## Subnet SET-UP   - analogy (house)
- Select Subnet from the left drop down menu
- Create Subnet
- Select the VPC where you want to create the subnet - "eng110-shuvo-VPC-"
- Subnet settings
  - Subnet Name "eng110-shuvo-sb-public" we add public so that we can differentiate from subnets we are gonna build in futrue that need to be private eg. mongodb database
- IPv4 CIDR block - analogy (door number)
  - specific for user to user - 10.0.1.0/24 (sharukh's) 10.0.8.0/24 (mine)
- Select Create Subnet

analogy - within that postcode (VPC) we have a house reserved (subnet) wit a specific door number (IPv4 CIDR block - 10.0.8.0/24 (mine)). We need to provide internet to the house (subnet) from the land

## Route Table SET-UP - analogy (traffic lights)
- Select Route Table from the left side drop down menu
- Select the Route table if it has been procided, otherwise create one 
  - Name tag - eng110-shuvo-rt-public
  - Select VPC (eng110-shuvo-vpc)
- Click Create route table

When I create this route table only knows which VPC we are in but doesn't know which subnet yet. So we need to connect the route table to the internet gateway to bring the external traffic in.

## Connect Route Table to internet gateway
- scroll down in your existing/created Route Table
- Under Routes click "Edit Routes"
- Add route
   - Destination "everywhere" - 0.0.0.0/0
   - Target "internet Gateway" - select my internet gateway
- Save changes

Upper level Architecture completed! Now tell route table to provide internet from gateway to subnet and any subnet we are gonna add in the future.

## Connect Route Table to Subnet
- scroll down in your existing/created Route Table
- Under Subnet Association 
  - First window/tab - select "Edit subnet association"
  - only one subnet listed, because we have selcted/created only one subnet.
  - Select the subnet you want to connect to 
- Save association

Now we have internet in our subnet from the external world through the VPC using the IG directed by the route table.

We can launch an EC2/AMI using our on VPC architecture details
- network - eng110-shuvo-vpc
- subnet - eng110-shuvo-sb-public
- auto assign public IP - yes

### To allow app instance to access DB, DB security group should allow public subnet through port 27017
 
inbound rule things can be done to me 
outbond rule things i can do 
 


