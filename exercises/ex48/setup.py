try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Alan Fluder',
	'url': 'URL to get to it',
	'download_url': 'Where to download from',
	'author_email': 'afluder1@mix.wvu.edu',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}
setup(**config)
