# ImageCompression

Python script to compress Images in a folder and all subfolders inside it without losing quality and exif information.

In the script quality value is set to70 % of original value.Can be changed based on requiremnet

## Dependencies
1.Pillow
2.Piexif

## Installation

```
$ cd
$ git clone https://github.com/ns23/ImageCompression.git
$ cd ImageCompression
$ pip install -U -r requirements.txt
```

**Important:** 

if you have installed both Python 2 and 3, the `pip` command
could invoke an installation for Python 2. To see which Python version `pip`
refers to, try `$ pip -V`. If it turns out `pip` is your Python 2 pip, try
`$ pip3 install -U -r requirements.txt` instead.


Run the Program in terminal
enter the path of folder.Hit Enter
Script will select all imagesin the folder and compress the images
Using piexif exif data is copied to compressed image


## Instructions for Compressing Images

**Important:** as like with `pip`, there might be no `$ python3` command.
This is most likely the case when you have only Python 3 but not 2 installed.
In this case try the `$ python` command instead of `$ python3`,
but make sure `$ python -V` gives you a `Python 3.x.x`!

- For all available options, run `$ python imgCompress.py --help`.
```
usage: imgCompress.py [-h] 
        (-d DIR | -f FILE)
         [-q QUALITY]

    optional arguments:
        -d DIRECTORY, --dir DIRECTORY Compress all images from folder / subfolder
        -f FILENAME, --file FILENAME Compress a single image file
```
