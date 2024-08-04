import os
import shutil
import subprocess
import threading

import git
import hapy.helpers as helpers
import hapy.config as config


logger = helpers.get_logger('git-sync')

LOCAL_PATH = '.'
REPOSITORY = config.settings.repository_url


def print_ssh_key(key):
    logger.warning(
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n:::: Add this public key to your GitHub repository's keys:  ::::::"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n\n{key}\n\n"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
    )


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
    os.chmod(id_rsa_path, 0o600)
    setup_ssh_config()

    ssh_agent_output = subprocess.check_output("ssh-agent -s", shell=True, text=True)
    # Parse the SSH agent output to set the environment variables
    for line in ssh_agent_output.splitlines():
        if line.startswith("SSH_AUTH_SOCK"):
            ssh_auth_sock = line.split(";")[0].split("=")[1]
            os.environ["SSH_AUTH_SOCK"] = ssh_auth_sock
        elif line.startswith("SSH_AGENT_PID"):
            ssh_agent_pid = line.split(";")[0].split("=")[1]
            os.environ["SSH_AGENT_PID"] = ssh_agent_pid

    subprocess.run(["ssh-add", id_rsa_path], check=True, text=True)

    with open(id_rsa_pub_path, "r") as pub_key_file:
        pub_key = pub_key_file.read()
        print_ssh_key(pub_key)


def setup_ssh_config():
    ssh_config = os.path.expanduser("~/.ssh/config")
    config_lines = [
        "Host github.com",
        "    StrictHostKeyChecking no",
        "    UserKnownHostsFile=/dev/null"
    ]

    # Ensure the .ssh directory exists
    os.makedirs(os.path.dirname(ssh_config), exist_ok=True)

    # Read existing config if it exists
    if os.path.exists(ssh_config):
        with open(ssh_config, "r") as config_file:
            existing_config = config_file.read()
    else:
        existing_config = ""

    # Check if the necessary config is already present
    if not all(line in existing_config for line in config_lines):
        with open(ssh_config, "a") as config_file:
            config_file.write("\n")
            config_file.write("\n".join(config_lines))
            config_file.write("\n")


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


def add_safe_directory(directory):
    try:
        abs_dir = os.path.abspath(directory)
        # Initialize the Git object
        git_cmd = git.Git()

        # Execute the git config command to add a safe directory
        git_cmd.execute(
            ['git', 'config', '--global', '--add', 'safe.directory', abs_dir]
        )
        print(f"Successfully added {abs_dir} as a safe directory.")
    except git.exc.GitCommandError as e:
        print(f"An error occurred while adding the safe directory: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def pull_repo():
    if not REPOSITORY:
        return False
    try:
        add_safe_directory(LOCAL_PATH)
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


def async_git_pull():
    thread = threading.Thread(target=pull_repo)
    thread.start()
    return thread
