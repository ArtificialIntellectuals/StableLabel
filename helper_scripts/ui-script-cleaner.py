import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from typing import Union, Callable


class ImageUI:
    """
    Class to create a user interface (UI) that displays images from a folder and allows moving them to different folders.

    Attributes:
    - root: tk.Tk
        The root window of the UI.
    - image_folder: str
        The path to the folder containing the images.
    - left_folder: str
        The path to the folder where the image will be moved when the left button is clicked.
    - right_folder: str
        The path to the folder where the image will be moved when the right button is clicked.
    - image_list: list
        A list of image file names in the image folder.
    - current_image_index: int
        The index of the currently displayed image in the image list.
    - image_label: tk.Label
        The label widget to display the image.
    """

    def __init__(self, image_folder: str):
        """
        Constructor to instantiate the ImageUI class.

        Parameters:
        - image_folder: str
            The path to the folder containing the images.
        """
        # Create folders if not yet existing
        mismatch_folder = image_folder + "/pollution"
        correct_folder = image_folder + "/clean"
        unsure_folder = image_folder + "/unsure"
        for folder in [mismatch_folder, correct_folder, unsure_folder]:
            if not os.path.exists(folder):
                os.mkdir(folder)

        # Creating the root window
        self.root = tk.Tk()

        # Setting the title of the window
        self.root.title("Image UI")

        # Setting the size of the window
        self.root.geometry("500x400")

        # Setting the image folder, left folder, and right folder
        self.image_folder = image_folder

        # Getting the list of image file names in the image folder
        self.image_list = wrapper_for_error_handling(function=self.get_image_list)

        # Initializing the current image index to 0
        self.current_image_index = 0

        # Creating the image label widget
        self.image_label = tk.Label(self.root)

        # Displaying the first image
        self.display_image()

        # Creating the left and right buttons
        left_button = tk.Button(self.root, text="Mismatch (Left)", command=lambda: wrapper_for_error_handling(function=self.move, params=[mismatch_folder]))
        right_button = tk.Button(self.root, text="Dog (Right)", command=lambda: wrapper_for_error_handling(function=self.move, params=[correct_folder]))
        unsure_button = tk.Button(self.root, text="Unsure (Down)", command=lambda: wrapper_for_error_handling(function=self.move, params=[unsure_folder]))

        # Placing the image label and buttons in the window
        self.image_label.pack()
        left_button.pack(side=tk.LEFT)
        right_button.pack(side=tk.RIGHT)
        unsure_button.pack(side=tk.BOTTOM)

        # Adding keyboard shortcuts for buttons
        self.root.bind("<Left>", lambda event: self.move(mismatch_folder))
        self.root.bind("<Right>", lambda event: self.move(correct_folder))
        self.root.bind("<Down>", lambda event: self.move(unsure_folder))

        # Running the main event loop
        self.root.mainloop()

    def get_image_list(self):
        """
        Retrieves the list of image file names in the image folder.

        Returns:
        - list:
            A list of image file names.
        """

        # Getting the list of files in the image folder
        file_list = os.listdir(self.image_folder)

        # Filtering the list to include only image files
        image_list = [file for file in file_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        return image_list

    def display_image(self):
        """
        Displays the current image in the image label widget.
        """

        if self.current_image_index < len(self.image_list):
            # Getting the path to the current image file
            image_path = os.path.join(self.image_folder, self.image_list[self.current_image_index])

            # Opening the image file using PIL
            image = Image.open(image_path)

            # Resizing the image to fit the label widget
            image = image.resize((400, 300))

            # Creating a Tkinter-compatible image object
            tk_image = ImageTk.PhotoImage(image)

            # Setting the image in the label widget
            self.image_label.configure(image=tk_image)
            self.image_label.image = tk_image
        else:
            # Displaying a message when the last image is reached
            messagebox.showinfo("End of Images", "You have reached the end of the image set.")

    def move(self, destination_folder: str):
        """
        Moves the current image to the left folder and displays the next image.

        - destination_folder: str
            The path to the folder where the image will be moved.
        """

        # Getting the path to the current image file
        current_image_path = os.path.join(self.image_folder, self.image_list[self.current_image_index])

        # Moving the image file to the destination folder
        os.rename(current_image_path, os.path.join(destination_folder, self.image_list[self.current_image_index]))

        # Incrementing the current image index
        self.current_image_index += 1

        # Displaying the next image
        self.display_image()
    

def wrapper_for_error_handling(function: Callable, params: Union[list, dict, None] = None):
    """
    Wraps a function with error handling to display error messages in a Tkinter messagebox.

    Parameters:
    - function (Callable): The function to be executed.
    - params (Union[list, dict, None]): Parameters to be passed to the function. Can be a list, a dictionary,
      or None. Defaults to None.

    Returns:
    - The result of the function if it executes successfully.

    Examples for how to wrap functions:
    - my_function(1, 2, 3) can be wrapped with
        ==> return_value = wrapper_for_error_handling(my_function, [1, 2, 3]) can be wrapped with
    - my_function(first_param=1, second_param=2, third_param=3)
        ==> return_value = wrapper_for_error_handling(my_function, {'first_param': 1, 'second_param': 2, 'third_param': 3})
    """
    if params is None:
        params = {}
    try:
        if isinstance(params, list):
            return function(*params)
        elif isinstance(params, dict):
            return function(**params)
    except Exception as e:
        tk.messagebox.showerror(title="An error occurred!", message=str(e))


# Start script
if __name__ == '__main__':
    DATASET_FOLDER = "../archive/dogs-cleaned/test"
    image_ui = ImageUI(DATASET_FOLDER)
