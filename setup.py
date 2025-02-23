from setuptools import setup, find_packages


setup(
    name = 'brain-plasma',
    version = '0.2',
    description = 'Share python between callbacks in Dash, using Apache Plasma',
    long_description = 'Adds variable naming and unique intra-instance namespaces to the Apache Plasma in-memory object store.',
    keywords = ' dash plasma callbacks plotly apache arrow pandas numpy redis namespace python',
    url = 'https://github.com/russellromney/brain-plasma',
    download_url = 'https://github.com/russellromney/brain-plasma/archive/v0.2.tar.gz',
    author = 'Russell Romney',
    author_email = 'russellromney@gmail.com',
    license = 'MIT',
    packages = find_packages(),
    install_requires = [],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data = False,
    zip_safe = False
)
