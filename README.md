# Training lstm and transformer models. cs182

### env creation for running locally:

- recommend running in google colab so we don't have to create a local environment, the instructions below will get you most of the way there if you do choose to use a local environment, but there may be some additional packages that need to be installed

- install pytorch and torchvision from pytorch channel

- then install (some redundancy with pytorch but is okay):
numpy matplotlib pillow scipy h5py scikit-image cython imageio jupyter nltk

- I used mamba, and python 3.11 (installed by pytorch by default)

### potential issues

- running these notebooks is quite slow depending on hardware

- if certain data files are missing, may need to run certain bash scripts in the /datasets directories

- for cython issues, run the following from /deeplearning directories and restart kernel:
python setup.py build_ext --inplace 

- for character encoding issues visit charset_decoder.py file
