import qrcode
img = qrcode.make("hello Guys i am Akash Pandey Lets begin With the Our First Python Project")
img.save("youtubeQR.jpg")



import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("myQRCode.jpg"))
print("Decoded text is: ", val)