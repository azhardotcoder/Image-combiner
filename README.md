# Image Combiner

This script combines two images vertically into one image without compressing the image size. The width of both images should be the same. 

## Requirements

- Python 3.x
- Pillow library

## Installation

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Pillow**: Open your command prompt or terminal and install the Pillow library using pip:

    ```bash
    pip install pillow
    ```

## Usage

1. **Save the Script**: Save the provided Python code in a file named `combine_images.py`.

2. **Prepare Images**: Place your images (`img1.jpg` and `img2.jpg`) in the same directory where you saved the script.

3. **Specify Paths**: Open `combine_images.py` in a text editor and replace the placeholder paths with the actual paths to your images and the desired output path.

    ```python
    image1_path = os.path.join('C:\\Users\\YourUsername\\Desktop\\images', 'img1.jpg')
    image2_path = os.path.join('C:\\Users\\YourUsername\\Desktop\\images', 'img2.jpg')
    output_path = os.path.join('C:\\Users\\YourUsername\\Desktop\\images', 'combined_image.jpg')
    ```

4. **Run the Script**:

    - **Windows**:
      - Open Command Prompt.
      - Navigate to the directory where you saved `combine_images.py`:

        ```bash
        cd C:\path\to\your\folder
        ```
      - Run the script:

        ```bash
        python combine_images.py
        ```

    - **macOS/Linux**:
      - Open Terminal.
      - Navigate to the directory where you saved `combine_images.py`:

        ```bash
        cd /path/to/your/folder
        ```
      - Run the script:

        ```bash
        python3 combine_images.py
        ```

## Example

If your images are in a folder named `images` on your desktop, your paths in the script might look like this:

```python
image1_path = os.path.join('C:\\Users\\YourUsername\\Desktop\\images', 'img1.jpg')
image2_path = os.path.join('C:\\Users\\YourUsername\\Desktop\\images', 'img2.jpg')
output_path = os.path.join('C:\\Users\\YourUsername\\Desktop\\images', 'combined_image.jpg')
