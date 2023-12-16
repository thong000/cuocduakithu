import cv2
from deepface import DeepFace
import sys
import pygame
import pygame.camera
import pygame.image
import numpy
import os

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font('faceid_python/f_resource/vn.otf', 32)


class Text:
    def __init__(self, font, text, r, g, b, ):
        self.font = font
        self.text = text
        self.font_but = self.font.render(text, True, (r, g, b))

    def draw_text(self, sur, x, y):
        sur.blit(self.font_but, (x, y))


class Button:
    def __init__(self, image, x, y, w, h):
        self.but_pos = (x, y)
        self.x = x
        self.y = y
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.image_rect = self.image.get_rect(center=(x, y))

    def draw_but(self, sur):
        sur.blit(self.image, self.image_rect)


def check_press(rect, pos):
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False


class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = ""
        self.txt_surface = FONT.render(self.text, True, (255, 255, 255))
        self.active = False


def pygameSurfaceToCv2Image(selected_area):
    # selected_area =  mysurface.subsurface((x, y, w, h))
    img_array = numpy.array(pygame.surfarray.pixels3d(selected_area))
    image_object = numpy.transpose(img_array, (1, 0, 2))
    image_object[:, :, [0, 2]] = image_object[:, :, [2, 0]]
    image_object = image_object[150:650, 400:1000]
    return image_object


