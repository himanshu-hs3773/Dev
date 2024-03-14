Collaboration on Python Projects with PRO
Python312

# Data Engineering

## Linux equivalent Windows
| *Description*                                     | *Linux*                | *Windows*     |
|:--------------------------------------------------|:-----------------------|:--------------|
| Directory listing                                 | ls -l                  | dir           |
| Rename a file                                     | mv                     | ren           |
| Copying a file                                    | cp                     | copy          |
| Moving a file                                     | mv                     | move          |
| Clear Screen                                      | clear                  | cls           |
| Delete file                                       | rm                     | del           |
| Compare contents of files                         | diff                   | fc            |
| Search for a string in a file                     | grep                   | find          |
| Display the manual/help details of the command    | man command            | command /?    |
| Returns your current directory location           | pwd                    | chdir         |
| Displays the time                                 | date                   | time          |
| Environment variables                             | set                    | env           |
| Change the current directory                      | cd                     | cd            |
| To create a new directory/folder                  | mkdir                  | md            |
| To print something on the screen                  | echo                   | echo          |
| To write in to files.                             | vim(depends on editor) | edit          |
| To leave the terminal/command window.             | exit                   | exit          |
| To format a drive/partition.                      | mke2fs or mformat      | format        |
| To display free space.                            | mem                    | free          |
| To delete a directory.                            | rm -rf/rmdir           | rmdir         |
| To kill a task.                                   | kill                   | taskkill      |
| To list running tasks.                            | ps x                   | tasklist      |
| To set environment variables.                     | export var=value       | set var=value |
| To change file permissions.                       | chown/chmod            | attrib        |
| To print the route packets trace to network host. | traceroute             | tracert       |
| daemon to execute scheduled commands.             | cron                   | at            |
| To print contents of a file.                      | cat                    | type          |
| To send ICMP ECHO_REQUEST to network hosts.       | ping                   | ping          |
| To query Internet name servers interactively.     | nslookup               | nslookup      |
| For disk usage.                                   | du -s                  | chdisk        |
| To list directory recursively.                    | ls -R                  | tree          |


## Local setup(Win)
- >py -m venv venv
- >venv\Scripts\activate
- >python.exe -m pip install --upgrade pip
- >pip list

## Local setup(Win)
- >source venv/Scripts/activate

## FastAPI
- [Conda Windows](https://stackoverflow.com/questions/49392719/get-the-anaconda-prompt-running-in-the-pycharm-terminal)
- `uvicorn fastapi_dev.main:app --reload`

## AirFlow
- Airflow+Docker+Windows: [Ref](https://medium.com/@garc1a0scar/how-to-start-with-apache-airflow-in-docker-windows-902674ad1b)

## RabbitMQ
- [Win ref](https://www.rabbitmq.com/install-windows.html)
- ΓÇ£a pure-Python AMQP 0ΓÇô9ΓÇô1 client for rabbitMQΓÇ¥
- choco install rabbitmq | scoop install rabbitmq
- Verify chocolatey
- - >choco /?
- Install chocolatey
- - Run Powershell as admin
- - >Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-
Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

```Creating shim for 'rabbitmqctl'.
Creating shim for 'rabbitmq-defaults'.
Creating shim for 'rabbitmq-diagnostics'.
Creating shim for 'rabbitmq-echopid'.
Creating shim for 'rabbitmq-env'.
Creating shim for 'rabbitmq-plugins'.
Creating shim for 'rabbitmq-queues'.
Creating shim for 'rabbitmq-server'.
Creating shim for 'rabbitmq-service'.
Creating shim for 'rabbitmq-upgrade'.```
"# dev" 


## Redis
https://github.com/redis-developer/redis-datasets/tree/master?tab=readme-ov-file
https://dev.to/redis/top-10-sample-dataset-for-redis-for-you-28l7
https://redis.readthedocs.io/en/stable/examples/connection_examples.html#Connecting-to-a-default-Redis-instance,-running-locally.
