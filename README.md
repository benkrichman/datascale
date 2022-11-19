<img align="left" src="./images/datascale_icon.png">

#datascale

Functions for automatic scaling of matplotlib plot axes/resolution to data

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

Scale line width or marker width for line plots and scatter plots to correspond directly to the scale of data on either/both plot axes. For more detail see help output:
```python
help(datascale.plotdatasize)
```

![plotdatasize() example](/images/datascale_plotdatasize_test.png?raw=true)

To reproduce this image view test() in datascale.py or use
```python
datascale.test()
```

### plotdatadpi()

Scale dpi of output image to produce a certain number of pixels per data unit on either/both plot axis/axes. Useful for plots that need a certain amount of detail per axis unit (e.g. geographic projections). For more detail see help output:
```python
help(datascale.plotdatadpi)
```

![plotdatadpi() example](/images/datascale_plotdatadpi_test.png?raw=true)

To reproduce this image view test() in datascale.py or use
```python
datascale.test()
```

