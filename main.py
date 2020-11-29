import png

width = 540
height = 960
img = []

raw_dataset_5 = open('DS5.txt', 'r')
dataset_5 = raw_dataset_5.readlines()
for num_row in range(len(dataset_5)):
    dataset_5[num_row] = dataset_5[num_row].replace('\n', '')
    dataset_5[num_row] = dataset_5[num_row].split(' ')


for y in range(height):
    row = []
    for x in range(width):
        row += (255, 255, 255)
    img.append(row)

for ds_list in dataset_5:
    px_x = int(ds_list[0])
    px_y = int(ds_list[1])
    img[px_y][px_x*3-1] = 0
    img[px_y][px_x * 3] = 0
    img[px_y][px_x * 3 + 1] = 0

with open('lab2.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)
f.close()
