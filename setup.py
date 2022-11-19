import setuptools as st

with open('README.md','r') as ldf:
    longdesc=ldf.read()

st.setup(
    name='datascale',
    version='0.1.0',
    license='MIT',
    url='https://github.com/benkrichman/datascale',
    description='Functions for automatic scaling of matplotlib plot axes/resolution to data',
    long_description=longdesc,
    long_description_content_type="text/markdown",
    author='Benjamin Krichman',
    author_email='benkrichman@gmail.com',
    packages=['datascale'],
    install_requires=[
        'numpy',
        'matplotlib'
    ],
)
