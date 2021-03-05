# dask-mini-tutorial
Mini tutorial on Dask for CMS skills week.

## How to use
<p>
1. Clone the github repo:

`git clone https://github.com/stefgrs/dask-mini-tutorial`

</p>

<p>
2. Create a virtual environment or a conda environment. 

With virtual env do :
`python3 -m venv /path/to/new/virtual/environment`
`source /path/to/new/virtual/environment/bin/activate`

With conda do:

`conda create --name dask-tutorial`
`conda activate dask-tutorial`

With virtualenvwrapper do:

`mkvirtualenv dask-tutorial`
`workon dask-tutorial`

</p>

<p>
3. From within the folder dask-mini-tutorial, install the requirements:

`pip install -r requirements.txt`

</p>
<p>

4. We also need to install the graphviz binaries. 

On Ubuntu this is done by typing `sudo apt-get install graphviz` (note: this is the only one I actually tested). 

On MAC, this should be done by typing `brew install graphviz`.

On Windows this should be done with the following steps.
 
More info here on how to install graphviz at [this stackoverflow thread](https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft)
</p>
<p>

5. Finally, open jupyter notebook by typing:

jupyter notebook

There is also a Colab version here [add link](), but some functionalities will not work as well.

-----------------------------------
Parts of it are taken from the [dask tutorial](https://github.com/dask/dask-tutorial) that has the following copyright:
Copyright (c) 2017-2018, Anaconda, Inc. and contributors
All rights reserved.
