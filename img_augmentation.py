from keras.preprocessing.image import ImageDataGenerator
from skimage import io
import os

datagen = ImageDataGenerator(rotation_range=45,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='reflect', cval=125)

#for i in range(8,26):
#   x = io.imread(f'000008.jpg')
#   x = x.reshape((1, ) + x.shape)

directory = r'E:\PROGRAMMING\HACKATHONS\MCGILL_PHYSICS_2020\IMAGES'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(filename)
        x = io.imread(os.path.join(directory, filename))
        x = x.reshape((1, ) + x.shape)
    j = 0
    for batch in datagen.flow(x, batch_size=16,
                            save_to_dir='augmented',
                            save_prefix='aug',
                            save_format='jpg'):
        j += 1
        if j > 20:
            break
