Practice creating Packages

Steps:
- Create 'script'.py, put in src folder inside project directory
- Create setup.py in project dir.
- run command: python 'script'.py bdist_wheel (Create package from script.py using setup.py as config)
- run command: pip install -e .   (Install package in current directory)
- test script: from 'script' import 'funcname' ... call function
- Choose a license https://choosealicense.com/ and create LICENSE.txt file
- Add classifiers to setup.py file https://pypi.org/classifiers/
- Add a README.md describing project, how to install, usage
- Add README to setup.py file as long_description