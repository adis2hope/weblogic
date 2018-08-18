###########################################################
# This script will dynamically create the domain as per your inputs

###########################################################
import os
WLHOME=os.environ['WL_HOME']
AdminName=os.environ['ADMIN_NAME']
AdminListenAdr=os.environ['ADMIN_LIST_ADD']
AdminListenPort=os.environ['ADMIN_LIST_PORT']
AdminUsrName=os.environ['ADMIN_USR_NAME']
AdminPassword=os.environ['ADMIN_PASS']
domainPath=os.environ['DOMAIN_PATH']
domainName=os.environ['DOMAIN_NAME']
#==========================================
# Create a domain from the weblogic domain template.
#==========================================
readTemplate(WLHOME+'/common/templates/wls/wls.jar')
cd('Servers/AdminServer')
#AdminName=raw_input('Please Enter Admin ServerName: ')
set('Name',AdminName)
#==========================================
# Configure the Administration Server
#==========================================
#AdminListenAdr=raw_input('Please Enter Admin Listen Address: ')
#AdminListenPort=input('Please enter Admin listen Port: ')
set('ListenAddress',AdminListenAdr)
AdminListenPort_int=int(AdminListenPort)
set('ListenPort', AdminListenPort_int)
#====================================================
# Define the password for user weblogic. You must define the password before you
# can write the domain.
#====================================================
cd('/')
cd('Security/base_domain/User/weblogic')
#usr=raw_input('Please Enter AdminUser Name: ')

set('Name',AdminUsrName)

#AdminPassword=raw_input('Please enter Admin password:')

cmo.setPassword(AdminPassword)

# - OverwriteDomain: Overwrites domain, when saving, if one exists.

setOption('OverwriteDomain', 'true')
#==============================================
# Write the domain, close template and finally exit from the WLST
#==============================================
#domainPath=raw_input('Enter the domain path: ')
#domainName=raw_input('Enter domain name: ')
print 'Given domain path, name : ', domainPath, domainName
writeDomain(domainPath+"/"+domainName)
closeTemplate()
exit()
