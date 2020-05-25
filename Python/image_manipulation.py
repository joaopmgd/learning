from PIL import Image
import glob, os

path = "/Users/joao/Downloads/Tensorflow/Supermarket/"
image_format = "*.jpeg"
resized_images_path = "/Users/joao/Downloads/Tensorflow/Supermarket/resized/"
divisor = 2

for infile in glob.glob(path + image_format):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    width, height = im.size
    size = (int(width/divisor), int(height/divisor))
    print(("Resizing: %s to %d x %d" % (file[len(path):].encode('UTF-8'), size[0], size[1])))
    im = im.resize(size)
    im.save(resized_images_path+ file[len(path):]+ ".jpeg")