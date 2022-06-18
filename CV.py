import cv2


image_counter = 0
with open("image_counter.txt", "r") as F:
    image_counter = int(F.readline())




def num_img(num):
    if(int(num[2]) < 9):
        return num[0] + num[1] + str(int(num[2]) + 1)
    else:
        if(int(num[1]) < 9):
            return num[0] + str(int(num[1]) + 1) + "0"
        else:
            return str(int(num[0]) + 1) + "00"


def merge_channels(input_dir, output_dir):
    number_image = "000"
    def image_health(img_r, img_g, img_b):
        image = cv2.imread(img_r)
        image_r = cv2.imread(img_r)
        image_g = cv2.imread(img_g)
        image_b = cv2.imread(img_b)
        for i in range(len(image_r)):
            for j in range(len(image_r[i])):
                tim = [image_r[i][j], image_b[i][j], image_g[i][j]]
                image[i][j] = [image_b[i][j][0], image_g[i][j][1], image_r[i][j][2]]
                #print(image[i][j], end=" ")
            #print()
        return image

    for o in range(image_counter):
        number_image = num_img(number_image)
        new_file = "results/" + str(int(number_image)) + ".jpg"
        with open(new_file, "w"):
            pass
        r = f'data/00{number_image}_r.jpg'
        b = f'data/00{number_image}_b.jpg'
        g = f'data/00{number_image}_g.jpg'
        cv2.imwrite(new_file, image_health(r, g, b))

    




merge_channels("data", "results")
