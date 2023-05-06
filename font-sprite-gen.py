import os
import time
import argparse
from halo import Halo
from PIL import Image, ImageDraw, ImageFont, ImageChops

parser = argparse.ArgumentParser(description='Generate sprite sheet of font characters')
parser.add_argument('font', type=str, help='path to font file')
parser.add_argument('--size', type=int, default=16, help='font size (default: 16)')
parser.add_argument('--spacing', type=int, default=1, help='spacing between characters (default: 1)')
parser.add_argument('--width', type=int, default=1024, help='image width (default: 512)')
parser.add_argument('--height', type=int, default=1024, help='image height (default: 512)')
args = parser.parse_args()

font_path = args.font
font_size = args.size
spacing = args.spacing
img_width = args.width
img_height = args.height
full_cycle = 143000  #Possible number of ASCII table indexes

text = "   ___                _    __               _  _            ___\n" \
       "  / __\\  ___   _ __  | |_ / _\\ _ __   _ __ (_)| |_   ___   / _ \\  ___  _ __  \n" \
       " / _\\   / _ \\ | '_ \\ | __|\\ \\ | '_ \\ | '__|| || __| / _ \\ / /_\\/ / _ \\| '_ \\ \n" \
       "/ /    | (_) || | | || |_ _\\ \\| |_) || |   | || |_ |  __// /_\\\\ |  __/| | | |\n" \
       "\\/      \\___/ |_| |_| \\__|\\__/| .__/ |_|   |_| \\__| \\___|\\____/  \\___||_| |_|\n" \
       "                              |_|                                            "

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.001)

font = ImageFont.truetype(font_path, font_size)
font_name = os.path.splitext(os.path.basename(font_path))[0]

def is_same_image(img1, img2):
    diff = ImageChops.difference(img1, img2)
    return not diff.getbbox()

img = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

x, y = 0, 0
symbols_count = 0

# Create an image of the first character for comparison
first_char_img = Image.new('RGBA', (font_size, font_size), (0, 0, 0, 0))
first_draw = ImageDraw.Draw(first_char_img)
first_char = chr(0)
first_draw.text((0, 0), first_char, font=font, fill=(255, 255, 255, 255))

spinner = Halo(text='Generate 0%', spinner='dots', color='magenta', text_color='cyan')
for i in range(1, full_cycle):
    char = chr(i)
    char_img = Image.new('RGBA', (font_size, font_size), (0, 0, 0, 0))
    char_draw = ImageDraw.Draw(char_img)
    char_draw.text((0, 0), char, font=font, fill=(255, 255, 255, 255))

    if not is_same_image(first_char_img, char_img):
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width, char_height = bbox[2], bbox[3]
        draw.text((x, y), char, font=font, fill=(255, 255, 255, 255))
        symbols_count += 1
        x += char_width + spacing
    else:
        bbox = font.getbbox(char)
        char_width, char_height = bbox[2], bbox[3]

    if x + char_width > img_width:
        x = 0
        y += char_height + spacing

    spinner.text = f'Generate sprite-sheet {i/full_cycle*100:.0f}%'
    spinner.start()

output_filename = f'sprite-{font_name}.png'
img.save(output_filename)

spinner.succeed(f"Done!. Filename: {output_filename}. Find symbols: {symbols_count}")
spinner.stop()
