#!/usr/bin/env python
import sys
import subprocess

cmd_list = ["create-storage", "create-vm", ""]

if len(sys.argv) <> 3 or sys.argv[1] not in cmd_list:
    print """
Available commands are below:
    
    Storage:
        create-storage storage.conf
        move-storage   storage.conf
        delete-storage storage.conf

    VM:
        create-vm      vm.conf
        stop-vm        vm.conf
        migrate-vm     migrate-vm.conf

    Network:
        create-network network.conf
        delete-network network.conf
    """
    sys.exit(2)

def create_storage(config_file):
    pass

def create_vm(config_file):
    try:
        cmd = "virsh define %s" % config_file
        print cmd
    except Exception as e:
        print e
        exit(1)

if sys.argv[1] == "create-vm":
    create_vm(sys.argv[2])
