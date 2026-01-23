import re
import os

# Đọc file index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm tất cả các slide-container
# Pattern để match từ <!-- SLIDE ... --> đến </div> kết thúc slide
slide_pattern = r'(<!-- SLIDE [^>]+-->.*?</div>\s*\n\s*)(?=<!-- SLIDE|<!-- ====|</body>)'
slides = re.findall(slide_pattern, content, re.DOTALL)

print(f"Tìm thấy {len(slides)} slides")

# Định nghĩa các section ranges
sections = {
    'section1.html': (3, 10),   # Slide 3-10: Cuộc cách mạng Mở
    'section2.html': (11, 14),  # Slide 11-14: Đặc tả Kỹ thuật
    'section3.html': (15, 19),  # Slide 15-19: Vi kiến trúc Pipeline
    'section4.html': (20, 23),  # Slide 20-23: Hệ thống & Đặc quyền
    'section5.html': (24, 27),  # Slide 24-27: Hệ sinh thái
}

# Tạo thư mục sections nếu chưa có
os.makedirs('sections', exist_ok=True)

# Ghi từng section
for filename, (start, end) in sections.items():
    section_content = ''
    for i, slide in enumerate(slides, start=1):
        if start <= i <= end:
            section_content += slide + '\n'
    
    if section_content:
        filepath = os.path.join('sections', filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(section_content)
        print(f"Đã tạo {filepath}")

print("Hoàn thành!")
