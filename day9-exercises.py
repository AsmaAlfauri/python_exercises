# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:42:46 2019

@author: Asma Alfauri
"""


# =============================================================================
# #Ex-1:
# import statistics as st
# X=[3, 1.5, 4.5, 6.75, 2.25, 5.75,2.25,10,120,12.5,13]
# print(st.mean(X)) 
# print(st.harmonic_mean(X))
# print(st.median (X) ) 
# print(st.median_low (X) ) 
# print(st.median_high(X) ) 
# print(st.median_grouped(X)) 
# print(st.mode(X)) 
# print(st.pstdev(X)) 
# print(st.pvariance(X)) 
# print(st.stdev(X)) 
# print(st.variance(X))
# 
# =============================================================================

# =============================================================================
# #Ex-2:
# 
# import random
# print( random.random() )
# print ( random.randrange(10) )
# print ( random.choice(['Ali', 'Khalid', 'Hussam']) ) 
# print ( random.sample(range(1000), 10) )
# print ( random.choice('OrangeAcademy') )
# items = [1,5,8,9,2,4]
# random.shuffle(items)
# print( items ) 
# print ( random.randint(20,30) )
# print ( random.randrange(1000, 2111, 5) )
# print  ( random.uniform(10000, 1100))
# 
# =============================================================================

# =============================================================================
# 
# #Ex-3:
# import math
# print("pi= ",math.pi)
# print ("cos(200)=" ,math.cos(200))
# print ("sin(30)=" ,math.sin(30))
# print ("tan(180)=" ,math.tan(180))
# print(math.floor(10.8))
# print(math.ceil(10.8))
# 
# 
# =============================================================================

# =============================================================================
# #Ex-4:
# from PIL import Image,ImageFilter,ImageDraw
# im1=Image.open('timon.jpg')
# im2=Image.open('timon1.jpg').resize(im1.size)
# 
# im1.show()
# print (im1.format , im1.size , im1.mode)
# 
# im1_filp=im1.transpose(Image.FLIP_TOP_BOTTOM)
# im1_filp.show()
# 
# greyscale_image=im1.convert('L')
# greyscale_image.show()
# 
# croppedImage=im1.crop((0,0,50,50))
# croppedImage.show()
# 
# draw=ImageDraw.Draw(im1)
# draw.line((0,0)+im1.size, fill = (225,225,225))
# draw.line((0,im1.size[1], im1.size[0],0),fill=(225,225,225))
# draw.text((im1.size[0]/2-im1.size[0]/2,im1.size[1]/2+20),'Asma',fill=(225,225,0))
# draw.text((im1.size[0]/2-im1.size[0]/2,im1.size[1]/2-60),'Image',fill=(225,225,0))
# im1.show()
# 
# 
# newImage2=im2.filter(ImageFilter.SHARPEN)
# newImage2.show()
# newImage2=im2.filter(ImageFilter.EDGE_ENHANCE)
# newImage2.show()
# newImage3=im2.filter(ImageFilter.FIND_EDGES)
# newImage3.show()
# newImage4=im2.filter(ImageFilter.SMOOTH)
# newImage4.show()
# 
# 
# Image.blend(im1,im2,0.5).save('newimg.jpg'.format(0.5))
# im=Image.open('newimg.jpg')
# im.show()
# 
# blurred=im1.filter(ImageFilter.BLUR)
# im1.show()
# 
# size=(128,128)
# saved="timon4.png"
# try:im
# except:print("Unable to load image")
# im.thumbnail(size)
# im.save(saved)
# im.show()
# 
# 
# im1_flip=im1.transpose(Image.ROTATE_90)
# im1_flip.show()
# 
# mask=Image.open('mask.png')
# mask=mask.resize(im1.size)
# Image.composite(im1,im2,mask).save('maskimage.jpg')
# imagMask=Image.open('maskimage.jpg')
# imagMask.show()
# =============================================================================








