import setuptools

install_requires = [
    'python-dotenv',
    'requests',
    'websocket-client',
]

setuptools.setup(
    name='ha_control',
    version='0.1',
    author="jon-alamo",
    author_email="jonrivala@gmail.com",
    description=(""),
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
    install_requires=install_requires
 )
