from setuptools import setup, find_packages

setup(
    name='scrapo',  
    version='0.1.0',  
    description='Scrapo, scrapes.',  
    author='Yakup Cemil Kayabaş',  
    author_email='ycemilkayabas@gmail.com', 
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'nicegui',
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'scrapo=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
