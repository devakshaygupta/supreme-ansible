# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set default user
ARG USERNAME=vscode

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/workspace/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/workspace/.venv"

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    openssh-client \
    python3 \
    python3-pip \
    python3-venv \
    podman \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment and install requirements
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m venv /workspace/.venv && \
    /workspace/.venv/bin/pip install --upgrade pip && \
    /workspace/.venv/bin/pip install -r /tmp/requirements.txt

# Set default shell
SHELL ["/bin/bash", "-c"]

RUN useradd -m $USERNAME --shell /bin/bash
USER $USERNAME
