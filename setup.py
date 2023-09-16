from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rtcamp_assignment/__init__.py
from rtcamp_assignment import __version__ as version

setup(
	name="rtcamp_assignment",
	version=version,
	description="Rtcamp Hiring Portal Assignment",
	author="God",
	author_email="4rnguwsj@duck.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
