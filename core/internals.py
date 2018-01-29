import os

valid_format = ['JPG', 'JPEG']


def get_images(path):
    """"""
    os.chdir(path)
    return [f for f in os.listdir(path) if os.path.isfile(f)]


def get_all_images(root):
    """Get images from all folders and subfolders"""
    response = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            extension = name.split('.')[-1:][0].upper()
            if extension in valid_format:
                # print str(i) + " " + str(os.path.join(path, name))
                response.append(os.path.join(path, name))

    return response


def is_valid_path(filePath):
    """ Check if file path is valid """
    respone = False
    if os.path.isfile(filePath):  # split this code
        extension = filePath.split('.')[-1:][0].upper()
        if extension in valid_format:
            respone = True

    return respone


def is_valid_folder(folderPath):
    """ Check if folder exists """
    respone = False
    if os.path.isdir(folderPath):
        respone = True
    elif create_folder(folderPath):
        respone = True
    return respone


def create_folder(folderPath):
    """ Create folder """
    try:
        os.makedirs(folderPath)
        return True
    except OSError:
        return False

def get_full_path(path):
    pass


