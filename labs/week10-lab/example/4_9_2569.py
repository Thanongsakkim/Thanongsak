# === 1 ===
# เขียนโปรแกรม นับจำนวนอักขระที่สนใจในข้อความที่กำหนดโดยผู้ใช้
# 1. รับข้อความที่กำหนดให้จากผู้ใช้ (text)
# 2. รับอักขระที่สนใจจากผู้ใช้ (char)
# 3. แสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้าจอ

# ตัวอย่างหน้าจอ
# Insert the text: Kasetsart Sriracha
# Charcter to find: r
# 3 letters 'r' found in 'Kasetsart Sriracha'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
char = input("Character to find ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

# ==== 2 ====
# เขียนโปรแกรม ตรวจสอบความแข็งแรง password
# password ที่แข็งแรงคือ ยาวมากกว่า 8 ตัว และผสมกันะหว่างตัวเลข ตัวอักษร และอักขระพิเศษ

# ตัวอย่างหน้าจอ
# Insert your password: Test123
#Your password i not strong!

# Insert your password: Test1234;
# Your password is strong

password = input("Insert your password: ")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("Your password is strong!")
else:
    print("Your password is not strong!")