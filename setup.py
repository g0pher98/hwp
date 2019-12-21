from setuptools import setup, find_packages

setup(
	name				= 'hwp',
	version				= '0.0.1',
	description			= 'Python Hangul Word Press Library',
	author				= 'Lee Jae Seung, Lee Hyo Jin, (정예림)',
	author_email		= 'g0pher98@naver.com',
	url					= 'https://github.com/g0pher98/hwp',
	download_url		= 'https://github.com/g0pher98/hwp/archive/(version.tar.gz)',
	install_requires	= [],
	packages			= find_packages(exclude = ['docs', 'tests*']),
	keywords			= ['hwp', 'pyhwp', 'hangul'],
	python_requires		= '>=3',
	package_data		= {},
	zip_safe=False,
	classifiers			= [
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.7'
	]
)