import cv2
import os

hengtu = './hengtu/'
shutu = './shutu/'

image_list = os.listdir('./pixiv/')


def process_image(img,bgcolor,max_side = float(1920),min_side = float(1080)):
    size = img.shape
    h, w = size[0], size[1]
    if max(w,h)/min(w,h) < 16/9:
        scale = min(w, h) / float(min_side)
    else:
        scale = max(w, h) / float(max_side)
    new_w, new_h = int(w/scale), int(h/scale)
    # print(new_w,new_h)
    resize_img = cv2.resize(img, (new_w, new_h))
    # 填充至min_side * min_side
    if h > w:
        top, bottom, left, right = (max_side-new_h)/2, (max_side-new_h)/2, (min_side-new_w)/2, (min_side-new_w)/2
        target = shutu
    else:
        top, bottom, left, right = (min_side-new_h)/2, (min_side-new_h)/2, (max_side-new_w)/2, (max_side-new_w)/2
        target = hengtu
    pad_img = cv2.copyMakeBorder(resize_img, int(abs(top)), int(abs(bottom)), int(abs(left)), int(abs(right)), cv2.BORDER_CONSTANT, value=bgcolor) #从图像边界向上,下,左,右扩的像素数目

    return pad_img,target


for image in image_list:
    print(image)
    img = cv2.imread('./pixiv/'+image)
    bgcolor = cv2.mean(img)
    img_pad,target = process_image(img, list(bgcolor[0:3]))
    cv2.imwrite(os.path.join(target,image),img_pad)
# img = cv2.imread('./pixiv/1.jpg')
# bgcolor = cv2.mean(img)
# print(list(bgcolor[0:3]))
# img_pad = process_image(img,list(bgcolor[0:3]))
# cv2.imwrite(os.path.join(hengtu,'0.jpg'),img_pad)