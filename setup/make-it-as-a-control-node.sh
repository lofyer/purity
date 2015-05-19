#!/bin/bash
if [ -e ~/.ssh/id_rsa.pub ]
then
    echo "Copying ssh public key..."
    declare -a HOSTS=($(cat hosts.list))
    cnt=${#HOSTS[@]}
    for ((i=0;i<cnt;i++)); do
        cat ~/.ssh/id_rsa.pub | ssh ${HOSTS[i]} 'mkdir .ssh; cat >> ~/.ssh/authorized_keys2; chmod 700 ~/.ssh; chmod 640 ~/.ssh/authorized_keys2'
    done
else
    echo "Please generate your ssh public key without password:\n\tssh-keygen -t rsa"
fi
