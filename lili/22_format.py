gpa_dict = {"大姥":3.859, "小王":3.416, "小李":3.213}
for name in gpa_dict:
    gpa = gpa_dict[name]
    print("{0} 你好， 你当前的绩点为:{1: .2f}". format(name , gpa))
