
# first task I'm going to do is create the color blind types 
# and give mark them with commeted commets to describe what easle needs to be done
# as luck we are "treding down a path that's been walked before" 
# https://gist.github.com/Lokno/df7c3bfdc9ad32558bb7 


#_____________________________Divide on section______________________________________
# Above section ofOld stuff like reserarch, code/ testing area was removed

# same as what we did in the early days of class. I much prefer this way, as I understand it. 
from final_project import images
from PIL import Image

# Protanopia - reduced sensitivity to red light
def protanopia(pixel):
    r, g, b = pixel
    r_new = r // 2         
    g_new = g              
    b_new = min(255, b + 50)  
    return (r_new, g_new, b_new)

# Deuteranopia - reduced sensitivity to green light
def deuteranopia(pixel):
    r, g, b = pixel
    r_new = r
    g_new = g // 2         
    b_new = min(255, b + 50)  
    return (r_new, g_new, b_new)

# Tritanopia - reduced sensitivity to blue light
def tritanopia(pixel):
    r, g, b = pixel
    r_new = min(255, r + 50)  
    g_new = g
    b_new = b // 2         
    return (r_new, g_new, b_new)

# Achromatopsia - total color blindness (grayscale)
def achromatopsia(pixel):
    r, g, b = pixel
    avg = (r + g + b) // 3   
    return (avg, avg, avg)

# "image_path" will need to change to point to the direction of where image is located.
# and where those image is is the website we look/ point at to gather that image data.

def apply_filter(image_path, filter_name, transform_fn):
    im = Image.open(image_path)
    new_pixels = map(transform_fn, im.getdata())
    im.putdata(list(new_pixels))

    base, ext = os.path.splitext(image_path)

    # "output_image" image will need to be put back in or automaticly display the image when the use selects and "enters" 
    # what color view they want.
    output_image = f"{base}_{filter_name}{ext}"
    im.save(output_image)
    print(f"Saved: {output_image}")


# "walk.jpg" is being used as a stand-in while figure out on how to intergrate our filters on our inteted target.
def use():
    for i in range(0, 1, len(images)):
        image_file = images[i]
        apply_filter(image_file, "protanopia", protanopia)
        apply_filter(image_file, "deuteranopia", deuteranopia)
        apply_filter(image_file, "tritanopia", tritanopia)
        apply_filter(image_file, "achromatopsia", achromatopsia)