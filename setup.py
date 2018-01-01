from setuptools import setup


install_requires = [
    'click',
    'cookiecutter',
    'pyyaml',
    'isort'
]

tests_require = [
    'pytest',
]


setup(
    name='fgen',
    version='0.1',
    py_modules=['base', 'config'],
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points='''
        [console_scripts]
        fgen=base:hello
    '''
)
