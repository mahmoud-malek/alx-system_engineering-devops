0x12. Web Stack Debugging #2
Description
This project focuses on debugging web server issues related to user permissions. We’ll create a Bash script that allows us to run commands as another user and verify the correct permissions.

Requirements
Ubuntu 20.04 LTS
All files should end with a new line.
A README.md file at the root of the project folder is mandatory.
All Bash script files must be executable.
Bash scripts must pass Shellcheck without any error.
Bash scripts must run without error.
The first line of all Bash scripts should be #!/usr/bin/env bash.
The second line of all Bash scripts should be a comment explaining what the script does.
Tasks 0. Run software as another user (mandatory)
Write a Bash script that accepts one argument.
The script should run the whoami command under the user passed as an argument.
Test your script by passing different users.
Example usage:

$ whoami
root
$ ./0-iamsomeoneelse www-data
www-data
$ whoami
root

Repository
GitHub repository: alx-system_engineering-devops
