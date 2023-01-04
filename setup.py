import setuptools as st

with open('README.md','r') as ldf:
    longdesc=ldf.read()

st.setup(
    name='datascale',
    version='1.1.1',
    license='MIT',
    url='https://github.com/benkrichman/datascale',
    description='Functions for automatic scaling of matplotlib plot axes/resolution to data',
    long_description=longdesc,
    long_description_content_type="text/markdown",
    author='Benjamin Krichman',
    author_email='benkrichman@gmail.com',
    packages=st.find_packages(),
    install_requires=[
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization"
    ]
)
