# Use Ubuntu as the base image
FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    openssh-client \
    python3 \
    python3-pip \
    podman \
    podman-compose \
    && rm -rf /var/lib/apt/lists/*

# Install ansible-navigator
RUN pip3 install ansible-navigator

# Set default shell
SHELL ["/bin/bash", "-c"]

# Set default user
ARG USERNAME=vscode
RUN useradd -m $USERNAME --shell /bin/bash
USER $USERNAME
