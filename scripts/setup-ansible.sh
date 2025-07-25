#!/bin/bash

# This script sets up Ansible and podman.

set -e

sudo dnf update -y

sudo dnf config-manager --enable ansible-automation-platform-2.4-for-rhel-9-x86_64-rpms

sudo dnf install ansible-builder ansible-core ansible-navigator containernetworking-plugins squashfs-tools gcc gcc-c++ kernel-devel dnf-plugins-core -y

sudo systemctl enable --now podman

mkdir -pv ~/.config/containers/systemd

cp /usr/share/containers/containers.conf ~/.config/containers/containers.conf

touch ~/.config/containers/registries.conf

cat <<EOF >> ~/.config/containers/registries.conf
unqualified-search-registries=["docker.io", "registry.redhat.io"]

[[registry]]
location="docker.io"
blocked=false

[[registry]]
location="registry.redhat.io"
blocked=false
EOF

