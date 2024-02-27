import setuptools

install_requires = [
    'python-dotenv',
    'requests',
    'websocket-client',
    'watchdog',
    'zhaquirks @ git+https://github.com/zigpy/zha-device-handlers.git'
]


setuptools.setup(
    name='ha_control',
    version='0.1',
    author="jon-alamo",
    author_email="jonrivala@gmail.com",
    description=("HA PurePython Automation Package"),
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'ha-startproject = ha_control.commands:start_project',
        ],
    },
)
