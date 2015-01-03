from setuptools import setup, find_packages


setup(name='pi-shuffler',
      version='0.0.1',
      install_requires=[
        'python-mpd2',
      ],
      test_suite='nose.collector',
      tests_require=[
        #'mock',
      ],
      setup_requires=[
        'nose',
        'coverage',
        #'mock',
      ],
      )
