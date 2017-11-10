from setuptools import setup

setup(
  name = 'pycake',
  packages = ['pycake'],
  version = '1.10.0',
  description = 'Python SDK for CAKE API',
  long_description = open('README.rst').read(),
  author = 'Timothy Johnson',
  author_email = 'tim@getcake.com',
  license = 'MIT',
  url = 'https://github.com/heytimj/pycake', 
  download_url = 'https://github.com/heytimj/pycake/archive/1.10.0.tar.gz', 
  keywords = ['cake', 'api', 'sdk'],
  classifiers = [],
  install_requires = [
    'requests',
  ],
  data_files = [('', ['LICENSE.txt'])]
)
