#image_path = "/Users/n.a./Downloads/Поврежденные крыши/Все крыши/Целые крыши/Снимок экрана 2024-04-29 в 08.52.53.png"  # Путь к вашему изображению

from PIL import Image
import matplotlib.pyplot as plt

def get_image_size(image):
    width, height = image.size
    print("Исходный размер изображения:", width, "x", height)
    return width, height

def crop_image(image, top, right, bottom, left):
    width, height = image.size
    left_coord = left
    upper_coord = top
    right_coord = width - right
    lower_coord = height - bottom
    cropped_image = image.crop((left_coord, upper_coord, right_coord, lower_coord))
    print("Полученный размер обрезанного изображения:", cropped_image.size)
    return cropped_image

# Загружаем исходное изображение
image_path = "/Users/n.a./Downloads/Поврежденные крыши/Все крыши/Целые крыши/Снимок экрана 2024-04-29 в 08.52.53.png"
original_image = Image.open(image_path)

# Определяем и выводим размерность исходного изображения
original_width, original_height = get_image_size(original_image)

# Подрезаем изображение по заданным параметрам
top = 350
right = 650
bottom = 200
left = 650
cropped_image = crop_image(original_image, top, right, bottom, left)

# Отображаем в одном окне исходное и обрезанное изображения
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title("Исходное изображение")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cropped_image)
plt.title("Обрезанное изображение")
plt.axis('off')

plt.show()

# Сохраняем обрезанное изображение
cropped_image.save("/Users/n.a./Downloads/Поврежденные крыши/Все крыши/Целые крыши_обрезанные/cropped_image.png")