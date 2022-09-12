from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
	name='periodic-table-info',
	version='0.3.0',
    description='Print all the elements in the Periodic Table of the Elements, with an interactive prompt to learn more.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Education',
    ],
    keywords='periodic table education info cli',
    url='https://github.com/Dog-Face-Development/Periodic-Table-Info',
    author='willtheorangeguy',
    py_modules = ['elements', 'print', 'main'],
    entry_points={
        'console_scripts': [
            'periodic-table-info=elements:element_print_out'
        ]
    },
)
