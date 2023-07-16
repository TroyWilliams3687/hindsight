# Support

This folder contains the scripts that can be used to build/rebuild the virtual environment. It contains a shell script and a PowerShell script. Both of these will work in a similar way on Linux and Windows to properly setup the virtual environment and to install the requirements.

The purpose of these scripts are to work with a Python git repository to build the virtual environment and install the required modules in a consistent cross-platform manor. You will have to use the shell script on Linux and the PowerShell script on Windows. However, every attempt is made to make the experience as consistent as possible between the platforms so you can focus on the Python development.

The scripts, along with this README, are located in a folder called `support`. This folder can be renamed to suit the repository it is working with.

## Ubuntu/Linux

### Files

- `build_venv.sh`
    - Build or Rebuild the virtual environment
    - Must be executed in the same folder where the virtual environment will be installed
    - Install all of the `*requirements.txt` files
    - Uses the `path.ini` file to launch the correct Python binary

- `sample.path.ini`
    - This is a sample file that will be included with the repository
    - The idea is to make a copy of this file, renaming it to `path.ini` on each computer and assign the correct paths
    - This file will be part of the repository and live in the same folder as `build_venv.sh`

- `path.ini`
    - This file will be custom to each computer and live in the same folder as `build_venv.sh`
    - This fill will *NOT* be included with the repository

- `.gitignore`
    - This file will instruct git to ignore certain files that shouldn't be included with the repo
    - This file will be in the same folder as `build_venv.sh`

### Aliases

Aliases make things easier to work with on Linux. All you have to do is modify the `~/.bashrc`.

>NOTE: You can add other aliases as you see fit that augment your workflow.

#### `activate`

This will activate the virtual environment so you can use the tools and code installed within it.

Edit `~/.bashrc` and add the following lines:

```text
# Python Virtual Environment Alias
alias activate="source .venv/bin/activate"
```

#### `launchj`

Add an alias to launch the jupyter notebooks server. This won't require activating the virtual environment, but will require the command to be lunched from the root of the repo.

Edit `~/.bashrc` and add the following lines:

```text
# Launch Jupyter Notebooks
alias launchj=".venv/bin/jupyter notebook --notebook-dir=."
```

>NOTE: This doesn't require a call to the `activate` command first. It will work by itself.

## Windows

### Files

- `build_venv.ps1`
    - Build or Rebuild the virtual environment
    - Must be executed in the same folder where the virtual environment will be installed
    - Install all of the `*requirements.txt` files
    - Uses the `path.ini` file to launch the correct Python binary

- `sample.path.ini`
    - This is a sample file that will be included with the repository
    - The idea is to make a copy of this file, renaming it to `path.ini` on each computer and assign the correct paths
    - This file will be part of the repository and live in the same folder as `build_venv.ps1`

- `path.ini`
    - This file will be custom to each computer and live in the same folder as `build_venv.ps1`
    - This fill will *NOT* be included with the repository

- `.gitignore`
    - This file will instruct git to ignore certain files that shouldn't be included with the repo
    - This file will be in the same folder as `build_venv.ps1`

### Aliases

Adding aliases to PowerShell will produce similar results to Linux, making things easier to work with in the terminal.

Within the PowerShell terminal use `notepad $profile` to open the correct file to edit in notepad.

Reference: https://superuser.com/questions/886951/run-powershell-script-when-you-open-powershell


#### `activate`

```powershell
oh-my-posh init pwsh | Invoke-Expression
Set-alias activate .venv/Scripts/activate
```

#### `launchj`

```powershell
function launchj()
{
    .venv/Scripts/jupyter notebook --notebook-dir=.
}
```

>NOTE: Aliases in PowerShell do not support arguments.  You have to make a function to handle those cases. This link can provide an good example: https://seankilleen.com/2020/04/how-to-create-a-powershell-alias-with-parameters/

### PowerShell

We want to make sure we are working with PowerShell 7 and not Windows PowerShell (there is a difference).

Reference:

- https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows
- https://learn.microsoft.com/en-us/windows/terminal/tutorials/custom-prompt-setup

- https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal
    - good stuff on getting oh-my-posh working

```bash
winget install --id Microsoft.Powershell --source winget
```

Upgrade:

```bash
winget upgrade PowerShell
```

>NOTE: Could probably use `scoop` to install oh my posh and posh git.