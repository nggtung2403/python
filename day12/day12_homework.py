import random 
import string

def random_user_id():
    character = string.ascii_letters + string.digits
    return "".join(random.choices(character,k=6))
print(random_user_id())

def random_user_id2():
    cha = string.ascii_letters + string.digits
    return "".join(random.choices(cha,k=10))
print(random_user_id2())

def user_id_gen_by_user():
    cha = string.ascii_letters + string.digits
    n = int(input("nhap n: "))
    m = int(input("nhap m:"))
    for i in range(m):
        print("".join(random.choices(cha,k=n)))
    
user_id_gen_by_user()

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rbg({r},{g},{b})"
print(rgb_color_gen())

def list_of_hexa_colors(number_of_colors = 6):
    chars = string.hexdigits[:16]
    colors = []
    for _ in range(number_of_colors):
        color = "#" + "".join(random.choices(chars,k=6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(6))

def list_of_rgb_colors(number_of_colors = 1):
    colors = []
    for _ in range(number_of_colors):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        colors.append(f"rbg({r},{g},{b})")
    return colors
print(list_of_rgb_colors(3))

def generate_colors(color_type,count):
    if color_type == "hexa":
        chars = string.hexdigits[:16]
        colors = []
        for _ in range(count):
            color = "#" + "".join(random.choices(chars,k=6))
            colors.append(color)
        return colors
    elif color_type == "rbg":
        colors = []
        for _ in range(count):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            colors.append(f"rbg({r},{g},{b})")
        return colors
    else:
        return "Ko hop le"

print(generate_colors("hexa",3))
print(generate_colors("hexa",1))
print(generate_colors("rbg",3))
print(generate_colors("rbg",1))

def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled
numbers = [1,2,3,4,5,6,7]
print(shuffle_list(numbers))

def seven_random_numbers():
    return random.sample(range(10),7)
print(seven_random_numbers())