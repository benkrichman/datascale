# datascale

Functions for automatic scaling of matplotlib plot axes/resolution to data

## plotdatasize()

Scale line width or marker width for line plots and scatter plots to correspond directly to the scale of data on either/both plot axes.

![plotdatasize() example](/images/datascale_plotdatasize_test.png?raw=true)

To reproduce this image use datascale.test() or view test() in datascale.py

## plotdatadpi()

Scale dpi of output image to produce a certain number of pixels per data unit on either/both plot axis/axes. Useful for plots that need a certain amount of detail per axis unit (e.g. geographic projections).

![plotdatadpi() example](/images/datascale_plotdatadpi_test.png?raw=true)

To reproduce this image use datascale.test() or view test() in datascale.py

