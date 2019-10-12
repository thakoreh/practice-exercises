import cv2
img=cv2.imread("galaxy.jpg",0)

print(img)


resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_img)
cv2.imwrite("Galaxy_resize.jpg",resized_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
