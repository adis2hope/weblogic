###########################################################
# This script will dynamically create the domain as per your inputs
###########################################################
import os
WLHOME=os.environ['WL_HOME']
domainLoc=os.environ['MW_HOME']
loadProperties('labWLSTdom.properties')

def printInStyle(txt):
 print'-'*10 +txt
 
#==========================================
# Create a domain from the weblogic domain template.
#==========================================
print(WLHOME)
#readTemplate("/u01/app/software/mw_home/fmw/oraclehome/wlserver/common/templates/wls/wls.jar")
selectTemplate(WLHOME+'/common/templates/wls/wls.jar','12.2.1.3')
loadTemplates()
printInStyle('Setting AdminServer name')
cd('Servers/AdminServer')
set('Name',adminServerName)
#==========================================
# Configure the Administration Server
#==========================================
printInStyle('Set the ListenAddress and ListenPort')
set('ListenAddress',adminServerListenaddr)
set('ListenPort', int(admlistenport))
#====================================================
# Define the password for user weblogic. You must define the password before you
# can write the domain.
#====================================================
printInStyle('Creating Password')
cd('/')
cd('Security/base_domain/User/weblogic')
set('Name',adminUser)
cmo.setPassword(adminPassword)

printInStyle('Setting StartUp Options')
setOption('OverwriteDomain', 'true')
#==============================================
# Write the domain, close template and finally exit from the WLST
#==============================================
print 'Given domain path, name : ', domainLoc, domainName
# Create Domain to File System
printInStyle('Writing Domain To File System')
writeDomain(domainLoc+"/"+domainName)
closeTemplate()

# Exiting
print('Exiting now...')
exit()
