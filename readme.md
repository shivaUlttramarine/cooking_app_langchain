1. install environment:
conda create --name env_cooking python=3.10
conda install --file requirements.yml
conda install --file D:\project\coocking\requirements.yml


1. install environemt:
conda env create -f requirements.yml
conda env create -f D:\project\coocking\requirements.yml

--remove env:
conda remove -n env_cooking --all


2.create bash file and give proper access:
 chmod +x ~/app.sh

3.connect to git:
 git config --global user.email "shiva.ghandi.bi.1992@gmail.com"
 git config --global user.name "shiva"
 -generate ssh and add it:
 ssh-keygen -t rsa -b 4096 -C "shiva.ghandi.bi.1992@gmail.com"
 ssh-add ~/.ssh/id_rsa
 -read public key and add it to git
 cat ~/.ssh/id_rsa.pub
 -check ssh:
 ssh -T git@github.com
-pass: 4270107

git remote add origin https://github.com/shivaUlttramarine/cooking_app_langchain.git

git add .
git commit -m ""
git push --set-upstream origin master
git push -u origin main
git push origin main

