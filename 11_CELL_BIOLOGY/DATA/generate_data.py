import os
import shutil
import zipfile
import hemo_generate
import numpy as np

def generate_hemo_data(num_images=100, output_dir='TEMP/', output_fname='hemo.zip', mean=100, std=10):
    """
    Generates hemo data and saves it to a zip file.
    
    Parameters:
    num_images (int): The number of images to generate.
    output_dir (str): The output directory to save the images and zip file.
    output_fname (str): The name of the output zip file.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create output file
    with zipfile.ZipFile(output_fname, 'w') as myzip:
        for i in range(num_images):
            # Generate image
            img = hemo_generate.generate_image(mean=mean, std=std)

            # Save image to file
            fname = 'hemocytometer_slide_{}.png'.format(i)
            img.save(os.path.join(output_dir, fname))

            # Add image to zip file
            myzip.write(os.path.join(output_dir, fname), fname)

    # Delete the output directory even if it is not empty
    shutil.rmtree(output_dir)

if __name__ == '__main__':
    means = np.linspace(100,299, 100)
    np.random.shuffle(means)

    sds = np.linspace(10, 29, 100)
    np.random.shuffle(sds)

    for i, (mean, sd) in enumerate(zip(means, sds)):
        print(i+100, 'Generating data for mean: {}, sd: {}'.format(mean, sd))
        generate_hemo_data(output_fname='hemo_{}.zip'.format(i+100), mean=mean, std=sd)
    






