#from matplotlib.pyplot import imread, imsave
import numpy as np
import cv2
import ocroseg
import subprocess

seg = ocroseg.Segmenter("lowskew-000000259-011440.pt")
#image = 1.0 - imread("results-ocroseg-drive/doc-rec.png")
ii = cv2.imread("testdata/W1P0.png")
gray_image = (255 - cv2.cvtColor(ii, cv2.COLOR_BGR2GRAY)).astype(np.float32)/255
print gray_image.shape
#cv2.imwrite("results-ocroseg-drive/BI.png", gray_image)
lines = seg.extract_textlines(gray_image)
#imsave("results-ocroseg-drive/main.png", seg.lines)
main_lines = 255 - (seg.lines*255).astype(np.uint8)
#print main_lines.shape
#print main_lines
cv2.imwrite("results-ocroseg-drive-test/main.png", main_lines)
for idx, line in enumerate(lines):
    #imsave("results-ocroseg-drive/line_%d.png"%idx, line['image'])
    img_line = 255 - (line['image']*255).astype(np.uint8)
#    print img_line.shape
#    print img_line
    cv2.imwrite("results-ocroseg-drive-test/line_%d.png"%idx, img_line)

subprocess.call(["gdrive", "sync", "upload", "results-ocroseg-drive-test/", "1QRVDaYjdcAUqj1sh59_1NmE5bgAyvTcD"])
