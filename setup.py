from setuptools import setup
import pathlib


version = __import__('datetimeutc').__version__

LONG_DESCRIPTION = """
django-datetime-utc provides DateTimeUTCField, a naive datetime model field.
In PostgreSQL this translates to the field 'timestamp without time zone'."""


def long_description():
    try:
        return pathlib.Path('README.rst').read_text(encoding='utf-8')
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='django-datetime-utc',
    version=version,
    description='Django UTC datetime field - timestamp without time zone',
    long_description=long_description(),
    url='https://github.com/pixeldomain/django-datetime-utc',
    author='Darren O\'Neill',
    author_email='darren@pixeldomain.co.uk',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='django, timestamp without time zone, utc, datetime',
    packages=['datetimeutc'],
    install_requires=['Django>=1.5.0', 'python-dateutil'],
)
