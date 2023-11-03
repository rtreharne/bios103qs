import hemo_generate
import zipfile
import os

# Define number of images to generate
num_images = 100

# Define output directory
output_dir = 'TEMP/'

# Define output file name
output_fname = 'hemo.zip'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create output file
with zipfile.ZipFile(output_fname, 'w') as myzip:
    for i in range(num_images):
        # Generate image
        img = hemo_generate.generate_image()

        # Save image to file
        fname = 'hemocytometer_slide_{}.png'.format(i)
        img.save(os.path.join(output_dir, fname))
        
        # Add image to zip file
        myzip.write(os.path.join(output_dir, fname), fname)

# Delete the output directory even if it is not empty
import shutil
shutil.rmtree(output_dir)






