import cv2
import os

def apply_heatmap(image_path, output_folder):
    # Load the image
    image = cv2.imread(image_path)

    # Apply the heatmap filter
    heatmap = cv2.applyColorMap(image, cv2.COLORMAP_HOT)

    # Save the heatmap image with the same name to the output folder
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, heatmap)

def main(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through the images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            apply_heatmap(image_path, output_folder)

if __name__ == "__main__":
    input_folder = "C:\\Users\\Aadhith\\Desktop\\N-BGP\\Dataset\\Complete"
    output_folder = "C:\\Users\\Aadhith\\Desktop\\N-BGP\\Dataset\\Heatmaps"
    main(input_folder, output_folder)
