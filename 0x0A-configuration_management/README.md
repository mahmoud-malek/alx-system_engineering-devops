# Configuration Management Project

Welcome to the Configuration Management project as part of your Software Engineering Foundations curriculum! This project is designed to familiarize you with essential concepts in configuration management, leveraging tools like Puppet. Follow the guidelines below to successfully complete the tasks.

## Background Context

The project is inspired by a real-world scenario faced by Sylvain Kalache during his time at SlideShare. Understanding the significance of tools like Puppet becomes apparent when managing and scaling infrastructure efficiently, as highlighted in Sylvain's experience.

## Resources

Make sure to go through the provided resources before starting the tasks. These will help you grasp the fundamental concepts of Configuration Management and Puppet.

- [Intro to Configuration Management](#)
- [Puppet resource type: file](#)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](#)
- [Puppet lint](#)
- [Puppet emacs mode](#)

## Requirements

### General

- All files will be interpreted on Ubuntu 20.04 LTS.
- Files should end with a new line.
- A README.md file at the root is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining their purpose.
- Puppet manifest files must end with the extension .pp.

### Versioning

Ensure your Ubuntu 20.04 VM has Puppet 5.5 preinstalled. Follow the provided commands for installation.

## Tasks

### 0. Create a File

**Objective:** Create a file in /tmp using Puppet.

**Requirements:**
- File path is /tmp/school
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains "I love Puppet"

Refer to the provided example for guidance.

[View Task Details](#)

### 1. Install a Package

**Objective:** Install Flask from pip3 using Puppet.

**Requirements:**
- Install flask
- Version must be 2.1.0

Refer to the provided example for guidance.

[View Task Details](#)

### 2. Execute a Command

**Objective:** Create a manifest that kills a process named killmenow using the exec Puppet resource and pkill.

Refer to the provided example for guidance.


Feel free to ask for clarification or assistance throughout the project. Good luck, and enjoy your journey into Configuration Management! 🚀
