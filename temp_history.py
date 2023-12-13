import pygame
import sys
import textwrap
import re

bg = pygame.image.load("background/menugamemap.png")
bg = pygame.transform.scale(bg, (1344, 756))


# Hàm để đọc tệp và trả về danh sách các dòng
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
text = "abc 123 def"

# Sử dụng regex để tìm số trong chuỗi
numbers = re.findall(r'\d+', text)

# Chuyển đổi từng số thành số nguyên
numeric_values = [int(number) for number in numbers]


# In các giá trị số
print("Các giá trị số từ chuỗi:", numeric_values[0])

# Hàm để vẽ danh sách lên màn hình với chức năng lăn chuột
def draw_text_list(screen, text_list, font, scroll_y):
    screen.blit(bg, (0, 0))
    column_width = 200  # Độ rộng của mỗi cột

    # Can giữ và vẽ từng dòng trong danh sách
    for i, line in enumerate(text_list):
        columns = line.strip().split(',')  # Phân chia dòng thành các cột
        for j, column in enumerate(columns):
            wrapped_lines = textwrap.wrap(column, width=22)  # Can giữ với chiều rộng tối đa 15 ký tự
            for k, wrapped_line in enumerate(wrapped_lines):
                text_surface = font.render(wrapped_line, True, (0, 0, 0))  # Màu chữ đen
                x_position = j * column_width + 10  # Vị trí của mỗi cột
                y_position = i * 20 + k * 20 - scroll_y  # Vị trí của mỗi dòng con trong cột, điều chỉnh theo lăn chuột
                screen.blit(text_surface, (x_position, y_position))

    pygame.display.flip()


# Hàm main
def main():
    pygame.init()

    # Kích thước cửa sổ
    window_size = (1344, 756)

    # Tạo cửa sổ đồ họa
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Text File Viewer")

    # Font cho văn bản
    font = pygame.font.Font(None, 24)

    # Đường dẫn của tệp văn bản
    file_path = 'account/thanhthong/history.txt'  # Thay thế bằng đường dẫn thực tế của tệp văn bản của bạn

    # Đọc tệp và chuyển thành danh sách
    text_list = read_file(file_path)

    # Biến để theo dõi vị trí vuốt màn hình
    scroll_y = 0

    # Vòng lặp chính
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Bắt sự kiện lăn lên
                scroll_y += 20  # Điều chỉnh vị trí lên
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Bắt sự kiện lăn xuống
                scroll_y -= 20  # Điều chỉnh vị trí xuống

        # Giới hạn vị trí vuốt để không cho phép màn hình vượt quá nội dung
        scroll_y = max(0, min(scroll_y, len(text_list) * 20 * len(max(text_list, key=len))))

        # Vẽ danh sách lên màn hình với chức năng lăn chuột
        draw_text_list(screen, text_list, font, scroll_y)




if __name__ == "__main__":
    main()
