import os

directory = r'E:\PROGRAMMING\HACKATHONS\MCGILL_PHYSICS_2020\SCRIPTS\augmented'

for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        os.rename(os.path.join(directory, filename), os.path.join(directory + r'\archive', filename))
