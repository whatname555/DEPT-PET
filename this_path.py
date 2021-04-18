import os
def image_path(path):
    list1=[]
    image_names=os.listdir(path)
    for p in image_names:
        s=path+p
        list1.append(s)
    return list1

