from pathlib import Path
from base64 import b64encode
from git import Repo
import subprocess


PATH_TO_REPO = Path(__file__).parent.parent.resolve()


def get_main_setup_checksum():
    repo = Repo(PATH_TO_REPO)

    current_head = repo.head.ref
    main_head = repo.refs.main

    main_head.checkout()
    proc = subprocess.Popen("sha256sum setup.py", stdout=subprocess.PIPE)
    checksum = proc.stdout.read().decode().split(" ")[0]
    checksum = b64encode(bytes.fromhex(checksum)).decode()

    # go back to the original branch
    current_head.checkout()

    return checksum


if __name__ == "__main__":
    get_main_setup_checksum()
