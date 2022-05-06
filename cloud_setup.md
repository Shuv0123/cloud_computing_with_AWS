# Cloud Setup (step-by-step)
## setup access to EC2(VM) on AWS
- Move file.pem into .ssh folder, located in user directory (Shuvo)
- Give read only permission to the file.pem - "chmod 400 file.pem" in bash terminal

## EC2 set-up on AWS
- Search and select "EC2"
- Select "launch instance"
- Select "free tier" in the redirected page
- Select the machine of interest (in our case "Ubuntu 18.04")
- Select "t2 micro" since the app is not big only 3 pages
### Configuring instance details
- Number of Instance: 1
- Default network
- Select subnet default - DevOpsStudent - default euw ending in 1a
- Auto-assign public IP: Enable
- Leave the rest of the config the same
### Storage config
- Storage provided is more than enough
### Tag
-Add tag - "Name" "eng110_shuvo"
### Security group
- Create a new "Security Group", if one is not already been created for the same app being deployed
- Name it and give description "eng110_shuvo_app"
- When installing nginx
  - SSH - default port "22" source "My IP" which is the office ip or wherever working from. Give description
  - HTTP - port "80" with source being "Anywhere"
  - For the app we are delivering- Custom TCP port "3000" source "Anywhere"
### Launch
- Choose existing key pair
- eng119 | RSA
- connect instance

## Connect to created EC2 instance
- Allow the instance to start running
- Select the created instance
- Click "connect" which will redirect you to a new page 
- Click on "SSH client" and copy the command example
- Go on your git BASH
- cd .ssh
- Paste "command example"
- sudo apt-get update -y
- sudo apt-get upgrade -y
- sudo apt-get install nginx -y
- Go to your public IP
- Copy paste url on search bar - ready to go!
## Copying file from Localhost to EC2 (2 methods)
### Method 1 
- Push your files on github repository
- cd .ssh
- Paste "command example"
- git clone repository on VM
### Method 2 
- scp -i location/file.pem -r destination/dir ec2@ip.com:source/file/or/folder
  - scp -i ~/.ssh/eng119.pem -r ~/Desktop/sparta_repo/cloud_computing_with_AWS/starter_code ubuntu@ec2<ipaddress found on ec2 connect page>:/home/ubuntu
    - SCP is secure file proxy
    - -i is for files
    - -r folders

## How to run app
- given that the following steps have been ran:
  - cd .ssh
  - Paste "command example"
  - sudo apt-get update -y
  - sudo apt-get upgrade -y
  - sudo apt-get install nginx -y
  - cd /app
### Install node.js
- curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
- sudo apt install -y nodejs
- npm install
- npm start
## Reverse Proxy
- If in security group (inbound rule) the port 3000 not been added upfront
  - In Security Groups, edit inbound rules
    Custom TCP, set port range to 3000, access "Anywhere"
- on VM, cd to home
- cd /etc/nginx/sites-available
- sudo nano default
- Under location add the following:
  - location / { # First attempt to serve request as file, then # as directory, then fall back to displaying a 404. try_files $uri $uri/ =404; proxy_pass http://localhost:3000; }

  - location /fibonacci/ { proxy_pass http://localhost:3000/fibonacci/; }
- cd app
- npm start
## MongoDB set-up
- Search and select "EC2"
- Select "launch instance"
- Select "free tier" in the redirected page
- Select the machine of interest (in our case "Ubuntu 18.04")
- Select "t2 micro" since the app is not big only 3 pages
### Configuring instance details
- Number of Instance: 1
- Default network
- Select subnet default - DevOpsStudent - default euw ending in 1a
- Auto-assign public IP: Enable
- Leave the rest of the config the same
### Storage config
- Storage provided is more than enough
### Tag
-Add tag - "Name" "eng110_shuvo_MongoDB"
### Security group
- Create a new "Security Group", if one is not already been created for the same app being deployed
- Name it and give description "eng110_shuvo_app"
- When installing nginx
  - SSH - default port "22" source "My IP" which is the office ip or wherever working from. Give description
  - HTTP - port "80" with source being "Anywhere"
  - For the app we are delivering- Custom TCP port "3000" source "Anywhere"
### Launch
- Choose existing key pair
- eng119 | RSA
- connect instance

## Connect to created EC2 instance
- Allow the instance to start running
- Select the created instance
- Click "connect" which will redirect you to a new page 
- Click on "SSH client" and copy the command example
- Go on your git BASH
- cd .ssh
- Paste "command example"
