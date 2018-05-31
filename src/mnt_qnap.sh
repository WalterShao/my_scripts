set -x

#--> prepare required dirs
mkdir -p /mnt/rr2_src
mkdir -p /mnt/hbs_src
mkdir -p /mnt/cloud_ucc
mkdir -p /mnt/c28


#--> mount qnap nas source code folders
sudo mount -t nfs 172.17.28.27:Public/rr2_src /mnt/rr2_src/
sudo mount -t nfs 172.17.28.27:Public/hbs_src /mnt/hbs_src/
sudo mount -t nfs 172.17.28.27:Public/cloud_ucc /mnt/cloud_ucc/
sudo mount -t nfs 172.17.28.27:Public/MD882/mediaDash /mnt/c28/

set +x
