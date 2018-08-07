---
libvirt_name: "vm-1"
libvirt_title: "VM 1"
libvirt_description: "VM used for: Testing"
libvirt_memory: "2048"
libvirt_vcpus: "1"
libvirt_disk_size: "20"
libvirt_os_variant: "centos7.0"
libvirt_iso: "/home/abhishek/Downloads/CentOS-7-x86_64-DVD-1804.iso"
libvirt_ksfile: "/home/abhishek/vm-1.ks"
libvirt_network_hostif: "virbr0"
libvirt_http_host: '192.168.122.1'
libvirt_network_type: "bridge"
