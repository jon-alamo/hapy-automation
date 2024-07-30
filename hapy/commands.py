import os
import argparse
import inspect
import dotenv
import hapy
# import hapy.templates.application as app_template
# import hapy.templates.automations as automations_template
import hapy.config as config

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


def generate_side_files(directory):
    env_file = os.path.join(directory, '.env')
    if not os.path.exists(env_file):
        with open(env_file, 'w') as f:
            f.write(f'HA_API_URL={config.settings.ha_api_url}\n')
            f.write(f'HA_WS_URL={config.settings.ha_ws_url}\n')
            f.write(f'HA_TOKEN={config.settings.ha_token}')
            f.write(f'LOG_LEVEL={config.settings.log_level}\n')
    gitignore_file = os.path.join(directory, '.gitignore')
    if not os.path.exists(gitignore_file):
        with open(gitignore_file, 'w') as f:
            f.write((
                '.vscode\n__pycache__\n.idea\n*.pyc\n*.pyo\n*.pyd\nvenv\n'
                '*.dist-info\n*.dist\n*.egg-info'
            ))


def create_update_project(directory):
    ha_api_url = config.settings.ha_api_url
    ha_ws_url = config.settings.ha_ws_url
    ha_token = config.settings.ha_token

    if not ha_api_url:
        raise ValueError('HA_URL needs to be defined in .env file.')
    if not ha_token:
        raise ValueError('HA_TOKEN needs to be defined in .env file.')
    ensure_directory(directory)
    generate_side_files(directory)

    app_tmp_path = os.path.join(os.path.dirname(__file__), 'templates', 'application.py')
    with open(app_tmp_path, 'r') as f:
        app_tmpl_source = f.read()
    # app_tmpl_source = inspect.getsource(app_template)
    create_application_template(directory, app_tmpl_source)
    auto_tmp_path = os.path.join(os.path.dirname(__file__), 'templates', 'automations.py')
    with open(auto_tmp_path, 'r') as f:
        auto_tmpl_source = f.read()
    # auto_tmpl_source = inspect.getsource(automations_template)
    create_automations_template(directory, auto_tmpl_source)
    hapy.generate_modules(directory, ha_api_url, ha_ws_url, ha_token)


def init_project():
    parser = argparse.ArgumentParser(
        description='Init a new Home Assistant project.'
    )
    parser.add_argument(
        '--directory',
        type=str,
        help='Directory to create the project in.',
        default='.'
    )
    args = parser.parse_args()
    create_update_project(args.directory)


def run_application():
    hapy.init_project()
    ha_api_url = config.settings.ha_api_url
    ha_ws_url = config.settings.ha_ws_url
    ha_token = config.settings.ha_token
    registry = hapy.get_registry()

    import automations
    app = hapy.Application(
        automations_module=automations,
        ha_api_url=ha_api_url,
        ha_ws_url=ha_ws_url,
        ha_token=ha_token,
        registry=registry
    )
    app.run_forever()
