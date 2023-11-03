import random
from PIL import Image, ImageDraw, ImageFilter
from PIL import Image, ImageDraw, ImageFilter


def generate_image(fname='hemocytometer_slide.png'):
    # Define image size
    width = 1000
    height = 1000
    
    # Define number of circles
    num_circles = random.randint(100, 300)
    
    # Define radius of circles
    r = 5
    
    # Define percentage of circles with blue outline
    x = random.randint(5, 20)
    
    # Create image
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw circles
    centers = []
    for i in range(num_circles):
        # Define circle center
        while True:
            x_center = random.randint(r, width-r)
            y_center = random.randint(r, height-r)
            overlap = False
            for center in centers:
                if (x_center - center[0])**2 + (y_center - center[1])**2 < (2*r)**2:
                    overlap = True
                    break
            if not overlap:
                centers.append((x_center, y_center))
                break
        
        # Define circle outline color
        outline_color = 'blue' if random.random() < x/100 else 'black'
        fill_color = 'blue' if outline_color == 'blue' else 'white'
        
        draw.ellipse((x_center-r, y_center-r, x_center+r, y_center+r), fill=fill_color, outline=outline_color, width=3)


    # Overlay grid, very very light gray
    major_grid_color = 'lightgray'
    minor_grid_color = 'lightgray'

    # I want 9 major grids
    major_grid_spacing = width // 3
    
    # I want 4 minor grids per major grid
    minor_grid_spacing = width // 12

    # Draw major grid
    for i in range(0, width, major_grid_spacing):
        draw.line((i, 0, i, height), fill=major_grid_color, width=1)
        draw.line((0, i, width, i), fill=major_grid_color, width=1)

    # Draw minor grid
    for i in range(0, width, minor_grid_spacing):
        draw.line((i, 0, i, height), fill=minor_grid_color, width=1)
        draw.line((0, i, width, i), fill=minor_grid_color, width=1)





    # Save image
    img.save(fname)


if __name__ == '__main__':
    generate_image()

