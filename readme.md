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
test the Docker container locally 
- docker run -p 5000:5000 my_flask_app
Access the application at http://localhost:5000.
run with access to the container os:
- docker run -it -p 5000:5000 my_flask_app
run docker with openai key
- docker run -e OPENAI_API_KEY= "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" -p 5000:5000 my_flask_app




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
