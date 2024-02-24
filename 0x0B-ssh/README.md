## Background Context

In this project, you have been assigned an Ubuntu server located in a remote datacenter. The connection to the server is through SSH, utilizing an RSA key instead of a password. Your server has already been configured with the public key generated in a previous project shared on your intranet profile.

### Resources
Read or watch the following resources for better understanding:
- What is a (physical) server - [text](link) | [video](link)
- SSH essentials
- SSH Config File
- Public Key Authentication for SSH
- How Secure Shell Works
- SSH Crash Course
- Understanding the SSH Encryption and Connection Process
- Secure Shell Wiki
- IETF RFC 4251 (Description of the SSH Protocol)

### Learning Objectives

By the end of this project, you should be able to explain:
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`
4 explaining the script's purpose

### Your servers

| Name           | Username | IP               | State   |
|----------------|----------|------------------|---------|
| example-web-01 | ubuntu   | 0.0.0.0.0.0.0    | pending |

## Tasks

### 0. Use a private key
Write a Bash script using `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair:
- Private key named `school`
- 4096 bits key
- Key protected by the passphrase `betty`

### 2. Client configuration file
Share your SSH client configuration in your answer file, configured to use the private key `~/.ssh/school` and refuse authentication using a password.

### 3. Let me in!
Add the provided SSH public key to your server so that we can connect using the `ubuntu` user.

## Repository Information

### GitHub Repository
[alx-system_engineering-devops](repository_link)

### Directory
0x0B-ssh

### Files
- 0-use_a_private_key
- 1-create_ssh_key_pair
- 2-ssh_config
