# weblogic
Weblogic Installation and Configuration

Step 1: Fist create a Weblogic Installation job in jenkins using the Weblogic Installation.sh script here.
Note : this job should have 2 string parameters - FMW_VERSION and BASE_HOME (where installation should happen)

Step 2: Configure a domain using file - DomainCreation_Properties.py and create "OPENSTYLE" job with below commands and no parameters-

. $HOME/.bash_profile
rm -rf weblogic
git clone https://github.com/adis2hope/weblogic.git

cd weblogic

wlst DomainCreation_Properties.py

Step 3: Not yet done ( start admin server and add managed server followed by deployment)
