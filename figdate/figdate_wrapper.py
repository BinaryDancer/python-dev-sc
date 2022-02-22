import argparse
import shutil
import subprocess
import tempfile
import venv


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Show date using pyfiglet.')
    parser.add_argument('format', nargs='?', type=str, default='%Y %d %b, %A', help='date format.')
    parser.add_argument('font', nargs='?', type=str, default='graceful', help='pyfiglet font style.')
    args = parser.parse_args()

    dir = tempfile.mkdtemp()
    venv.create(dir, clear=True, with_pip=True)

    subprocess.run(["{}/bin/pip".format(dir), 'install', 'pyfiglet'])
    subprocess.run(["{}/bin/python3".format(dir), '-m', 'figdate', args.format, args.font])

    shutil.rmtree(dir)
