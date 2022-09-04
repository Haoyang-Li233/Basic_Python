is_male = True

if is_male:
    print("123")
else:
    print("321")

is_tall = True

if is_male and is_tall:
    print(4321)
elif is_male and not(is_tall):
    print(2222)
elif not(is_male) and is_tall:
    print(3333)
else:
    print(4444)