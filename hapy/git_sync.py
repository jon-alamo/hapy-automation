import os
import time
import shutil
import subprocess

import git
import hapy.helpers as helpers
import hapy.config as config


logger = helpers.get_logger('git-sync')

LOCAL_PATH = '.'
REPOSITORY = config.settings.repository_url


def setup_ssh():
    ssh_dir = os.path.expanduser("~/.ssh")
    key_name = "hapy-addon-key"
    id_rsa_path = os.path.join(ssh_dir, key_name)
    id_rsa_pub_path = id_rsa_path + ".pub"

    if not os.path.exists(id_rsa_path):
        os.makedirs(ssh_dir, exist_ok=True)
        subprocess.run([
            "ssh-keygen", "-t", "rsa", "-b", "4096", "-f", id_rsa_path,
            "-N", ""
        ])

    subprocess.run(["ssh-agent", "-s"])  # Start the ssh-agent
    # subprocess.run(['eval', '"$(ssh-agent -s)"'])
    time.sleep(3)
    subprocess.run(["ssh-add", id_rsa_path])

    with open(id_rsa_pub_path, "r") as pub_key_file:
        pub_key = pub_key_file.read()
    logger.warning(
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n:::: Add this public key to your GitHub repository's keys:  ::::::"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n\n{pub_key}\n\n"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
    )


def push_repo():
    if not REPOSITORY:
        return False
    repo = git.Repo(LOCAL_PATH)
    repo.git.add(A=True)
    repo.index.commit("[AUTO-PUSH] Hapy Automations File Structure")
    origin = repo.remotes.origin
    origin.push()
    return True


def preserve_files():
    logger.warning(f'Saving files to be restored later ...')
    files = {}
    for name in os.listdir(LOCAL_PATH):
        if not os.path.isdir(name):
            with open(name, 'r') as f:
                files[name] = f.read()
                logger.warning(f'File {name} saved.')
    return files


def restore_files(files):
    logger.warning('Restoring files ...')
    for name, content in files.items():
        with open(name, 'w') as f:
            f.write(content)
            logger.warning(f'File {name} restored.')


def remove_content():
    for item in os.listdir(LOCAL_PATH):
        item_path = os.path.join(LOCAL_PATH, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def pull_repo():
    if not REPOSITORY:
        return False
    try:
        repo = git.Repo(LOCAL_PATH)
        origin = repo.remotes.origin
        origin.pull()
    except git.InvalidGitRepositoryError:
        files = preserve_files()
        try:
            remove_content()
            git.Repo.clone_from(REPOSITORY, LOCAL_PATH)
            restore_files(files)
        except Exception as e:
            restore_files(files)
            raise e

    return True

