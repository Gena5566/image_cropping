from PIL import Image
import os

def crop_image(image, top, right, bottom, left):
    width, height = image.size
    left_coord = left
    upper_coord = top
    right_coord = width - right
    lower_coord = height - bottom
    cropped_image = image.crop((left_coord, upper_coord, right_coord, lower_coord))
    return cropped_image

# Путь к папке с исходными изображениями
input_folder = "/Users/n.a./Downloads/Поврежденные крыши/Все крыши/Поврежденные крыши/"

# Путь к папке для сохранения обрезанных изображений
output_folder = "/Users/n.a./Downloads/Поврежденные крыши/Все крыши/Повреж. крыши_обрезаные/"

# Параметры обрезки
top = 350
right = 650
bottom = 200
left = 650

# Счетчик для именования файлов
counter = 1

# Перебираем все файлы в папке
for filename in os.listdir(input_folder):
    # Проверяем, что файл - изображение
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Открываем изображение
        image_path = os.path.join(input_folder, filename)
        original_image = Image.open(image_path)

        # Подрезаем изображение
        cropped_image = crop_image(original_image, top, right, bottom, left)

        # Формируем имя файла для сохранения
        output_filename = f"fault_roof_{counter}.jpg"
        output_path = os.path.join(output_folder, output_filename)

        # Масштабируем изображение до размера 640x640
        cropped_image = cropped_image.resize((640, 640))

        # Преобразуем изображение в режим RGB
        cropped_image = cropped_image.convert("RGB")

        # Сохраняем обрезанное изображение в формате JPEG
        cropped_image.save(output_path, format="JPEG")

        # Увеличиваем счетчик
        counter += 1

print("Обрезанные изображения сохранены в папке:", output_folder)


