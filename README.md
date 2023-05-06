<p align="left">
  <img src="./resouces/FontSpriteGen.png" width="128" alt="# FontSpriteGen Icon">
</p>

# FontSpriteGen
<pre>
   ___                _    __               _  _            ___
  / __\  ___   _ __  | |_ / _\ _ __   _ __ (_)| |_   ___   / _ \  ___  _ __  
 / _\   / _ \ | '_ \ | __|\ \ | '_ \ | '__|| || __| / _ \ / /_\/ / _ \| '_ \ 
/ /    | (_) || | | || |_ _\ \| |_) || |   | || |_ |  __// /_\\ |  __/| | | |
\/      \___/ |_| |_| \__|\__/| .__/ |_|   |_| \__| \___|\____/  \___||_| |_|
</pre>


FontSpriteGen is a simple Python tool for generating sprite sheets from TTF font.

## Installation

1. Make sure you have Python 3.7 or higher installed. If not, download and install it from the [official website](https://www.python.org/downloads/).

2. Install the Pillow library:
```bash
python -m pip install Pillow==9.0.0 Halo --user
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/vladgohn/FontSpriteGen.git
```

2. Go to the project folder:
```bash
cd FontSpriteGen
```

3. Run the script and specify the font file path:
```bash
python font-sprite-gen.py font.ttf [--size SIZE] [--spacing SPACING] [--width WIDTH] [--height HEIGHT]
```

## Example
To generate a sprite sheet from the `font.ttf` font with default settings, run:
```bash
python font-sprite-gen.py font.ttf
```
This will create a file named `sprite-font.png` in the same directory.

To get a list of available options, you can use the command:
```bash
python font-sprite-gen.py --help
```
```bash
usage: font-sprite-gen.py [-h] [--size SIZE] [--spacing SPACING]
                          [--width WIDTH] [--height HEIGHT]
                          font

Generate sprite sheet of font characters

positional arguments:
  font                  path to font file

optional arguments:
  -h, --help            show this help message and exit
  --size SIZE, -s SIZE  font size (default: 16)
  --spacing SPACING, -sp SPACING
                        spacing between characters (default: 1)
  --width WIDTH, -w WIDTH
                        image width (default: 512)
  --height HEIGHT, -h HEIGHT
                        image height (default: 512)
```

## Output
The tool generates a sprite sheet image with all characters from the font. The output file name is `sprite-<font_name>.png`, where `<font_name>` is the name of the font file without the extension.

The tool also outputs the number of characters found in the font.

Enjoy!


Creation of the project: **Vlad Gohn**. Support: GPT-4 by OpenAI. <img width="16" height="16" src="./resouces/GPT4.svg">

## License
This project is available under the [MIT License](./LICENSE).