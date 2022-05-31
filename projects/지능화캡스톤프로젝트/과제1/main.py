
#1. Open CV 사용 선언
import random
import cv2

#2. imread : 괄호안의 경로 이미지를 불러온다.
image = cv2.imread('image_F16.png')

#3. shape : 이미지의 정보를 가져온다.
#가로 픽셀수
image_width = image.shape[1]
print(f"Width : {image_width}",)
#세로 픽셀수
image_height = image.shape[0]
print(f"Height : {image_height}")
#채널(컬러 이미지는 Blue, Red, Green 세개의 채널, 흑백 이미지는 1개 채널)의 숫자
image_channel_count = image.shape[2]
print(f"Channel : {image_channel_count}")

#4. 이미지 변환 및 화면 출력
#imshow("제목", 출력이미지)
cv2.imshow("original image",image)
#cvtColor(원본이미지, 변환형식)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("gray image",gray_image)
cv2.imshow("hsv image",hsv_image)

cv2.waitKey(0)


#5. 이미지 크기 변환
cv2.imshow("original image",image)
#resize(변경할 이미지, 크기)
half_image = cv2.resize(image, (256,256))
cv2.imshow("half image",half_image)
cv2.waitKey(0)


#6. 이미지 저장
cv2.imwrite('half_img.png', half_image)

#7. 픽셀 변환
blue_img = image.copy()
#원본 이미지의 256이하의 세로 픽셀을 파란색으로 변경
blue_img[:256] = (255,0,0) #BGR
cv2.imshow("Half Blue image",blue_img)

red_img = image.copy()
#원본 이미지의 256이하의 가로 픽셀을 빨간색으로 변경
red_img[:,:256] = (0,0,255) #BGR
cv2.imshow("Half Red image",red_img)

#원본 이미지에서 랜덤한 픽셀을 빨간색으로 변경
rand_img = image.copy()
w, h = rand_img.shape[1], rand_img.shape[0]
for i in range(10000):
    rand_w = random.randrange(w)
    rand_h = random.randrange(h)
    rand_img[rand_w,rand_h] = (0,0,255)

cv2.imshow("Random Point",rand_img)

cv2.waitKey(0)