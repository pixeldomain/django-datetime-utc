from setuptools import setup
from os.path import join
from os.path import dirname


version = __import__('datetimeutc').__version__

LONG_DESCRIPTION = """
django-datetime-utc provides DateTimeUTCField, a naive datetime model field.
In PostgreSQL this translates to the field 'timestamp without time zone'."""

def long_description():
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name="django-datetime-utc",
    version=version,
    description="Django UTC datetime model field - timestamp without time zone",
    long_description=long_description(),
    url='https://github.com/pixeldomain/django-datetime-utc',
    author='Darren O\'Neill',
    author_email='darren@pixeldomain.co.uk',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='django, timestamp without time zone, utc, datetime',
    packages=['datetimeutc'],
    install_requires = ['Django>=1.5.0', 'python-dateutil'],
)
