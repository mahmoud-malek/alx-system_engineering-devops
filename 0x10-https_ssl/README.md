# HTTPS SSL Project

This project is part of the SE Foundations curriculum. It focuses on the implementation and understanding of HTTPS and SSL.

## Background Context

This project aims to understand the implications of not securing website traffic and how to implement security measures to mitigate these risks.

## Resources

- [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [What are the 2 main elements that SSL is providing](https://www.ssl.com/faqs/what-is-ssl/)
- [HAProxy SSL termination on Ubuntu16.04](https://serversforhackers.com/c/using-ssl-certificates-with-haproxy)
- [SSL termination](https://www.nginx.com/resources/glossary/ssl-termination/)
- [Bash function](https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php)

## Learning Objectives

At the end of this project, you are expected to be able to explain:

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

### 0. World wide web

Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

### 1. HAproxy SSL termination

"Terminating SSL on HAproxy" means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
