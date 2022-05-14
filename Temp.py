from PIL import Image,ImageOps

num = 1
img1 = f'VOCdevkit/VOC2007/JPEGImages/{str(num)}.jpg'
img2 = f'VOCdevkit/VOC2007/TemplateImages/{str(num)}.jpg'

image = [Image.open(img1), Image.open(img2)]
# image = [ImageOps.exif_transpose(_) for _ in image]
image[0].show()
image[1].show()
exit()
# im_rotate = image[1].rotate(180, expand=1)
# im_rotate.save(img2)