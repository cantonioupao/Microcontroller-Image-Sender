# Microcontroller-Image-Sender
Introducing a simple Python GUI to resize and send via serial images to microcontrollers

![GUI of the sender](/asset/screenshot_main2.jpg)

## How to use
To use this tool you have to install the packages in requirement.txt (you can do that via `pip install -r requirements.txt`) and then run `python Serial_Image_Sender_GUI.py`. The GUI will open and you can access all the functionalities of the program without a single line of code.

Done that, you should just click Connect! If the button turns green it means that the connection has been established and that images can be sent. Just click on _Next image_ or _Berserk mode_ to send one image or to continously send imges one after another!

## What should I input?

The GUI only requires a path to the test images folder and the COM port of the microcontroller.
Additionally, you can provide:
* The ground truth values: the file should contain in the first line the classes values separated by comma and then class numbers every new line
* Image annotations: some datasets provide X and Y coordinates of the most important part of an image. The sender can understand from this file those positions and crop accordingly the image. The file format should be x1,y1,x2,y2, with each entry separated by a new line.In Face Detection the bounding box coordinates can be given for the ground truth of an image
* Image resizing: you can resize the image to the entered pixel values. In case you don't want to resize the image please enter -1 in at least one of the resize boxes

## What should I send via serial?

The program expect the following input data in this order:
* Uint8_t for the class number
* Float_32 for the inference accuracy
* Uint32_t for the cycle count
* Uint16_t for the bounding box left pixel coordinate
* Uint16_t for the bounding box top pixel coordinate
* Uint16_t for the bounding box width
* Uint16_t for the bounding box height

## Expected Bounding Box format 
For Bounding Box coordinates the received format is 
**[left,top, width , height]** for the bounding box.Then the bounding box starting point is calculated according to 
**(x1,y1)=(left,top)** and the ending point of the bounding box is 
**(x2,y2)=(left+width,top+height)** 
The calculations and rectangle display are handled automatically by the application. A red rectangle is displayed on the image, representing the predicted face region from the face detection inference for the current input image



Credits to  **Marco Giordano** for sharing his code. Some slight modifications have taken place on the code to account for Face Detection
