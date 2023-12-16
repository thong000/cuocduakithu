import cv2
from deepface import DeepFace
import sys
import pygame
import pygame.camera
import pygame.image
import numpy
import os

import function_faceid  # import này vào file chính

pygame.init()

screen = pygame.display.set_mode((1344, 756))
a=False
b=""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    a,b = function_faceid.FaceID(1, 1344, 756, screen)   # (ngôn ngữ, độ rộng cửa sổ, độ cao cửa sổ, cửa sổ để vẽ đồ lên) 
    # ngôn ngữ 1 là tiếng anh, 0 là tiếng việt
    # cái hàm faceid trả về 1 bool (cho biết việc đăng nhập thành công chưa) và 1 string (tài khoản đã được đăng nhập)
    print(a)
    print(b)
    if a:
        pygame.quit()
        sys.exit()
        