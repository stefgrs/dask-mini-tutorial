# dask-mini-tutorial
Mini tutorial on Dask for CMS skills week.

## Setup

### Clone the github repo

`git clone https://github.com/stefgrs/dask-mini-tutorial`


### Create a virtual environment or a conda environment. 

- With virtual env do:

`python3 -m venv /path/to/new/virtual/environment`

`source /path/to/new/virtual/environment/bin/activate`

- With conda do:

`conda create --name dask-tutorial`

`conda activate dask-tutorial`

- With virtualenvwrapper do:

`mkvirtualenv dask-tutorial`

`workon dask-tutorial`

### Install the requirements
From within the folder dask-mini-tutorial, type:

`pip install -r requirements.txt`


### We also need to install the graphviz binaries. 

- On Ubuntu this is done by typing `sudo apt-get install graphviz` (note: this is the only one I actually tested). 

- On MAC, this should be done by typing `brew install graphviz`.

- On Windows this should be done with the following steps.
 
More info here on how to install graphviz at [this stackoverflow thread](https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft).

### Open jupyter notebook

Finally, open jupyter notebook by typing:

`jupyter notebook`

## Easier setup

There is also a Colab version of this two-parts tutorial, but some functionalities will not work as well. 
Make a copy of the notebooks before starting (click on 'File', then on 'save a copy in Drive').

1. The [dask.delayed notebook](https://colab.research.google.com/drive/1tLyHjD8-4Jcn4dqO3OuVijETOK79W1WR?usp=sharing).
2. The [dask.dataframe notebook](https://colab.research.google.com/drive/1tZUXhqUgwF5e_D0jilwe1fNoOE7c-chC?usp=sharing)


-----------------------------------
### Acknowledgements

Parts of it are taken from the [dask tutorial](https://github.com/dask/dask-tutorial) that has the following copyright:
Copyright (c) 2017-2018, Anaconda, Inc. and contributors
All rights reserved.
