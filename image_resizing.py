from PIL import Image, ImageFilter

# 이미지 불러오기
input_path = "SK_ons_logo-011.png"
output_path = "optimized_logo.png"

# 이미지 열기
image = Image.open(input_path)

# 이미지 크기를 50%로 줄이기
new_width = int(image.width * 0.25)
new_height = int(image.height * 0.25)
resized_image = image.resize((new_width, new_height), Image.LANCZOS)

# 선명도 향상 필터 적용
sharpened_image = resized_image.filter(ImageFilter.SHARPEN)

# 최적화된 이미지 저장
sharpened_image.save(output_path, format="PNG", optimize=True)
