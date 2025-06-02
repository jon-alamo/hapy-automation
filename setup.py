import setuptools

install_requires = [
    'requests',
    'websocket-client',
    'watchdog',
    'zha-quirks',
    'pydantic-settings',
    'pytz',
    'python-dateutil',
    'gitpython'
]


setuptools.setup(
    name='hapy',
    version='0.4',
    author="jon-alamo",
    author_email="jonrivala@gmail.com",
    description="Home Assistant Python Automation Tool",
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
            'hapy-init = hapy.commands:init_project',
            'hapy-update = hapy.commands:init_project',
            'hapy-run = hapy.commands:run_application'
        ],
    },
)
