# peek-cli

A simple, fast images, text files, and hex viewer.
![image](https://github.com/user-attachments/assets/cad28fc5-e9c3-459c-8d02-3248756598d3)

## Usage
```
peek <file> [height] [options] 
```

* `<file>`
  Path to a `.zip`, `.jpeg`/`.jpg`, `.png`, or `.txt` file (or any file to view as raw hex bytes).

* `[height]`
  When previewing an image: the vertical height in pixels.
  When previewing text or hex: the number of lines to display.

## Supported Formats

* **Images**: `.jpeg`, `.jpg`, `.png`
* **Archives**: `.zip`
* **Text**: `.txt`
* **Any other file**: viewed as raw hexadecimal bytes

## Options

| Option                      | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ |
| `-h`, `--help`              | Show help/usage information.                                                   |
| `--height`, `--lines`, `-l` | Set vertical size (in pixels) for images, or # of lines for text/hex output.   |
| `--hex`                     | View file in hex.                                                              |

## Examples

* Show help:

  ```
  peek -h
  ```
* Preview a PNG image at 40 px height:

  ```
  peek image.png 40
  ```
* Preview the first 30 lines of a text file:

  ```
  peek notes.txt --lines 30
  ```
* Same as above but using `--height`:

  ```
  peek image.png --height 40
  ```
* View contents of a zip:

  ```
  peek archive.zip
  ```
* Force hex view of a text file:

  ```
  peek document.txt --hex
  ```

## Todo
* Add markdown (.md) support
* add better image processing (bicubic interpolation, dithering)
