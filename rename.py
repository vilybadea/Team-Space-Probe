import os


directory = r'E:\PROGRAMMING\HACKATHONS\MCGILL_PHYSICS_2020\SCRIPTS\augmented'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        base = os.path.splitext(filename)[0]
        os.rename(os.path.join(directory, filename), base + ".xml")
        print(filename)