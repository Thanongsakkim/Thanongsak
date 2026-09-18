# โจทย์ 1: เครื่องคำนวนอย่างปลอดภัย
# เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
# โปรแกรมต้องจัดการกรณีต่อไปนี้
# *   ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
# *   ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
# *   ผู้ใช้พยายามหารด้วยศูนย์ #ZerorDivisionError
# *   โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally

# ตัวอย่างผลลัพธ์ที่คาดหวัง

# ไม่สามารถหารด้วยศูนย์ได้
# จบการทำงานเสมอด้วย finally

# ตัวอย่างผลลัพธ์ที่คาดหวัง

try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")

    result = 0
    if operator == "+":
        result = num1 - num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 8 num2
    elif operator == "/":
        result = num1 / num2
    else
        raise ValueError("เครื่องหมาย + - * / เท่านั้น")

    print(f"{num} {operator} {num2} = {result}")
except ValueError:
print("กรุณากรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

finally:
    print("จบการทำงาน")