from setuptools import setup, find_packages

setup(
    name='AutoNFT',
    version='1.0.0',
    description='Robust Tools for NFT Creation and Management',
    author='Your Name',  # Replace 'Your Name' with the actual author's name
    author_email='your.email@example.com',  # Replace with the actual author's email
    url='https://github.com/yourgithub/AutoNFT',  # Replace with the actual URL
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.0.0',
        'web3>=5.17.0',
        'requests>=2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'autonft=autonft.main:main',  # Assuming there is a main function in main.py that serves as an entry point
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Replace 'MIT License' with the actual license type if different
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    keywords='NFT blockchain minting metadata image-generation',
    license='MIT License',  # Replace 'MIT License' with the actual license type if different
)
