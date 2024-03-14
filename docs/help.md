Python312

## Local setup(Win)
- >py -m venv venv
- >venv\Scripts\activate
- >python.exe -m pip install --upgrade pip
- >pip list
- >set PYTHONPATH=%PYTHONPATH%;.

## Conda
- Install ([Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html))
- In pycharm Settings > Tools > Terminal, change the Shell path as following:
- "/K" "path to miniconda" "default env"
> cmd.exe "/K" "F:\miniconda3\Scripts\activate.bat" "base"

And the C:\Users\me\Miniconda3 can be replaced by either one of your conda environment name such as base
### Conda basics
- `conda info` ## Verify conda is installed, check version number
- `conda update` conda ## Update conda to the current version
- `conda install PACKAGENAME` ## Install a package included in Anaconda
- `spyder` ## Run a package after install, example Spyder*
- `conda update PACKAGENAME` ## Update any installed program
- `COMMANDNAME --help` 
- `conda install --help`
### Using environments
- `conda create --name py35 python=3.5` ## Create a new environment named py35, install Python 3.5
- `WINDOWS: activate py35 LINUX, macOS: source activate py35` ## Activate the new environment to use it
- `conda env list` ## Get a list of all my environments, active environment is shown with *
- `conda create --clone py35 --name py35-2` ## Make exact copy of an environment
- `conda list ` ## List all packages and versions installed in active environment
- `conda list --revisions` ## List the history of each change to the current environment
- `conda install --revision 2` ## Restore environment to a previous revision
- `conda list --explicit > bio-env.txt` ## Save environment to a text file
- `conda env remove --name bio-env` ## Delete an environment and everything in it
- `WINDOWS: deactivate macOS, LINUX: source deactivate` ## Deactivate the current environment
- `conda env create --file bio-env.txt` ## Create environment from a text file
- `conda create --name bio-env biopython` ## Stack commands: create a new environment, name it bio-env and install the biopython package
### Finding, Installing and updating packages
- `conda search PACKAGENAME`
- https://docs.anaconda.com/anaconda/packages/pkg-docs
- `conda install ` ## Install a new package (Jupyter Notebook)  in the active environment
- `jupyter jupyter-notebook ` ## Run an installed package (Jupyter Notebook)
- `conda install --name bio-env toolz ` ## Install a new package (toolz) in a different environment (bio-env)
- `conda update scikit-learn  ` ## Update a package in the current environment
- `conda install --channel conda-forge boltons  ` ## Install a package (boltons) from a specific channel (conda-forge)
- `pip install boltons ` ## Install a package directly from PyPI into the current active environment using pip
- `conda remove --name bio-env toolz boltons` ## Remove one or more packages (toolz, boltons)  from a specific environment (bio-env)

### Specifying version numbers
- `conda create --name py34 python=3.4 ` ## Install different version of Python in  a new environment named py34
- Windows: `activate py34` Linux, macOS: `source activate py34` ## Switch to the new environment that has  a different version of Python
- `Windows:  where python Linux, macOS: which -a python ` ## Show the locations of all versions of Python that are currently in the path  NOTE: The first version of Python in the list will be executed.
- `python --version` ## Show version information for the current active Python

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
