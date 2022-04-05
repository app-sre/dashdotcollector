from setuptools import setup, find_packages


setup(name='dashdotdb',
      packages=find_packages(),
      version=open('VERSION').read().strip(),
      author='Red Hat Application SRE Team',
      author_email="sd-app-sre@redhat.com",
      description='',
      python_requires='>=3.6',
      license="GPLv2+",
      classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Web Environment',
            'Framework :: Flask',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: '
            'GNU General Public License v2 or later (GPLv2+)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
      ],
      install_requires=[
            "gql==3.1.0",
            'celery==4.4.2',
            'requests==2.23.0',
            'flower==0.9.4',
            'kombu==4.6.8'
      ],
      )
