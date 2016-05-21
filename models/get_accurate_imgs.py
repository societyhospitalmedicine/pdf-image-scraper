from PIL import Image

images = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,
1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(len(images))
filename = '../../pdfs/sohm_2014/page_1/1.png'
with Image.open(filename) as im:
    width, height = im.size
    print(im.size)
    print im.format
    print im.mode
    print im.width
    print im.height
    print im.palette
    print im.info
    # print list(im.getdata())
    print im.histogram() 
    print im.getextrema()
    print im.getpixel((1,1))
# page_68 is the crap images 

