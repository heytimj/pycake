from setuptools import setup, find_packages

setup(
  name = 'pycake',
  packages = find_packages(),
  include_package_date=True,
  version = '2.0.3',
  description = 'Python SDK for CAKE API',
  long_description = open('README.rst').read(),
  author = 'Timothy Johnson',
  author_email = 'tim@getcake.com',
  license = 'MIT',
  url = 'https://github.com/heytimj/pycake', 
  download_url = 'https://github.com/heytimj/pycake/archive/2.0.3.tar.gz', 
  keywords = ['cake', 'api', 'sdk'],
  classifiers = [],
  install_requires = [
    'requests',
  ],
  data_files = [('', ['LICENSE.txt'])]
)
