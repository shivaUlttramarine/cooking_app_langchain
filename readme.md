1. install environemt:
- conda env create -f requirements.yml
- conda env create -f D:\project\coocking\requirements.yml
--remove env:
- conda remove -n env_cooking --all


2.create bash file and give proper access:
 - chmod +x ~/app.sh

3.connect to git:
 - git config --global user.email "shiva.ghandi.bi.1992@gmail.com"
 - git config --global user.name "shiva"
 generate ssh and add it:
 - ssh-keygen -t rsa -b 4096 -C "shiva.ghandi.bi.1992@gmail.com"
 - ssh-add ~/.ssh/id_rsa
 read public key and add it to git
 - cat ~/.ssh/id_rsa.pub
 check ssh:
 - ssh -T git@github.com
pass: 4270107

- git remote add origin https://github.com/shivaUlttramarine/cooking_app_langchain.git

- git add .
- git commit -m ""
- git push --set-upstream origin master
- git push -u origin main
- git push origin main

3. dockerize:----------------------------------------
create .dockerignore
Build docker image:
in the folder of where your Dockerfile exists:
- docker build -t my_flask_app .
- docker images
Access the application at http://localhost:5000.
run with access to the container os:
- docker run -it -p 5000:5000 my_flask_app
run docker with openai key
- docker run -e OPENAI_API_KEY= "xxxxx" -p 5000:5000 my_flask_app



-------------------------------------
4. INSTAll AWS CLI:
install CLI: https://aws.amazon.com/cli/
cmd --> aws --version

install the library in conda environment in anaconda
- pip install awscli --upgrade --user
- aws --version

-- get access key and secret-key from aws for cli
- create a  user
- adde access key to user
- copy acces-key and secret acces-key

--- configute cli aws:
aws configure
add this cases:
AWS Access Key ID [None]: AKIAS2HWA7MHGUAKVFZC
AWS Secret Access Key [None]: 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
Default region name [None]: eu-central-1
Default output format [None]: json
verify configuration:
-aws sts get-caller-identity
-aws s3 ls


5. connect to EC2:
create EC2 and save coockingapp.pom
make sure just your user has access to coockingapp.pom
click on instance -> connect -->ssh client --> take the code:
connect to ec2:
- cd D:\project\coocking\for me
- ssh -i /path/to/your-key.pem ubuntu@ec2-your-ip-address.compute-1.amazonaws.com
- ssh -i "cookingapp.pem" ubuntu@ec2-35-159-25-78.eu-central-1.compute.amazonaws.com
install required libs on os:
- sudo apt update && sudo apt upgrade
- sudo apt install git
- python3 --version
sudo apt install python3 python3-pip
- sudo apt update && sudo apt upgrade
- sudo apt install python3-venv
- sudo apt install nginx

4. add Docker image to ECR by CLI
 take your repository id:
----- do to repository you created and click on publis
----- on windows you can see user_id and sample code
 login to ECR repo
-- aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com  :
-aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 193789491982.dkr.ecr.eu-central-1.amazonaws.com
tag docker:
- docker tag <your-image>:<tag> <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/<repository-name>:<tag>
- docker tag my_flask_app:latest 193789491982.dkr.ecr.eu-central-1.amazonaws.com/cooking:latest

push:
- docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/<repository-name>:<tag>
- docker push 193789491982.dkr.ecr.eu-central-1.amazonaws.com/cooking:latest

verify:
-aws ecr list-images --repository-name <repository-name> --region <your-region>
-aws ecr list-images --repository-name cooking --region eu-central-1.amazonaws.com




-------------------- node js and React:
 check version of installed libs:
- node -v
- npm -v
install react-native
- npm install -g react-native-cli
