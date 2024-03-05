from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quantbit_process_manufacturing/__init__.py
from quantbit_process_manufacturing import __version__ as version

setup(
	name="quantbit_process_manufacturing",
	version=version,
	description="This is app content manufacturing process",
	author="abhishek shinde",
	author_email="abhishek.shinde@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
