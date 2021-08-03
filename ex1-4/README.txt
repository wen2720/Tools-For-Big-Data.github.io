Exercise 1.4:
Launch a t2.micro instance on Amazon EC2. Log onto the instance, create some files and install some software (for example git).

(You have to enter your credit card to make an Amazon account. If you want to make sure you do not spend any money, you can remove your account when you are finished with the exercises. If you really don’t want to do this, you can use the GBar instead of Amazon.

The following link:https://aws.amazon.com/ec2/getting-started/ helps to go through the task. We have to consider which OS we are using to connect the AMI because of the ssh key file format and the connection method are different for *nix and Windows.

Security groups:
Set inbound rules in the security groups by adding new rules with setting the type and other fileds. For instance, type:ssh ; protocol:IPv4 destination; prot:22 and source 0.0.0.0/0. 

Creating key-pair 
The step requires to name a key-pair file name and choosing between either.pem or .ppk format. Then the key file would be downloaded

Launch:
To log onto the instance, we need to configure the series of settings beforehand. First step requires us to choose the brand of the Amazon Machine Image. Then the second step is to configure the instatnce details such as the number of the instances, etc. The third step is to add hard drive for the AMI. The fourth step is to add tag for the instance. Then the sixth step is to set the security groups as mentioned before. The last setting is to create and add the key-pair. Finally, the instance would run by clicking the launch button.

Connect to the instance.
As we are working the *nix we would like to have .pem downloaded for connecting the instance. We need to give file read permission to the key-file owner.
	chmod 400 FILENAME.pem
Then we can connect to the instance with secure shell by using the following command.
	ssh -i PATH/FILENAME.pem USER@AWS-PUBLIC-DNS.

Finger print
(Optional, to prevent man-in-the-middle attack)

Creating file
If everything were going fluently, at this point, we have already connected to the instance. Creating file is easy as the instance have some basic bash commands such as touch. Note, in Red Hat vi is installed already.

Install a software for i.e. git
yum is one of the front-tool of Red Had package manager. We can use it to install git. We can first check whether it has been installed with following command.
	yum list installed | grep git
Since, the instance does not have git, so we can install it with the following command:
	yum install git 

Create a new user
We may want create a new user because during the luanching configuaration, a default username is created.
	useradd -c "Wenhao" wen 
