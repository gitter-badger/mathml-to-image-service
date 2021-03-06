import os
import subprocess
import uuid


def to_image(svg_string, image_format, max_size):
    if max_size > 1000:
        raise NameError("max_size is too big. Max of 1000px.")

    tmp_file_name = '%s.svg' % uuid.uuid4().hex

    svg_file = open(tmp_file_name, 'w', encoding='utf-8')
    svg_file.write(svg_string)
    svg_file.close()

    if image_format.upper() == 'PNG':
        extention = '.png'
    elif image_format.upper() == 'GIF':
        extention = '.gif'
    else:
        raise NameError(
            'Unsupported output file format - "GIF" and "PNG" only.')

    png_filename = "%s.png" % (uuid.uuid4().hex)
    filename = "%s%s" % (uuid.uuid4().hex, extention)
   
    subprocess.check_call(
        ['rsvg-convert', tmp_file_name, '-w',
         '%s' % (max_size,),'--background-color','white','-o', png_filename], stderr=subprocess.DEVNULL)

    if image_format.upper() == 'GIF':
        subprocess.check_call(
            ['convert', png_filename, filename], stderr=subprocess.DEVNULL)

        os.remove(tmp_file_name)
        os.remove(png_filename)
        return filename
    
    else:
        os.remove(tmp_file_name)
        return png_filename
        
    #TODO: implement pngcrush -bit_depth 1 foo4.png foo5.png

def main():
    svg_string = open('example.svg', 'r', encoding='utf-8').read()
    print (to_image(svg_string, 'PNG', 300))


if __name__ == '__main__':
    main()
