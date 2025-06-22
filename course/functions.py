def laugh():
    print("MUAHAHAHAHA!! :D")

def cry():
    print("WAAA!! TT_TT")      

def multiplier(func, repeats):
    for i in range(repeats):
        func()

multiplier(laugh, 5)
multiplier(cry, 2)

def enroll(*courses): 
    print(type(courses))  # <class 'tuple'>
    for course in courses: 
        print(course)

enroll("Probabilistic Inference", "Introduction to Machine Learning",
    "Computer Vision", "Graphics")

"""
def customise_page(**kwargs):
    parse_args(kwargs)

def parse_args(options):
    for key, value in options.items():
        if key == "background":
            set_background(value)
        elif key == "width":
            set_width(value)
        elif key == "avatar":
            set_avatar(value)
        else:
            print(f"Unknown keyword {key}.")
            return

customise_page(background="red", width=500, avatar="selfie.jpg")

"""

