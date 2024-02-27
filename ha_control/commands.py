import os
import argparse
import inspect
import dotenv
import ha_control
import ha_control.templates.application as app_template
import ha_control.templates.automations as automations_template

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

    app_tmpl_source = inspect.getsource(app_template)
    with open('application.py', 'w') as f:
        f.write(app_tmpl_source)
    auto_tmpl_source = inspect.getsource(automations_template)
    with open('automations.py', 'w') as f:
        f.write(auto_tmpl_source)

    directory = os.getcwd()
    ha_control.generate_modules(directory, ha_url, ha_token)

