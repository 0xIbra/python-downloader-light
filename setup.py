import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='downloader-light',
    version='0.0.1',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    maintainer='Ibragim Abubakarov',
    maintainer_email='ibragim.ai95@gmail.com',
    description='Lightweight python package that allows the download of thousands of files concurrently.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ibragim64/python-downloader-light',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'pysftp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: File Transfer Protocol (FTP)"
    ]
)