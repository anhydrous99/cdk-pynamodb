from setuptools import setup, find_packages
setup(
    name='CDK PynamoDB',
    version='0.1.1',
    packages=find_packages(include=['cdk_pynamodb', 'cdk_pynamodb.*'])
)