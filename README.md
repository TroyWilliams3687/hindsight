# Hindsight

A tool that can record the position and size of windows on Ubuntu and restore those positions at a later time.

## Problem

The problem, in Ubuntu 20.04 (at least), Gnome has trouble handling the window positions when you have multiple monitors each setup with different resolutions. It is particularly pronounced when locking the system. If one monitor wakes up faster than the other monitor(s) the system assumes it is gone and proceeds to place all the windows onto one monitor or in a random mess. For example, you could have one monitor set at 1920 x 1080 and another at 3840 x 2160 (4k). I have found this can be quite annoying when you have dozens of windows open across multiple virtual desktops!

The idea is to launch a script ([monitor_lock.sh](monitor_lock.sh)) when you login that will monitor (using dbus-monitor) the system for a lock event. When the lock event is detected, the script calls `hindsight` and records the positions and sizes of the windows. When the script detects the unlock event, it calls `hindsight` and restores the window sizes and positions.

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

```bash
$ sudo apt install wmctrl
```

You can simply install the package from [pypi](https://pypi.org/project/hindsight-ubuntu/):

```bash
$ pip install hindsight-ubuntu
```

Or you can install it from the git [repo](https://github.com/TroyWilliams3687/hindsight):

```bash
$ mkdir -p ~/repositories/hindsight

$ cd ~/repositories/hindsight

$ git clone https://github.com/TroyWilliams3687/hindsight.git
```

Create the virtual environment:

```bash
$ make
```

Activate the virtual environment:

```bash
$ make shell
```

Or

```bash
$ . .venv/bin/activate
```

## Configuration File

A configuration file is located in the [sample](sample/settings.toml) folder. It
can be placed in `~/.config/bluebill.net/hindsight/settings.toml`. This will
will be used for fine tuning the window placement. It is structured as below:

```toml

# Hindsight
# ---------
#
# https://github.com/TroyWilliams3687/hindsight

# The configuration file allows you to customize Hindsight for your system. It
# allows you to set the scale and specific positions for specific windows that
# don't seem to follow the rules.

# Location - ~/.config/bluebill.net/hindsight/settings.toml

# ---------
# Scale

# Adjust the scale ratio if you have monitors at different resolution. Find the
# min and max values for the width and height and divide them to get a proper
# aspect ratio. For example, I have two monitors with the following resolutions:

#         w  x h
# m1 = [1920, 1080]
# m2 = [3840, 2160]

# scale_x = m1[0] / m2[0] = 0.5
# scale_y = m1[1] / m2[1] = 0.5

scale_x = 0.5 # Default 1.0
scale_y = 0.5 # Default 1.0

# ---------
# Window Fine Tuning

# Some windows will simply not play nice with the system. You can specify part
# of the text that is in the window title (that is how the system knows which
# window to use). You also can specify the x and y position of the upper left
# corner of the window. If one coordinate does not require an adjustment, set it
# to 0.

# NOTE: Default is empty

# NOTE: The text is case-sensitive

# https://toml.io/en/v1.0.0#array-of-tables

[[window_adjustments]]
title_text = "Firefox"
x = -7
y = -8

[[window_adjustments]]
title_text = "Discord"
x = -10
y = 0

```

## Usage

To record and save the window positions and sizes directly (make sure the virtual environment is active):

```bash
$ hindsight save
```

To restore the window sizes and positions:

```bash
$ hindsight restore
```

>NOTE: It only works with windows that are active in the system. If a window doesn't exist when restore is called it will be ignored.

>NOTE: This is a session based system. If you open a window, record its position and then close it. if you open it again, the saved position will not apply to it as it will have a new session based id.

## Storage Location

The window settings are stored here in a JSON file:

```bash
~/.config/bluebill.net/hindsight/locations.json
```

You can delete that file anytime you like, it will be re-created automatically. It is automatically overwritten each time settings are saved.

## Startup Script

You can use the startup script, [monitor_lock.sh](monitor_lock.sh), to launch a dbus monitor to watch for the lock/unlock events and automatically apply the scripts. If the startup script doesn't quite work, you can always bind to shortcut keys and save the configuration that way.

## Customization

### monitor_lock.sh

Most likely you will need to modify the path to the repository so that it can save/restore the window positions. You will need to change the path for the following line:

```bash
EXE=~/repositories/projects/hindsight/.venv/bin/hindsight
```

>NOTE: You add the script to the startup applications so that it is launched when you first log in to the system and continues to run till you log out.

### Hindsight Restore

The restore script was designed to handle two monitors at specific resolutions. Your mileage may vary. Most likely you will need to modify sections in the restore script, [restore.py](./hindsight/restore.py). The lines you are interested in are from 66 to 114.

>UPDATE: The above statement is no longer valid. There is a configuration file that you can use to fine tune the restore positions for specific classes of windows.

>NOTE: I couldn't figure out a better way to do this with the wmctrl tool. If you run `wmtrcl -lG` and observer the x,y,w,h it reports and use those exact same values in `wmctrl -ir xxxxxx, -e 0,x,y,w,h` the window will move quite a bit (at least it did on my system). It moved a lot more than the window decorations would indicate. And some windows moved more than others, there didn't appear to be a pattern. In the future if I can get it sorted I'll post revisions.

### `.bashrc` alias

I find it useful to have bash aliases setup to initiate that save/restore. In some cases, I have found that the monitor didn't wake up fast enough and the windows were not correctly positioned. In those cases, simply executing `hsr` did the trick.

```bash
alias hsr="~/repositories/projects/hindsight/.venv/bin/hindsight restore"
alias hss="~/repositories/projects/hindsight/.venv/bin/hindsight save"
```

>NOTE: Set the path the aliases are referring to based on the location you have created the virtual environment.

### Build/Rebuild Virtual Environment

In Linux us the shell script to create or rebuild the virtual environment:

```bash
./support/build_venv.sh
```

>NOTE: If you run the script again, it will delete the contents of the virtual environment and install everything again.

>NOTE: If you need to remove the virtual environment, simply delete the folder recursively.

You will need to have `./support/path.ini` defined. You can do that by making a copy of `./support/sample.path.ini`:

```bash
cp ./support/sample.path.ini ./support/path.ini
```

You will also need to add the path to the Python binary within the file:

```text
PYTHON="/home/troy/opt/python_3.11.4/bin/python3.11"
```

>NOTE: The path to the binary needs to be contained within double quotes as per the example `sample.path.ini`

>NOTE The support folder can be renamed to somethign more suitable depending on the project. See `./support/README.md` for more details.

## License

[MIT](https://choosealicense.com/licenses/mit/)