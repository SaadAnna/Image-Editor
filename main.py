from PIL import Image, ImageFilter
img_before = Image.open("road.png")
BoxBlurValue = 10
img_after = img_before.filter(ImageFilter.BoxBlur(BoxBlurValue))
img_after.show()