set -x

#--> prepare required dirs
mkdir -p /mnt/tutor
mkdir -p /mnt/work

#--> mount windows shared folders
sudo mount -t cifs //192.168.56.1/tutor /mnt/tutor -o username=waltertutor,password=tutor1234,vers=3.0 
sudo mount -t cifs //192.168.56.1/work /mnt/work -o username=waltertutor,password=tutor1234,vers=3.0 
set +x
