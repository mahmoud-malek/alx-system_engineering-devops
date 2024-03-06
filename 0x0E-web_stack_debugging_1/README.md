# alx-system_engineering-devops
## Project: 0x0E-web_stack_debugging_1

### Overview
This project focuses on debugging and fixing issues related to Nginx installation on an Ubuntu container. The tasks involve investigating why Nginx is not listening on port 80 and creating a Bash script to automate the fix.

### Task 0: Nginx likes port 80
**Objective:** Identify and resolve the issue preventing Nginx from listening on port 80. Create a Bash script to configure the server accordingly.

**Instructions:**
- Nginx must be running and listening on port 80 for all active IPv4 IPs.
- Write a Bash script that configures the server as specified.

**Usage:**
```bash
$ curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
$ ./0-nginx_likes_port_80 > /dev/null 2&>1
$ curl 0:80
<!DOCTYPE html>
<html>
<!-- Nginx welcome page content -->
</html>
```

**File:** [0-nginx_likes_port_80](https://github.com/alx-system_engineering-devops/0x0E-web_stack_debugging_1/blob/main/0-nginx_likes_port_80)

### Task 1: Make it sweet and short
**Objective:** Build on the previous task to create a shorter Bash script, keeping it within 5 lines.

**Instructions:**
- The Bash script must be 5 lines or less.
- Usual Bash script requirements apply.
- Do not use `;`, `&&`, or `wget`.
- The `service` (init) must correctly report that Nginx is not running.

**Usage:**
```bash
$ curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
$ ./1-debugging_made_short
$ curl 0:80
<!DOCTYPE html>
<html>
<!-- Nginx welcome page content -->
</html>
$ service nginx status
 * nginx is not running
```

**File:** [1-debugging_made_short](https://github.com/alx-system_engineering-devops/0x0E-web_stack_debugging_1/blob/main/1-debugging_made_short)

