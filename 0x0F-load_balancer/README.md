# Load Balancer Project

## Overview

This project focuses on enhancing the web stack by implementing redundancy for web servers using a load balancer. The goal is to improve the infrastructure's reliability, allowing for increased traffic handling and ensuring continued service in case of a server failure.


### Servers

| Name           | Username | IP              | State   |
| -------------- | -------- | --------------- | ------- |
| 433785-web-01  | ubuntu   | 18.204.10.149   | running |
| 433785-web-02  | ubuntu   | 34.239.254.0    | running |
| 433785-lb-01   | ubuntu   | 34.202.233.8    | pending |

## Tasks

### Task 0: Double the Number of Webservers

In this task, configure `web-02` to match `web-01` and add a custom Nginx response header. Write the script `0-custom_http_response_header` to automate the configuration on a new Ubuntu machine.

### Task 1: Install Your Load Balancer

Install and configure HAproxy on `lb-01` to distribute traffic to `web-01` and `web-02` using a round-robin algorithm. Ensure HAproxy can be managed via an init script.

## How to Use

### Task 0

```bash
./0-custom_http_response_header
```

### Task 1

```bash
./1-install_load_balancer
```

## Examples

Example response header:

```bash
curl -sI 34.198.248.145 | grep X-Served-By
# X-Served-By: 03-web-01
```

