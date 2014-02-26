from distutils.core import setup
import os


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]


setup(
    name='django-onetomany',
    version='0.0.1',
    author='Adi Sieker',
    author_email='adi@sieker.io',
    packages=['onetomany',],
    url='http://github.com/adsworth/django-onetomany/',
    platforms=['OS Independent'],
    license='LICENSE.txt',
    classifiers=CLASSIFIERS,
    description='A django relation field.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    install_requires=[
        "Django >= 1.5",
    ],
)
