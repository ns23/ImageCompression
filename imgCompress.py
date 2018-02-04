import piexif
from PIL import Image
import sys
from core import handle
from core import const
from core import internals
import os

Copyright = "Paresh Sawant"  # add name of copyright holder
Artist = "Paresh Sawant"  # add name of attist


def compress_file(filePath):
    if internals.is_valid_path(filePath):
        compress_image([filePath])
    else:
        print "Not a valid file format"


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
            im = Image.open(image_path)
            exif_dict = modify_exif(piexif.load(im.info["exif"]))
            exif_bytes = piexif.dump(exif_dict)

            if const.args.output:
                if const.args.dir:
                    image_path = const.args.output + \
                        image_path.split(const.args.dir)[1]
                elif const.args.file:

                    rel_path = image_path.split(
                        os.path.dirname(os.path.realpath(const.args.file)))
                    if os.path.isdir(rel_path[0]):
                        image_path = os.path.join(
                            const.args.output, rel_path[1])
                    else:
                        image_path = os.path.join(
                            const.args.output, const.args.file)
                        pass

                if not os.path.exists(os.path.dirname(image_path)):
                    os.makedirs(os.path.dirname(image_path))
                pass

            im.save(image_path, "jpeg", exif=exif_bytes,
                    quality=const.args.quality)
            im.close()
            pass
        except IOError:
            print "Not able to open file"
            pass
        finally:
            count = count + 1
            print("Processed: " + str(count) + "/" + str(file_count))


if __name__ == '__main__':
    const.args = handle.get_arguments()

    # check if output folder paramter is provided
    if const.args.output:
        if internals.is_valid_folder(const.args.output):
            print "valid folder"
        else:
            # take default folder instead
            sys.exit(0)
    try:
        if const.args.dir:
            image_files = internals.get_all_images(const.args.dir)
            compress_image(image_files)
        elif const.args.file:
            compress_file(const.args.file)
        sys.exit(0)
    except KeyboardInterrupt as e:
        sys.exit(3)
        pass
