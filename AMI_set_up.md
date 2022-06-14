# AMAZON MACHINE IMAGE (AMI)
## What is an AMI?
- An AMI is a supported and maintained an image/snapshot/blueprint/copy of an instance provided by AWS, which retains full functionality and set up of the original instance. Therfore, it does not require a manual set up.

## Use case of AMI

- When we are not using an instance we can either terminate it or stop it, we do this because it is cost effective. Terminating an instance is more cost effective than stopping it. However, if we go on a holiday and we terminate the instance,  we will have to go through all the manual set-up again when we are back, this will have some cost implication. Therefore, our goal is to terminate the instances so that we save money yet not lose the work. The way around it is to use AMI on AWS.
- I am on a holiday, someone else has to pick up my work while I am away. In this case having an AMI already built comes in handy because I can just pass the AMI to the next person, as the AMI has everything installed. All they have to do is ssh in run the update and upgrade and npm start and they are ready to go. This way i saved time, I saved cost, I did not lose any work and it makes the next persons life easier instead of sending them a long readme file with instructions to set up the instance.
## Benefits of AMI
- Ease of use
- Saves time
- Saves money
- Flexibility

