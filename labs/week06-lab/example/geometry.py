# คำนวนสามเหลี่ยม
def calculate_triangle_area(hight, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * hight * base
    print(f"Rectangle with hight {hight} and base {base}")
    print(f"Area = {hight} × {base} = {area}")
    print()

print("Calculating Triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

# จากตัวอย่างให้สร้าง function สำหรับคำนวนพื่นที่วงกลม
def calculate_circle_area(ray):
    """Calculates and displays circle area"""
    area = 3.14 * (ray * ray)
    print(f"circle with ray {ray}")
    print(f"Area = {3.14} × {ray} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(50)
calculate_circle_area(30)

# จากตัวอย่างด้านบน ให้เขียน funtion ชื่อ squara_root(n):
def square_root(n):
    """Returns the square of a number"""
    return n ** 0.5

print(f"square root of 25 =", square_root(25))
print()