def FaceID(lang, wnd_width, wnd_height, screen):
    global account, name_list
    pbutton_image = pygame.image.load('faceid_python/f_resource/button.jfif')
    pbutton_image.set_colorkey((255, 255, 255))
    background = pygame.image.load('faceid_python/f_resource/background.png')
    background = pygame.transform.scale(background, (wnd_width, wnd_height))

    pygame.camera.init()
    cam_list = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(cam_list[0])
    cam.start()

    # variable
    running = True
    login = register = 0
    menu = 1
    step1 = 1
    step2 = step3 = step4 = 0
    log1 = 1
    log2 = 0
    counter = 0
    login_account = ''
    login_success = False
    k = 0

    register_box = InputBox(522, 353, 300, 50)

    # Button
    login_but = Button(pbutton_image, 684, 350, 240, 75)
    register_but = Button(pbutton_image, 684, 400, 240, 75)
    next_but = Button(pbutton_image, 1100, 700, 200, 75)
    back_but = Button(pbutton_image, 100, 700, 200, 75)
    step_expl = Button(pbutton_image, 672, 50, 1000, 150)
    step2_warn = Button(pbutton_image, 600, 700, 700, 75)
    middle = Button(pbutton_image, 674, 372, 1100, 150)

    # Text
    if lang:
        login_text = Text(FONT, 'Login', 255, 255, 255)
        register_text = Text(FONT, 'Register', 255, 255, 255)
        next_text = Text(FONT, "Next", 255, 255, 255)
        back_text = Text(FONT, "Back", 255, 255, 255)

        step1_text1 = Text(FONT, "Create an account name", 255, 255, 255)
        step1_text2 = Text(FONT, "Account already exists", 255, 255, 255)
        step2_text1 = Text(FONT, "Please put your head in the red rectangle below", 255, 255, 255)
        step2_text2 = Text(FONT, "Press Enter to take a picture of yourself", 255, 255, 255)
        step2_text3 = Text(FONT, "Picture has been taken", 255, 255, 255)
        step2_text4 = Text(FONT, "An account with the same data has existed", 255, 255, 255)
        step3_text1 = Text(FONT, "Please put your head in the red rectangle below again", 255, 255, 255)
        step3_text2 = Text(FONT, "to comfirm the validity of the taken picture", 255, 255, 255)
        step4_text = Text(FONT, "Register complete, you can now use FaceID to login", 255, 255, 255)

        # login_text = Text(FONT, "Please put your head in the red rectangle", 255, 255, 255)
        notfound = Text(FONT, "Account not found", 255, 255, 255)
        found2 = Text(FONT, "Do you wish to continue?", 255, 255, 255)
    else:
        login_text = Text(FONT, 'Đăng nhập', 255, 255, 255)
        register_text = Text(FONT, 'Đăng kí', 255, 255, 255)
        next_text = Text(FONT, "Tiếp theo", 255, 255, 255)
        back_text = Text(FONT, "Quay lại", 255, 255, 255)

        step1_text1 = Text(FONT, "Tạo một tên tài khoản mới", 255, 255, 255)
        step1_text2 = Text(FONT, "Tài khoản đã tồn tại", 255, 255, 255)
        step2_text1 = Text(FONT, "Hãy đưa mặt của bạn vào hình chữ nhật bên dưới", 255, 255, 255)
        step2_text2 = Text(FONT, "Nhấn Enter để selfie bản thân", 255, 255, 255)
        step2_text3 = Text(FONT, "Ảnh đã được chụp", 255, 255, 255)
        step2_text4 = Text(FONT, "Một tài khoản với cùng khuôn mặt đã được đăng kí", 255, 255, 255)
        step3_text1 = Text(FONT, "Hãy đưa mặt của bạn vào lại hình chữ nhật bên dưới", 255, 255, 255)
        step3_text2 = Text(FONT, "để kiểm tra tính khả thi của bức ảnh bạn vừa chụp", 255, 255, 255)
        step4_text = Text(FONT, "Đăng kí thành công, bạn giờ có thể sử dụng FaceID để đăng nhập", 255, 255, 255)

        notfound = Text(FONT, "Tài khoản không tìm thấy", 255, 255, 255)
        found2 = Text(FONT, "Bạn có muốn tiếp tục không?", 255, 255, 255)

    while True:
        screen.fill((0, 0, 0))
        pos = pygame.mouse.get_pos()
        clock = pygame.time.Clock()
        counter += 1

        if menu:
            screen.blit(background, (0, 0))
            name_list = os.listdir('faceid_python/id_image')
            if login_success:
                break;

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            register_but.draw_but(screen)
            login_but.draw_but(screen)
            register_text.draw_text(screen, register_but.x - 70, register_but.y - 30)
            login_text.draw_text(screen, login_but.x - 70, login_but.y - 30)

            if check_press(register_but.image_rect, pos):
                register = 1
                menu = 0
                warn = 0
            if check_press(login_but.image_rect, pos):
                login = 1
                menu = 0

        if register:  # dang ki               
            if step1:  # nhap ten acc va kiem tra acc da ton tai hay chua
                k = 0
                screen.blit(background, (0, 0))
                if check_press(register_box.rect, pos):
                    register_box.active = True

                register_box.color = COLOR_ACTIVE if register_box.active else COLOR_INACTIVE

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if register_box.active:
                            if event.key == pygame.K_BACKSPACE:
                                register_box.text = register_box.text[:-1]
                            else:
                                register_box.text += event.unicode

                width = max(200, register_box.txt_surface.get_width() + 10)
                register_box.rect.w = width

                register_box.txt_surface = FONT.render(register_box.text, True, (255, 255, 255))
                pygame.draw.rect(screen, register_box.color, register_box.rect)
                screen.blit(register_box.txt_surface, (register_box.rect.x + 5, register_box.rect.y + 5))

                step_expl.draw_but(screen)
                step1_text1.draw_text(screen, step_expl.x - 250, step_expl.y - 50)

                next_but.draw_but(screen)
                next_text.draw_text(screen, next_but.x - 50, next_but.y - 18)
                if check_press(next_but.image_rect, pos):
                    name_not_repeat = True
                    for name in name_list:
                        temp_name = name.replace(".jpg", "")
                        if temp_name == register_box.text:
                            name_not_repeat = False

                    if name_not_repeat:
                        account = register_box.text
                        step1 = 0
                        step2 = 1
                        warn = 0
                    else:
                        warn = 1
                if warn: step1_text2.draw_text(screen, step_expl.x - 250, step_expl.y - 5)

                back_but.draw_but(screen)
                back_text.draw_text(screen, back_but.x - 50, back_but.y - 18)
                if check_press(back_but.image_rect, pos):
                    register = 0
                    menu = 1

            if step2:  # chup anh va kiem tra anh co ton tai?

                image = cam.get_image()
                image = pygame.transform.scale(image, (wnd_width, wnd_height))

                screen.blit(image, (0, 0))
                step_expl.draw_but(screen)
                step2_text1.draw_text(screen, step_expl.x - 270, step_expl.y - 50)
                step2_text2.draw_text(screen, step_expl.x - 270, step_expl.y - 5)
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(400, 150, 600, 500), 3)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            temp_image = pygameSurfaceToCv2Image(image)
                            min_dist = 1
                            for name in name_list:
                                compare = cv2.imread('faceid_python/id_image/' + name)
                                try:
                                    dist = DeepFace.verify(temp_image, compare)["distance"]
                                except ValueError:
                                    dist = 1
                                if dist < min_dist:
                                    min_dist = dist
                            if min_dist < 0.21:
                                warn = 2
                            else:
                                k = 1
                                warn = 1
                                chosen_image = temp_image

                if warn:
                    step2_warn.draw_but(screen)
                    if warn == 1:
                        step2_text3.draw_text(screen, step2_warn.x - 280, step2_warn.y - 15)
                    else:
                        step2_text4.draw_text(screen, step2_warn.x - 380, step2_warn.y - 15)

                next_but.draw_but(screen)
                next_text.draw_text(screen, next_but.x - 50, next_but.y - 18)
                back_but.draw_but(screen)
                back_text.draw_text(screen, back_but.x - 50, back_but.y - 18)
                if check_press(next_but.image_rect, pos) and k:
                    step2 = 0
                    step3 = 1
                if check_press(back_but.image_rect, pos):
                    step2 = 0
                    step1 = 1
                    warn = 0

            if step3:  # kiem tra do chinh xac cua anh
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                image = cam.get_image()
                image = pygame.transform.scale(image, (wnd_width, wnd_height))
                screen.blit(image, (0, 0))
                step_expl.draw_but(screen)
                step3_text1.draw_text(screen, step_expl.x - 300, step_expl.y - 50)
                step3_text2.draw_text(screen, step_expl.x - 300, step_expl.y - 5)
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(400, 150, 600, 500), 3)

                if counter % 80 == 0:
                    live_image = pygameSurfaceToCv2Image(image)

                    try:
                        if DeepFace.verify(live_image, chosen_image)["distance"] < 0.21:
                            step3 = 0
                            step4 = 1
                    except ValueError:
                        pass

                back_but.draw_but(screen)
                back_text.draw_text(screen, back_but.x - 50, back_but.y - 18)
                if check_press(back_but.image_rect, pos):
                    step3 = 0
                    step2 = 1
                    warn = 0

            if step4:  # thong bao dang ki thanh cong
                screen.blit(background, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                cv2.imwrite('faceid_python/id_image/' + account + '.jpg', chosen_image)
                middle.draw_but(screen)
                step4_text.draw_text(screen, middle.x - 500, middle.y - 10)

                next_but.draw_but(screen)
                next_text.draw_text(screen, next_but.x - 50, next_but.y - 18)
                if check_press(next_but.image_rect, pos):
                    step4 = 0
                    step1 = 1
                    register = 0
                    menu = 1

        if login:
            if log1:  # kiểm tra mặt
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                image = cam.get_image()
                image = pygame.transform.scale(image, (wnd_width, wnd_height))
                screen.blit(image, (0, 0))
                step_expl.draw_but(screen)
                step2_text1.draw_text(screen, step_expl.x - 250, step_expl.y - 30)
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(400, 150, 600, 500), 3)

                if counter % 80 == 0:
                    min_dist = 1
                    live_image = pygameSurfaceToCv2Image(image)
                    for name in name_list:
                        compare = cv2.imread('faceid_python/id_image/' + name)
                        try:
                            dist = DeepFace.verify(live_image, compare)["distance"]
                        except ValueError:
                            dist = 1
                        if dist < min_dist:
                            min_dist = dist
                            account = name.replace(".jpg", "")
                    if min_dist < 0.21:
                        log1 = 0
                        log2 = 1

                back_but.draw_but(screen)
                back_text.draw_text(screen, back_but.x - 50, back_but.y - 18)
                if check_press(back_but.image_rect, pos):
                    login = 0
                    menu = 1

            if log2:  # thông báo có tài khoản trùng khớp
                screen.blit(background, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                if lang:
                    found1 = Text(FONT, "Account '" + account + "' results in a match", 255, 255, 255)
                else:
                    found1 = Text(FONT, "Tài khoản '" + account + "' khớp với dữ liệu đưa vào", 255, 255, 255)
                middle.draw_but(screen)
                found1.draw_text(screen, middle.x - 250, middle.y - 50)
                found2.draw_text(screen, middle.x - 250, middle.y - 5)
                next_but.draw_but(screen)
                next_text.draw_text(screen, next_but.x - 50, next_but.y - 18)
                back_but.draw_but(screen)
                back_text.draw_text(screen, back_but.x - 50, back_but.y - 18)
                if check_press(next_but.image_rect, pos):
                    login_account = account
                    login_success = True
                    menu = 1
                    login = 0
                if check_press(back_but.image_rect, pos):
                    log2 = 0
                    log1 = 1

        clock.tick(60)
        pygame.display.update()

    return login_success, login_account
    # bool (đăng nhập thành công), string (tài khoản được đăng nhập)
