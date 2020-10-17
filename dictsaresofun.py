user = "gin"


# option 1
map = {"gin": "hi gin",
       "akashi": "shameful display",
       "galford": "probably late",
       "khona": "glaring"}
print(map[user])

# option 2
if user == "gin":
    print("hi gin")
elif user == "akashi":
    print("shameful display")
elif user == "galford":
    print("probably late")
else:
    print("glaring")


