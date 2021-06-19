import cv2
import jason2

img = cv2.imread("/your/image")
res = {"image": str(img.tolist()).encode('base64')}