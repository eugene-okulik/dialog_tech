import subprocess
import sys
import atexit


def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError:
        print("Error: Failed to install dependencies.")
        sys.exit(1)


def uninstall_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError:
        print("Error: Failed to uninstall dependencies.")


install_dependencies()
atexit.register(uninstall_dependencies)
