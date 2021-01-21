
import cv2



def canny_edge(image):

		# make it grayscale
	Gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	# Make canny Function
	canny=cv2.Canny(Gray,40,140)

	return canny
