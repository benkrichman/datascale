<h1><img align="left" src="https://github.com/benkrichman/datascale/raw/main/images/datascale_icon.png" width="130">datascale</h1>

Functions for automatic scaling of matplotlib line width, marker width, fontsize, and resolution to data

\
[![Downloads](https://pepy.tech/badge/datascale)](https://pepy.tech/project/datascale)   
[![PyPI version](https://badge.fury.io/py/datascale.svg)](https://badge.fury.io/py/datascale)

## Installation

```bash
pip install datascale
```

or

```bash
pip install git+https://github.com/benkrichman/datascale.git@main
```

## Main Functions

### plotdatasize()

Scale line width, marker width, or fontsize for plots to correspond directly to the scale of data on either/both plot axes. For more detail see help output:
```python
help(datascale.plotdatasize)
```

![plotdatasize() example](https://github.com/benkrichman/datascale/raw/main/images/datascale_plotdatasize_test.png?raw=true)

To reproduce this image view test() in datascale.py or use
```python
datascale.test()
```

### plotdatadpi()

Scale dpi of output image to produce a certain number of points per data unit on either/both plot axis/axes. Useful for plots that need a certain amount of detail per axis unit (e.g. geographic projections). For more detail see help output:
```python
help(datascale.plotdatadpi)
```

![plotdatadpi() example](https://github.com/benkrichman/datascale/raw/main/images/datascale_plotdatadpi_test.png?raw=true)

To reproduce this image view test() in datascale.py or use
```python
datascale.test()
```

