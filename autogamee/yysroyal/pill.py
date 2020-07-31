from PIL import Image
im=Image.open('ten_end.png')
pix=im.load()
print(pix[13,21])
im_g=im.convert('L')
pix_g=im_g.load()
print(pix_g[13,21])