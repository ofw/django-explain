# coding: utf-8

import os
from setuptools import setup, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-explain',
    version='1.1.1',
    py_modules=[
        'django_explain',
    ],
    include_package_data=True,
    install_requires=['Django>=1.7', 'requests', 'sqlparse'],
    license='MIT License',
    description='A helper to get EXPLAIN and EXPLAIN ANALYZE OUTPUT for django queryset.',
    author='Egor Orlov',
    author_email='oeegor@gmail.com',
    platforms='any',
    url='https://github.com/oeegor/django-explain',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    cmdclass={
        'clean': CleanCommand,
    },
)
