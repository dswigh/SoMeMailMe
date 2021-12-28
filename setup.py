from setuptools import find_packages, setup
setup(
    name='SoMeMailMe',
    packages=find_packages(include=['SoMeMailMe']),
    version='0.1.0',
    description='Send yourself an email with your TikTok and IG follower count',
    author='Daniel Wigh',
    license='MIT',
    install_requires=['scraper', 'datetime', 'pandas'],
    setup_requires=[]
)
