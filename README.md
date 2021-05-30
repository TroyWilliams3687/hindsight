# Hindsight

A tool that can record the position and size of windows on Ubuntu and restore those positions at a later time.

## Problem

The problem, in Ubuntu 20.04 (at least), Gnome has trouble handling the window positions when you have multiple monitors each setup with different resolutions. It is particularly pronounced when locking the system. If one monitor wakes up faster than the other monitor(s) the system assumes it is gone and proceeds to place all the windows onto one monitor or in a random mess. For example, you could have one monitor set at 1920 x 1080 and another at 3840 x 2160 (4k). I have found this can be quite annoying when you have dozens of windows open across multiple virtual desktops!

The idea is to launch a script ([monitor_lock.sh](monitor_lock.sh)) when you login that will monitor the (using dbus-monitor) the system for the lock event. When the lock event is detected, the script calls `hindsight` and records the positions and sizes of the windows. When the script detects the unlock event, it calls `hindsight` and restores the window sizes and positions.

>NOTE: If you don't want to run the script automatically, you can call it manually before the lock event and then restore manually. You could assign the call to a shortcut key pair.

>NOTE: It isn't a 100% accurate. For most windows it should work fine, but you may have to tweak some windows to work better. You will most likely need to configure things for your system. If you have more than two monitors, you will need to make some edits to the [restore.py](./hindsight/restore.py) script.

>NOTE: Sometimes the script may not restore to the correct virtual desktop (monitor loaded slower than usual or I was too quick entering a password). You'll have to manually invoke the call to `hindsight restore`.

## Versions and Requirements

- Ubuntu v20.04
- Python v3.9
- wmctrl - `sudo apt install wmctrl`

You will need Python installed (the latest will probably work fine, but you need at a minimum v3.9). You will also need a tool called [wmctrl](https://www.freedesktop.org/wiki/Software/wmctrl/).


## Installation

Install [wmctrl](https://www.freedesktop.org/wiki/Software/wmctrl/):

```
$ sudo apt install wmctrl
```

Create a folder to store the repository and clone the hindsight repo:

```
$ mkdir ~/repositories/third_party

$ cd ~/repositories/third_party

$ git clone https://github.com/TroyWilliams3687/hindsight.git
```

Create the virtual environment:

```
$ make
```

Activate the virtual environment:

```
$ . .venv/bin/activate
```

## Usage

To record and save the window positions and sizes directly (make sure the virtual environment is active):

```
$ hindsight save
```

To restore the window sizes and positions:

```
$ hindsight restore
```

>NOTE: It only works with windows that are active in the system. If a window doesn't exist when restore is called it will be ignored.

>NOTE: This is a session based system. If you open a window, record its position and then close it. if you open it again, the saved position will not apply to it as it will have a new session based id.

## Storage Location

The window settings are stored here in a JSON file:

```
~/.config/bluebill.net/hindsight/locations.json
```

You can delete that file anytime you like, it will be re-created automatically. It is automatically overwritten each time settings are saved.

## Startup Script

You can use the startup script, [monitor_lock.sh](monitor_lock.sh), to launch a dbus monitor to watch for the lock/unlock events and automatically apply the scripts. If the startup script doesn't quite work, you can always bind to shortcut keys and save the configuration that way.

## Customizations

### monitor_lock.sh

Most likely you will need to modify the path to the repository so that it can save/restore the window positions. You will need to change the path for the following line:

```
EXE=~/repositories/projects/hindsight/.venv/bin/hindsight
```

### Hindsight Restore

The restore script was designed to handle two monitors at specific resolutions. Your mileage may vary. Most likely you will need to modify sections in the restore script, [restore.py](./hindsight/restore.py). The lines you are interested in are from 66 to 114. 

>NOTE: I couldn't figure out a better way to do this with the wmctrl tool. If you run `wmtrcl -lG` and observer the x,y,w,h it reports and use those exact same values in `wmctrl -ir xxxxxx, -e 0,x,y,w,h` the window will move quite a bit (at least it did on my system). It moved a lot more than the window decorations would indicate. And some windows moved more than others, there didn't appear to be a pattern. In the future if I can get it sorted I'll post revisions.

### `.bashrc` alias

I find it useful to have bash aliases setup to initiate that save/restore. In some cases, I have found that the monitor didn't wake up fast enough and the windows were not correctly positioned. In those cases, simpling executing `hsr` did the trick.

```
alias hsr="~/repositories/projects/hindsight/.venv/bin/hindsight restore"
alias hss="~/repositories/projects/hindsight/.venv/bin/hindsight save"
```

>NOTE: Set the path the aliases are refering to based on the location you have created the virtual environment.


## License

[MIT](https://choosealicense.com/licenses/mit/)