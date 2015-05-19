#!/usr/bin/env python
import sys
import subprocess

cmd_list = ["create-volume", "move-volume", "delete-volume", "create-vm", \
        "copy-vm", "stop-vm", "poweroff-vm", "reboot-vm", "delete-vm", \
        "migrate-vm", "create-network", "delete-network", "show-config", \
        "delete-config", "get-info"]

if len(sys.argv) <> 3 or sys.argv[1] not in cmd_list:
    print """
Available commands are below:
    
    Storage:
        create-volume volume.conf
        move-volume   move-volume.conf
        delete-volume volume.conf

    VM:
        create-vm      vm.conf
        copy-vm      vm.conf
        stop-vm        vm.conf
        poweroff-vm        vm.conf
        reboot-vm        vm.conf
        delete-vm     vm.conf
        migrate-vm     migrate-vm.conf

    Network:
        create-network network.conf
        delete-network network.conf

    Config:
        show-config    volume|vm|network|all
        delete-config  volume|vm|network|all

    Infomation:
        get-info volume|vm|network|host|all
    """
    sys.exit(2)

def create_volume(config_file):
    # mkdir; chown; chmod; virsh create-volume update config
    pass

def move_volume(config_file):
    # vm_running?; mkdir; chown; copy volume; 
    # virsh create-volume; delete-volume; update config
    pass

def delete_volume(config_file):
    # vm_running?; delete-volume; update config
    pass

def create_vm(config_file):
    # find host with least running vms; mkdir; virsh create
    pass

def copy_vm(config_file):
    # vm_poweroff?; mkdir; chown; virsh create
    pass

def poweroff_vm(config_file):
    # virsh poweroff;
    pass

def reboot_vm(config_file):
    # virsh restart;
    pass

def stop_vm(config_file):
    # virsh shutdown;
    pass

def delete_vm(config_file):
    # any vm is using its backing file?; virsh delete;
    pass

def migrate_vm(config_file):
    # dest_host payload ok?; virtsh migrate
    pass

def create_network(config_file):
    # virsh create
    pass

def delete_network(config_file):
    # virsh delete
    pass

def show_config(obj):
    # show config
    pass

def delete_config(obj):
    # any object is using this config?; delete
    pass

def get_info(obj):
    # if volume; get path & usage & vms; if network; get type & ip;
    # if vm; get name & memory & cpu & graphic_info & host
    # if host; get running_vms & cpu & memory
    pass

def sample_cmd(config_file):
    try:
        cmd = "virsh define %s" % config_file
        print cmd
    except Exception as e:
        print e
        exit(1)

if sys.argv[1] == "sample-cmd":
    create_vm(sys.argv[2])
