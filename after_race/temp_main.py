# trong file chính sau khi có dữ liệu thứ tự từng thằng sau 1 trận thì gọi lại hàm trong file podium
# import podium rồi chạy podium.after_race(dữ liệu) và phải import os nữa

import pygame
import podium
import sys

pygame.init()

wnd_width = 1368
wnd_height = 754
screen = pygame.display.set_mode((wnd_width, wnd_height))
race = 1

while True: # while mẫu, đưa hàm vào file chính rồi thì file main này vứt đi (nhớ import os trong file chính nếu chưa)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if race: # race = 1 khi một trận đua đã được thực hiện
        podium.after_race(3, 2, 5, 1, 4, 3, screen, wnd_width, wnd_height)
        #giả sử top 1 số 3, top2 số 2, ..., set nhân vật là 1 
        screen = pygame.display.set_mode((wnd_width, wnd_height))
        # reset tạo screen mới
        race = 0
        #cái race này ông update = 0 ở chỗ khác cũng được
    
    pygame.display.update()
    # cái set 5 sẽ hơi lỏ một tí do cái phần source ảnh ko đủ ảnh để làm cho hoạt ảnh nó mượt : D
      
