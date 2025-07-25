#!/bin/bash

# This script installs Containerlab and its dependencies on a Linux system.

sudo dnf remove -y podman runc

sudo dnf install -y gcc gcc-c++ kernel-devel dnf-plugins-core

sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

systemctl enable --now docker


