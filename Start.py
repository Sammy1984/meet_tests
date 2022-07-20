import argparse
import platform
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--bc", default=1)
parser.add_argument("--mc", default=1)
parser.add_argument("--mlf", default=1)
parser.add_argument("--mlt", default=1)
parser.add_argument("--mtm", default=1)
parser.add_argument("--rid", default=1)
args = parser.parse_known_args()


def set_args():
    with open('Constants.py', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(old_data,
                                f'''
ROOMID = '{args[0].rid}'
BOTS_COUNT = {args[0].bc}
MESSAGE_COUNT = {args[0].mc}
MESSAGE_LENGTH_TO = {args[0].mlt}
MESSAGE_LENGTH_FROM = {args[0].mlf}
MESSAGE_TIMING = {args[0].mtm}
REF_URL = None''')

    with open('Constants.py', 'w') as f:
        f.write(new_data)


script_file = "run_tests.py"

if platform.system() == "Windows":
    python_bin = r"venv\Scripts\python"
elif platform.system() == "Linux":
    python_bin = r"venv/bin/python"


if __name__ == "__main__":
    set_args()
    subprocess.Popen([python_bin, script_file])
