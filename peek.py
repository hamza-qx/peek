import argparse
from PIL import Image
from os import path
import zipfile

def resize(image, new_height, g=1): # if whoever reads this is smart add dithering/sharpening
    width, height = image.size
    aspect_ratio = width / height
    new_width = int(new_height * aspect_ratio)
    return image.resize((int(new_width), int(new_height * g)))

def grayscale(r, g, b):
    return (0.299*r*r + 0.587*g*g + 0.114*g*b) ** 0.5 # adjust for green cones in eyes

def file_data(file_path):
    size = path.getsize(file_path)
    units = ['bytes', 'kb', 'mb', 'GB', 'TB']
    unit_index = 0

    while size >= 512 and unit_index < len(units) - 1: # no less then 0.5 of one unit
        size /= 1024.0
        unit_index += 1

    unit = units[unit_index]
    size_str = f"{size:.2f}"

    return (
        f"\033[1;33m[/]\033[0m {file_path}  " # shoutout to chatgpt for these terrible ansi codes
        f"\033[1;32m[*]\033[0m {size_str} {unit}\n"
        "\033[1;90m" + "═" * 44 + "\033[0m\n"
    )

def peek(image_path, height=46):
    try:
        image = Image.open(image_path).convert("RGBA")
    except Exception as e:
        return str(e)

    image = resize(image, height)
    pixels = image.load()
    w, h = image.size
    result = []

    for y in range(0, h - 1, 2):
        row = ""
        for x in range(w):
            r1, g1, b1, a1 = pixels[x, y]
            r2, g2, b2, a2 = pixels[x, y + 1]

            char = " "
            ansi = ""

            top_visible = a1 > 127
            bottom_visible = a2 > 127

            if top_visible and bottom_visible:
                ansi += f"\033[38;2;{r1};{g1};{b1}m"
                ansi += f"\033[48;2;{r2};{g2};{b2}m"
                char = "▀"
            elif top_visible:
                ansi += f"\033[38;2;{r1};{g1};{b1}m"
                ansi += "\033[49m"
                char = "▀"
            elif bottom_visible:
                ansi += f"\033[38;2;{r2};{g2};{b2}m"
                ansi += "\033[49m"
                char = "▄"
            else:
                ansi += "\033[0m"
                char = " "

            row += f"{ansi}{char}"

        row += "\033[0m"  # these ansi escape codes suck
        result.append(row)

    return file_data(image_path) + "\n".join(result)

def peektxt(file_path, x=20):
    try:
        with open(file_path, 'r') as file:
            output = ''
            lines = file.readlines()
            total = len(lines)

            for i in range(min(x, total)):
                output += lines[i]

            return file_data(file_path) + output + (f"\n... \n{max(0, total - x)} more lines")
    
    except Exception as e:
        return e

def peek_zip(zip_path, height=20):
    output = file_data(zip_path)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            names = zf.namelist()
            names = names[:min(len(names), height)]

            for name in names:
                output += f"\033[1;34m[*]\033[0m {name}\n"
                
        return output
    except Exception as e:
        return e

def peek_hex(file_path, height, width=16):
    lines = []
    with open(file_path, 'rb') as f:
        offset = 0
        while True:
            chunk = f.read(width)
            if not chunk or len(lines) > height:
                break

            bytes = [f"{b:02x}" for b in chunk]

            if len(bytes) < width:
                bytes += ["  "] * (width - len(bytes))

            half = width // 2
            left = " ".join(bytes[:half])
            right = " ".join(bytes[half:])
            hex_part = f"{left}  {right}"

            ascii_part = "".join((chr(b) if 32 <= b < 127 else ".") for b in chunk)

            lines.append(f"{offset:08x}: {hex_part}  |{ascii_part}|")

            offset += width

    return file_data(file_path) + "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "file_path",
        help="— what do you think..?"
    )

    parser.add_argument(
        "height0",
        nargs="?",
        type=int,
        help="— identical to --height or --lines but doesnt require a flag."
    )

    parser.add_argument(
        "--height", "--lines", "-l",
        type=int,
        help="— resolution to resize image to in pixels (1 char = 2 vertical pixels)"
    )

    parser.add_argument(
        "--hex",
        action="store_true",
        help="— views file by bytes with hexadecimal"
    )

    args = parser.parse_args()

    ext = path.splitext(args.file_path)[1]
    output = ''

    height = args.height0 or args.height or 20 # so that u can do peek image.png 40 & peek image.png --height 50
    
    if args.hex:
        output = peek_hex(
            args.file_path,
            height
        )

    elif ext in [".png", ".jpeg", ".jpg"]:
        output = peek(
                args.file_path,
                height if height != 20 else 46,
        )

    elif ext == ".zip":
        output = peek_zip(
            args.file_path,
            height,
        )
    
    else: 
        output = peektxt(
            args.file_path, # doubles as lines to show
            height
        )

    if isinstance(output, Exception):
        print(f"\x1b[1;31mu did something you useless idiot;\n\033[0m{output}")
    else :
        print(output)

if __name__ == "__main__":
    main()