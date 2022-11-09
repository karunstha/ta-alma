import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='AlmaIndicate',
	version='0.0.1',
	author='Mark Lester A. Bolotaolo, Karun Shrestha',
	description='A small library for computing ALMA indicator for stocks',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/karunstha/ta-alma',
	packages=setuptools.find_packages(),
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.6',
	install_requires=[
		"numpy",
		"pandas",
		"python-dateutil",
		"pytz",
		"six",
		"ta"
	]
)