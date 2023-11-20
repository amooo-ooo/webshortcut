import argparse
import importlib
import subprocess
import sys
import webbrowser

def force_import(package, module=None):
    if module is None:
        module = package
    try:
        return importlib.import_module(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return importlib.import_module(module)

def main():
    parser = argparse.ArgumentParser(description='Add keyboard shortcuts to open URLs.')
    parser.add_argument('--config_file', type=str, help='The path to the configuration file.')
    parser.add_argument('--add_shortcut', type=str, help='The keyboard shortcut keys separated by commas.')
    parser.add_argument('--shortcut_url', type=str, help='The URL to open with the keyboard shortcut.')
    args = parser.parse_args()

    pynput = force_import('pynput')
    keyboard = pynput.keyboard

    shortcuts = {}
    if args.config_file:
        with open(args.config_file, 'r') as f:
            for line in f:
                keys, url = line.strip().split(' ')
                keys = keys.split(',')
                keys = [getattr(keyboard.Key, key) if hasattr(keyboard.Key, key) else keyboard.KeyCode(char=key) for key in keys]
                shortcuts[frozenset(keys)] = url
    if args.add_shortcut and args.shortcut_url:
        keys = args.add_shortcut.split(',')
        keys = [getattr(keyboard.Key, key) if hasattr(keyboard.Key, key) else keyboard.KeyCode(char=key) for key in keys]
        shortcuts[frozenset(keys)] = args.shortcut_url

    current_keys = set()

    def on_press(key):
        current_keys.add(key)
        for combination, url in shortcuts.items():
            if combination.issubset(current_keys):
                webbrowser.open_new_tab(url)

    def on_release(key):
        if key in current_keys:
            current_keys.remove(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
