# SCONS

[SCONS](https://scons.org/) - SCons is an Open Source software construction tool. Think of SCons as an improved, cross-platform substitute for the classic Make utility with integrated functionality similar to autoconf/automake and compiler caches such as ccache. In short, SCons is an easier, more reliable and faster way to build software.

We aren't going to be building software with scons, the possible exception will be python packages. We'll use it to construct the virtual environments and install the required packages. Basically a generic way to get up and running quickly.

The SCONS [documentation](https://scons.org/doc/production/HTML/scons-user.html) contains the vital information.

## Installation

```bash
python -m pip install scons
```

>NOTE: Install SCONS in the current python installation that is on your path. That way it is accessible on your system.

## Configuration

There are the following example `SConstruct` files:

- `SConstruct.basic`
- `SConstruct.jupyter` - includes the commands to launch jupyter and ensure that the extensions are configured correctly when the virtual environment is created.

Rename the appropriate one to simple `SConstruct` and place it at the root of the project folder.

>NOTE: `SConstruct.jupyter` is virtually identical to `SConstruct.basic`. It only adds the jupyter related commands

## Basic Commands

The following is the basic to get a virtual environment up and running. This will be the most common command to run:

```bash
scons
```

The second most common, will be the remove command. It will delete the venv and clean out the other support files that are not required (caches, bytecode, etc.):

```bash
scons remove
```


Create a virtual environment and nothing else:

```bash
scons venv
```

Install the packages into the virtual environment (force an upgrade and force a reinstallation):
```bash
scons packages
```

Clean the bytecode files and caches:

```bash
scons clean
```


Run all unit tests:

```bash
scons test
```

Apply the various code formatters:

```bash
scons format
```

Apply various linters to the code:

```bash
scons lint
```

Launch the jupyter notebook environment:

```bash
scons jupyter
```

Apply the jupyter notebook extensions:

```bash
scons jupyter_extensions
```

## Help

```bash
scons -h
```

## Packages

If the project you are working with is a python package there is a line to install the package into the virtual environment and maintain it as editable. This is handy. But if you are not working on a package, the line should be commented out.

## .gitignore

Add the following items to the `.gitignore` file so they are not included in the repo:

```text
.sconsign.dblite
.sconstruct.ini
```

## Setting up a Terminal in Windows

If you are on a Linux box, you don't need to worry about it. It'll work out of the box. If you are on windows, see this [article](https://www.bluebill.net/windows_terminal_and_cmder.html) to setup windows terminal and `make` support.