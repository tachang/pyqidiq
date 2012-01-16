from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyqidiq', 
    version='0.1.0',
    description='A qidiq library in python',
    long_description=read('README'),
    author='Jeff Tchang',
    url='http://www.qidiq.com',
    author_email='jeff.tchang@gmail.com',
    packages=find_packages(),
    namespace_packages=['pyqidiq'],
    install_requires=['setuptools'],
    license='BSD',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
    keywords = 'qidiq api'
)
