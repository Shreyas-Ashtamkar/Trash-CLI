from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
	name='trash-it',
	version='0.1.0',
	license='MIT',
	
	description='A Python Built Package for Sendign Files to Trash.',
	long_description=long_description,
    long_description_content_type="text/markdown",
    
    author="Shreyas Ashtamkar",
    author_email="shreyu@programmer.net",
    url="https://github.com/Shreyas-Ashtamkar/Trash-CLI",

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Posix :: Linux",
    ],

	python_requires='>=3.6',
    install_requires=requirements,

    packages=find_packages(),
    entry_points={
		'console_scripts': ['trash=trashit.command_line:main'],
  	},

  	include_package_data=True,
  	zip_safe=False
)