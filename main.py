


import pyfiglet
import rembg
import numpy as np
from PIL import Image
import os
import time
import webbrowser

def show_welcome_screen():
    clear_screen()
    welcome_ascii = pyfiglet.figlet_format("Celebrare")
    print(welcome_ascii)
    time.sleep(1.5)
    clear_screen()
    welcome_ascii = pyfiglet.figlet_format("Image BG Remover")
    print(welcome_ascii)
    time.sleep(1)

def show_exit_screen():
    clear_screen()
    exit_ascii = pyfiglet.figlet_format("Thank You!")
    print(exit_ascii)
    time.sleep(0.2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_custom_input_path():
    # Get custom input path from the user
    input_path = input("Enter the full path to the input image: ")
    return input_path

def show_image_list():
    # Show a numbered list of images in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images = [file for file in os.listdir(script_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if images:
        print("Image BG Remover")
        print("Select an option:")
        print("0. Go back to the menu")

        for i, image in enumerate(images, start=1):
            print(f"{i}. {image}")

        try:
            choice = input("Enter your choice (0-n or 'all'): ")

            if choice == '0':
                return None
            elif choice.isdigit():
                image_number = int(choice)
                if 1 <= image_number <= len(images):
                    return os.path.join(script_dir, images[image_number - 1])
                else:
                    print("Invalid image number.")
                    return None
            elif choice.lower() == 'all':
                confirm_all = input("Remove background for all images? This may take some time. (y/n): ")
                if confirm_all.lower() == 'y':
                    return 'all'
                else:
                    return None
            else:
                print("Invalid choice.")
                return None
        except ValueError:
            print("Invalid input.")
            return None

def remove_background(input_path):
    try:
        # Load the input image
        input_image = Image.open(input_path)

        # Convert the input image to a numpy array
        input_array = np.array(input_image)

        # Apply background removal using rembg
        output_array = rembg.remove(input_array)

        # Convert the output array to RGB mode
        output_image = Image.fromarray(output_array).convert('RGBA')

        # Save the output image in the same directory as the input image
        output_filename = os.path.splitext(os.path.basename(input_path))[0] + " transparent.png"
        output_path = os.path.join(os.path.dirname(input_path), output_filename)
        output_image.save(output_path, format='PNG')

        print(f"Background removed successfully. Output saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def remove_background_all(images):
    output_folder = os.path.join(os.path.dirname(images[0]), "output_images")
    os.makedirs(output_folder, exist_ok=True)

    for image in images:
        try:
            # Load the input image
            input_image = Image.open(image)

            # Convert the input image to a numpy array
            input_array = np.array(input_image)

            # Apply background removal using rembg
            output_array = rembg.remove(input_array)

            # Convert the output array to RGB mode
            output_image = Image.fromarray(output_array).convert('RGBA')

            # Save the output image in the output folder
            output_filename = os.path.splitext(os.path.basename(image))[0] + " transparent.png"
            output_path = os.path.join(output_folder, output_filename)
            output_image.save(output_path, format='PNG')

            print(f"Background removed for {os.path.basename(image)}. Output saved to {output_path}")

        except Exception as e:
            print(f"An error occurred for {os.path.basename(image)}: {e}")

def open_link(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"An error occurred while opening the link: {e}")

def main():
    show_welcome_screen()
    while True:
        clear_screen()  # Clear the screen

        print("\nOptions:")
        print("1. Show list of images in the same directory")
        print("2. Enter custom path of the image file")
        print("3. About Celebrare")
        print("4. About Me")
        print("e. Exit")

        choice = input("Enter your choice (1-4, e): ")

        if choice == '1':
            images_choice = show_image_list()

            if images_choice:
                if images_choice == 'all':
                    images = [file for file in os.listdir(os.path.dirname(os.path.abspath(__file__))) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
                    remove_background_all(images)
                else:
                    remove_background(images_choice)
        elif choice == '2':
            input_path = get_custom_input_path()
            if input_path is not None:
                remove_background(input_path)
        elif choice == '3':
            open_link("https://celebrare.in/")
        elif choice == '4':
            open_link("https://linktr.ee/tiwarey")
        elif choice == 'e':
            confirm_exit = input("Are you sure you want to exit? (y/n): ")
            if confirm_exit.lower() == 'y':
                show_exit_screen()
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4 or 'e'.")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

if __name__ == "__main__":
    main()
