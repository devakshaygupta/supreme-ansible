# Use Ubuntu as the base image
FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    python3 \
    python3-pip \
    software-properties-common \
    podman \
    && rm -rf /var/lib/apt/lists/*

# Install ansible-navigator using pip
RUN pip3 install ansible-navigator

# Set default user
ARG USERNAME=vscode
RUN useradd -m $USERNAME
USER $USERNAME
