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
(The command require sudo). This is not root access, it is called key-based authentication. 
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
After completion of the AWS configuration, the instance is given a defualt user name: ec2-user.
We may want create a new user.
	useradd -c "DESCRIPTION" USERNAME
Set password for new user
	passwd USERNAME

Switch to other user from current
	su - USERNAME
Then system would ask for user's password. 
Add user to a group (optional)
	usermod -aG GROUP USERNAME
The command can add user to a group. For instance, allow user to use sudo.

Create a .ssh directory to save the public key. This requires to generate the public-key from the key-pair which downloaded after completing the setting of AWS instance. This sounds very fishy, since the public key would be the same for new user compare to the original default user which is ec2-user. But scine that ssh-keygen generates the public-key, so it is fine. Because we are connecting to the same server just different user. (File or direcotry start with . would not be shown in windows FS).
1.mkdir .ssh in the USER directory. 
	mkdir .ss
2.change mode for the directory to give rwx to the owner of the dicrectory. (This change is for only rwx by the owner, others can do none of them)
	chmod 700 .ssh 
3.create a new file to save the public key. (This change is for the owner can only rx the file.)
	touch authorized_keys
4.chage mode for the file to give rw to the file to owner.
	chmod 600 authorized_keys

Once the preparation was done, we can try to use ssh to connect the new user of the instance. But unfortunately the permission was denied. I have tried also mobify the sshd_config to allow both publicke and password as the authentication methods. The result was saying "port 22: Resource temporarily unavaliable. So I guess AWS does not allow this behaviour. Therefore we need to follow the guidence from link https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/. The step requires use adduser instead of useradd and also needs to disable the password while creating any new user. But AWS offers add IAM user which seems to be a solution for new user to have their own password authentication.

So, long words in short, we may first with the methods from the link then try with adding an IAM user.(the DNS is the root, ec2-user@DNS is the default user of the instance) 

5.verify the key-pair fingerprint "From the computer where you downloaded the private key file, generate an SSH2 fingerprint from the private key file. The output should match the fingerprint that's displayed in the console." The loacal ssh2 fingerprint should be generated as below to match with the one in the instance. ssh-key gen -l is the ss11 type fingerprint which would not match with the one in the instance.
	finger print shows while logging on the instance: SHA256:G5lAUL3ZTqtgy+HG5qtOkvmcpPX6N1Fifp1xKXs6AY4 
	openssl pkcs8 -in path_to_private_key -inform PEM -outform DER -topk8 -nocrypt | openssl sha1 -c
The finerprint conversion from PEM to DER
b7:b6:ad:6b:0c:03:48:5b:75:08:b1:47:68:c6:91:8d:c9:6c:72:b3

6. generate the public key from the key-pair.PEM
	ssh key-gen -y -f /PATH/KEY-PAIR.PEM
7. Try to connect the new user of the instance...which failed again as permission denied.

8. After managing the public-key with care, finally got succeed. We should care with that append the default user's .ssh/authorized_key with new public key and copy only the new public key to the new user's .ssh/authorized_key. The fishy part from begining is that the guidence doesn't tell this directly, the detail was in another link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#verify-key-pair-fingerprints.

9. Log off from the AWS instance requires the following command. If we are not logged on the defualt user, the command will direct us to the default user.
	exit 
 
