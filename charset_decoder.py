from charset_normalizer import detect
import os

folder = os.path.join(os.getcwd(), 'dset\\')
filename = folder + 'wp_vocab10000.vocab'
with open(filename, 'rb') as f:
    data = f.read()
encoding = detect(data).get('encoding')
print(encoding)