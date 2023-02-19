from setuptools import find_packages, setup

setup(
    name='netbox-users',
    version='0.0.1',
    description='Netbox Users',
    long_description='NetBox User Management',
    url='https://github.com/Onemind-Services-LLC/netbox-users/',
    author='Abhimanyu Saharan',
    author_email='asaharan@onemindservices.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    zip_safe=False,
)
