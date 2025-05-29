# peek-cli

A simple, fast image, text files, zip and hex viewer.
![image](https://github.com/user-attachments/assets/438d01c2-03c3-4ca9-907e-695772754f80)

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
![image](https://github.com/user-attachments/assets/6615b14d-8d5e-4f02-9ea9-2553b077337c)

* Preview the first 5 lines of a text file:

  ```
  peek notes.txt --lines 5
  ```
![image](https://github.com/user-attachments/assets/377d8fdb-f375-4164-bbae-fb4b0b4e98cb)
* View contents of a zip:

  ```
  peek archive.zip
  ```
![image](https://github.com/user-attachments/assets/5f0a85fb-4225-4054-9bd6-7aefbba8a2da)
* Hex view of the first 20 lines in a text file:

  ```
  peek document.txt --hex --height 20
  ```

![image](https://github.com/user-attachments/assets/b35ef82c-b612-4932-bf76-a5fb024b3c0b)

## Todo
* Add markdown (.md) support
* Add support for pdfs, html pages
