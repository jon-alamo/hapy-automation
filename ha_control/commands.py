import os
import shutil
import argparse

import dotenv
import ha_control

dotenv.load_dotenv()


def start_project():
    parser = argparse.ArgumentParser(
        description='Start ha_control automation project'
    )
    parser.add_argument(
        '--ha_url', type=str, help='Home Assistant URL', default=None
    )
    parser.add_argument(
        '--ha_token', type=str, help='Home Assistant Token', default=None

    )
    args = parser.parse_args()
    ha_url = args.ha_url or os.getenv('HA_URL')
    ha_token = args.ha_token or os.getenv('HA_TOKEN')

    if not ha_url:
        raise ValueError(
            'ha_url needs to be passed as argument, in .env or as '
            'environment variable'
        )
    if not ha_token:
        raise ValueError(
            'ha_token needs to be passed as argument, in .env or as '
            'environment variable'
        )

    directory = os.getcwd()
    ha_control.generate_modules(directory, ha_url, ha_token)
    templates_dir = os.path.join(ha_control.__path__[0], 'templates')
    for file_path in os.listdir(templates_dir):
        shutil.copy(
            os.path.join(templates_dir, file_path),
            os.path.join(directory, file_path)
        )
