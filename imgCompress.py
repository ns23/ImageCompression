import piexif
import os
from PIL import Image
from core import handle
from core import const

Copyright = "Paresh Sawant"  # add name of copyright holder
Artist = "Paresh Sawant"  # add name of attist
quality = 70


def get_images(path):
    os.chdir(path)
    return [f for f in os.listdir(path) if os.path.isfile(f)]
    pass


def get_all_images(root):
    valid_format = ['JPG', 'JPEG']
    response = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            extension = name.split('.')[-1:][0].upper()
            if extension in valid_format:
                # print str(i) + " " + str(os.path.join(path, name))
                response.append(os.path.join(path, name))

    return response


def modify_exif(exif_dict):
    global Copyright, Artist

    if exif_dict is not 0:
        exif_dict['0th'][piexif.ImageIFD.Copyright] = Copyright
        exif_dict['0th'][piexif.ImageIFD.Artist] = Artist

    return exif_dict


def compress_image(imagefiles):
    file_count = len(imagefiles)
    count = 0
    for image_path in imagefiles:
        try:
            # image_path = path + '/' + image
            im = Image.open(image_path)
            exif_dict = modify_exif(piexif.load(im.info["exif"]))
            exif_bytes = piexif.dump(exif_dict)
            im.save(image_path, "jpeg", exif=exif_bytes, quality=const.args.quality)
            im.close()
            pass
        except IOError:
            print "Not able to open file"
            pass
        finally:
            count = count + 1
            print("Processed: " + str(count) + "/" + str(file_count))



if __name__ == '__main__':
    const.args =  handle.get_arguments();
    if const.args.dir:
        image_files = get_all_images(const.args.dir)
        compress_image(image_files)
    elif const.args.file:
        print "Write logic to compress single file"
        pass    
