# WebShortcut

WebShortcut is a simple Python script that allows you to open specific web URLs with keyboard shortcuts. Define your own shortcuts to URLs either through the command line or a configuration file.

## Quick Start
Clone the repository:
```shell
git clone https://github.com/amooo-ooo/webshortcut
```

Run the script:
```shell
python main.py --add_shortcut=<keys> --shortcut_url=<web_url>
```

Here is an example:
```shell
python main.py --add_shortcut=ctrl,shift,alt,g --shortcut_url="www.google.com"
```

This will set up a global hotkey 'Ctrl + Shift + Alt + G' to open Google in your default browser. 

## Examples

Here are some examples of how you can use WebShortcut:

- Set up a single shortcut from the command line:

```shell
python main.py --add_shortcut=ctrl,shift,alt,cmd,l --shortcut_url="www.linkedin.com"
```

- Set up multiple shortcuts from a configuration file:

```shell
python main.py --config_file=shortcuts.txt
```

In this example, `shortcuts.txt` is a file with each line being a space-separated pair of a comma-separated list of keys and a URL. For example:

```
ctrl,shift,alt,cmd,g www.google.com
ctrl,shift,alt,cmd,l www.linkedin.com
```

## Quick Documentation

### Adding Shortcuts

You can add shortcuts in two ways:

1. Command Line: Use the `--add_shortcut` and `--shortcut_url` arguments when running the script. The `--add_shortcut` argument should be a string of keys separated by commas, and the `--shortcut_url` argument should be the URL to open with the keyboard shortcut.

2. Configuration File: Use the `--config_file` argument when running the script. The `--config_file` argument should be the path to a configuration file. Each line in the configuration file should be a space-separated pair of a comma-separated list of keys and a URL.

### Keys

The keys for the shortcuts are based on the `pynput.keyboard.Key` and `pynput.keyboard.KeyCode` classes. Here are some common keys:

- `ctrl`: Control key
- `shift`: Shift key
- `alt`: Alt key
- `cmd`: Command key (Windows key on Windows, command key on Mac)
- `a` to `z`: Letter keys
- `0` to `9`: Number keys

> [!NOTE]
> Please note that the script needs to keep running in the background for the hotkeys to work. You might want to consider turning this into a daemon or a service that starts on boot, depending on your use case and operating system.

## Contact
You can contact me at [amor.budiyanto@gmail.com](mailto:amor.budiyanto@gmail.com).