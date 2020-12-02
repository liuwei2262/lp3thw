try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My progect',
    'author':'daikai',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'daikai@acca.com.cn.',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'progectname'
}

setup(**config)

