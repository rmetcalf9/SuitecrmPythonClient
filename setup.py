from setuptools import setup
import versioneer

#Dependancy lists maintained here and in tox.ini
sp_install_requires = [
  'requests==2.31.0',
  'pytz==2019.3',
  'python-dateutil==2.8.1',
  'PythonAPIClientBase==0.0.9'
]
sp_tests_require = [
  'pytest==7.1.2',
  'python_Testing_Utilities==0.1.10'
]

all_require = sp_install_requires + sp_tests_require

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='SuitecrmPythonClient',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Python package which provides Suitecrm Client',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/rmetcalf9/SuitecrmPythonClient',
      author='Robert Metcalf',
      author_email='rmetcalf9@googlemail.com',
      license='MIT',
      packages=['SuitecrmPythonClient', 'SuitecrmPythonClient.ResourceWrappers'],
      zip_safe=False,
      install_requires=sp_install_requires,
      tests_require=sp_tests_require,
      include_package_data=True)
