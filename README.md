# supreme-ansible

Automate the configuration and management of network devices (VyOS, Nokia SR Linux) using Ansible.

---

## 📦 Structure

- `inventory.yml` — Inventory of network devices and groups
- `ansible.cfg` — Ansible configuration (paths, defaults)
- `group_vars/` & `host_vars/` — Per-group/host variables (supports environment variable lookups)
- `playbooks/` — Main playbooks for configuration, backup, and automation
- `collections/` — Custom and community Ansible collections
- `scripts/` — Setup scripts for Ansible and container tools

## 🚀 Quick Start

### 1. Prerequisites

- Codespaces or a Linux environment with Ansible and Podman
- Network connectivity to your devices
- SSH keys and credentials (use Codespace secrets for sensitive data)

### 2. Setup

```bash
# Install dependencies
scripts/setup-ansible.sh
```

### 3. Configure Secrets & Variables

- Add Codespace secrets (e.g., `ANSIBLE_VYOS_USER`, `ANSIBLE_VYOS_PRIVATE_KEY`)
- Reference them in `group_vars/vyos.yml`:

  ```yaml
  ansible_user: "{{ lookup('ansible.builtin.env', 'ANSIBLE_VYOS_USER') }}"
  ansible_ssh_private_key_file: "{{ lookup('ansible.builtin.env', 'ANSIBLE_VYOS_PRIVATE_KEY') }}"
  ansible_network_os: vyos.vyos.vyos
  ```

- Repeat for other device groups as needed.

### 4. Run Playbooks

```bash
ansible-playbook -i inventory.yml playbooks/configure-vyos.yml
```

## 🛠️ Troubleshooting

- Ensure your Codespace secrets are set and available as environment variables
- Check device connectivity and SSH access
- Review playbook output for module-specific errors

## 📚 References

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Network Guide](https://docs.ansible.com/ansible/latest/network/index.html)
- [Using Environment Variables in Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#defining-variables-at-runtime)

---

Supports automation for VyOS and Nokia SR Linux devices. See individual playbooks and scripts for more details.
