# Lane detection algorithm using python

### Prerequisites to run this algorithm:

1. Python installed in your computer ([click here](https://www.python.org/downloads/) for more information)
2. OpenCV library installed ([click here](https://pypi.org/project/opencv-python/) for more information)
3. Numpy library installed ([click here](https://numpy.org/install/) for more information)

## What does the algorithm do?

1. An image is loaded _(this can be a frame from a camera mounted on a car)_.
2. The image is transformed to grayscale.
3. The image is blurred. This is done to lower the image's details for a more effective edge detection later.
4. A mask is created and applied to the image in order to keep only the part of the image that contains the lane information we need.
5. The edges of the image are detected.
6. The lines that create these edges are detected and transformed in mathematical lines.
7. A mask is created and applied to the lines in order to keep only the part of them we are going to use.
8. The original frame is combined with the detected lines in a final image that is shown.

_(There are comments in the python script explaining every step)_

## How to run the algorithm

1. Clone the repository in your system using

```bash
git clone https://github.com/giannisgkountras/lane-detection.git
```

2. Open the created folder using

```bash
cd lane-detection
```

3. Run `main.py` using

```bash
python main.py
```

or

```bash
python3 main.py
```

based on your python installation.

You can press any key to view the next image.

_Any suggestions or improvements are welcome._
