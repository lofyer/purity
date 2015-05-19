#!/bin/bash

# Add id_rsa.pub to each host
declare -a HOSTS=($(cat hosts.list))
cnt=${#HOSTS[@]}

# Install essential pkgs in each host.
cmd_yum="yum install -y libvirt glusterfs-{server,client} qemu-kvm"
for ((i=0;i<cnt;i++)); do
    echo -en "${HOSTS[i]}\n$@\n"
    ssh ${HOSTS[i]} $cmd_yum
done

cmd_config="sed XXX;chkconfig glusterd on; chkconfig glusterfsd on; chkconfig libvirtd on"

# Generate configuration files for services
for ((i=0;i<cnt;i++)); do
    echo -en "${HOSTS[i]}\n$@\n"
    echo $cmd_config | ssh ${HOSTS[i]} 'bash'
done

# In first host run: Create Volume
cmd_gluster="gluster volumn create; set; start"
echo $cmd_config | ssh ${HOSTS[0]} 'bash'
