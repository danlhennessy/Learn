import time

image3 = (".gif", ".jpg", ".png")
image4 = "jpeg"
app = (".pdf", ".txt", ".zip")
# else application/octet-stream

def extensions(file):
    if file.endswith(image3):
        print(f"image/{file[-3:]}")
    elif file.endswith(image4):
        print(f"image/{file[-4:]}")
    elif file.endswith(app):
        print(f"application/{file[-3:]}")
    else:
        return("application/octet-stream")

t1 = time.perf_counter()
extensions('cat.jpeg')
t2 = time.perf_counter()

print(t2-t1)