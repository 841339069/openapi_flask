# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50

from setuptools import setup, find_packages

from openapi_flask import __version__

long_description = open('README.md', 'r', encoding='utf-8').read()

setup(
    name="openapi-flask",
    version=__version__,
    url='https://github.com/841339069/openapi_flask',
    description='Generate REST API and OpenAPI documentation for your Flask project.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    license_files='LICENSE.rst',
    author='gxw',
    author_email='841339069@qq.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False,
    platforms='any',
    install_requires=["Flask>=1.1", "pydantic>=1.2"],
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha    ',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)
