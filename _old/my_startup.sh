set -x

#!/bin/sh
sudo dhclient -r 
sudo dhclient 

#--> send VM info to my gmail
#python /home/waltershao/my_startup.py

#--> prepare required dirs
mkdir -p /mnt/tutor
mkdir -p /mnt/work

#--> mount windows shared folders
#sudo mount -t cifs //192.168.70.1/tutor /mnt/tutor -o username=waltertutor,password=tutor1234 
#sudo mount -t cifs //192.168.70.1/work /mnt/work -o username=waltertutor,password=tutor1234 
set +x
