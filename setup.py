import setuptools

install_requires = [
    'requests==2.34.2',
    'websocket-client==1.9.0',
    'watchdog==6.0.0',
    'zha-quirks==2.2.0',
    'zigpy==2.1.0',
    'pydantic-settings==2.14.2',
    'pytz==2026.3.post1',
    'python-dateutil==2.9.0.post0',
    'gitpython==3.1.58'
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
