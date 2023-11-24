# DevOps Project: Managing Processes and Signals with Bash

This repository contains scripts and solutions for tasks related to managing processes, PIDs, and signals in Linux environments using Bash scripting.

## Table of Contents

- [Introduction](#introduction)
- [Tasks Overview](#tasks-overview)
- [Scripts Overview](#scripts-overview)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Introduction

This project includes a set of Bash scripts designed to perform various tasks related to process management, PID retrieval, and signal handling in a Linux environment. Each script addresses a specific objective outlined in the project guidelines.

## Tasks Overview

Below is a brief overview of the tasks included in this project:
1. Task 0: What is my PID
2. Task 1: List your processes
3. Task 2: Show your Bash PID
4. Task 3: Show your Bash PID made easy
5. Task 4: To infinity and beyond
6. Task 5: Don't stop me now!
7. Task 6: Stop me if you can
8. Task 7: Highlander
9. Task 8: Beheaded process

## Scripts Overview

- `0-what-is-my-pid`: Script to display its own PID.
- `1-list_your_processes`: Script to display a list of currently running processes.
- `2-show_your_bash_pid`: Script to display lines containing the word "bash" to retrieve the Bash process PID.
- `3-show_your_bash_pid_made_easy`: Script to display PIDs of processes containing the word "bash".
- `4-to_infinity_and_beyond`: Script to display "To infinity and beyond" indefinitely.
- `5-dont_stop_me_now`: Script to stop the "To infinity and beyond" process.
- `6-stop_me_if_you_can`: Script to stop the "To infinity and beyond" process without using kill.
- `7-highlander`: Script to display a message indefinitely and handle SIGTERM signal.
- `8-beheaded_process`: Script to kill the process created by `7-highlander`.

## Usage

To use these scripts, clone the repository and navigate to the relevant directory. Make sure to follow the guidelines mentioned in each script's description in the project specifications.

Example:

```bash
./0-what-is-my-pid
```

## Requirements

- Bash environment
- Ubuntu 20.04 LTS
- Shellcheck version 0.7.0 or higher

## License

This project is licensed under the [MIT License](LICENSE).
