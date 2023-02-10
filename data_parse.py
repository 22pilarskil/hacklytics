import os
import shutil
from PIL import Image

print(os.getcwd())
lines = []

dataset_path = 'UECFOOD100'

with open('{}/category.txt'.format(dataset_path)) as f:
    f.readline()
    while True:
        line = f.readline().split()
        if line == []: break
        line[1] = " ".join([component for component in line[1:]])
        line = [line[0], line[1]]
        lines.append(line)
print(lines)

shutil.rmtree('dataset')

image_dir = 'dataset/images'
labels_dir = 'dataset/labels'

os.mkdir("dataset")
os.mkdir(image_dir)
os.mkdir(labels_dir)


files = os.listdir('{}'.format(dataset_path))
for file in files:

    if (file.isdigit()):
        print(file)
        img_files = os.listdir('{}/{}'.format(dataset_path, file))
        bb_data = {}
        with open('{}/{}/bb_info.txt'.format(dataset_path, file)) as f:
            f.readline()
            while True:
                line = f.readline().split()
                if line == []: break
                bb_data[line[0]] = [int(data) for data in line[1:]]


        for img_file in img_files:
            img_id = img_file[:-4]
            if (img_id.isdigit()):
                shutil.copyfile('{}/{}/{}'.format(dataset_path, file, img_file), '{}/{}'.format(image_dir, img_file))
                img = Image.open('{}/{}/{}'.format(dataset_path, file, img_file))
                points = bb_data[img_id]
                label_file = open("{}/{}".format(labels_dir, img_id + ".txt"), "w+")
                x_center = (points[0] + (points[2] - points[0]) / 2) / img.width
                y_center = (points[1] + (points[3] - points[1]) / 2) / img.height
                x_width = (points[2] - points[0]) / img.width
                y_width = (points[3] - points[1]) / img.height
                label_file.write('{} {} {} {} {}'.format(int(file) - 1, x_center, y_center, x_width, y_width))
                


                
