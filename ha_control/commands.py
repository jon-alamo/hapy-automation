import os
import argparse
import inspect
import dotenv
import ha_control
import ha_control.templates.application as app_template
import ha_control.templates.automations as automations_template
import ha_control.config as config

dotenv.load_dotenv()


def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def create_application_template(directory, app_tmpl_source):
    if not os.path.exists(os.path.join(directory, 'application.py')):
        with open(os.path.join(directory, 'application.py'), 'w') as f:
            f.write(app_tmpl_source)


def create_automations_template(directory, auto_tmpl_source):
    if os.path.exists(os.path.join(directory, 'automations.py')):
        return
    if os.path.exists(os.path.join(directory, 'automations')):
        return
    with open(os.path.join(directory, 'automations.py'), 'w') as f:
        f.write(auto_tmpl_source)


def create_update_project(directory):
    ha_url = config.settings.ha_url
    ha_token = config.settings.ha_token

    if not ha_url:
        raise ValueError('HA_URL needs to be defined in .env file.')
    if not ha_token:
        raise ValueError('HA_TOKEN needs to be defined in .env file.')
    ensure_directory(directory)
    app_tmpl_source = inspect.getsource(app_template)
    create_application_template(directory, app_tmpl_source)
    auto_tmpl_source = inspect.getsource(automations_template)
    create_automations_template(directory, auto_tmpl_source)
    ha_control.generate_modules(directory, ha_url, ha_token)


def start_project():
    parser = argparse.ArgumentParser(
        description='Start a new Home Assistant project.'
    )
    parser.add_argument(
        '--directory',
        type=str,
        help='Directory to create the project in.',
        default='.'
    )
    args = parser.parse_args()
    create_update_project(args.directory)
