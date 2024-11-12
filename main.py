# Importing libraries
import pikepdf  # Library for working with PDF
import os  # Library for handling file paths and operating system-dependent functionality
import paths  # Importing the PATHS list from a custom paths.py file that contains the PDF file paths

# Loading the paths from the paths.py file
list_of_paths = paths.PATHS

# Loop through each path in the list of PDF file paths
for one_path in list_of_paths:
    
    # Replace backslashes with the correct path separator depending on the operating system
    path = one_path.replace("\\", os.sep)
    
    # Normalize the path to handle redundant slashes and invalid characters
    final_path = os.path.normpath(path)

    try:
        # Open the PDF file using pikepdf (with the option to overwrite the input file)
        with pikepdf.Pdf.open(final_path, allow_overwriting_input=True) as pdf:
            
            # Set the "new title" in the PDF metadata
            pdf.docinfo["/Title"] = "new title"
            
            # Save the modified PDF back to the original file path
            pdf.save(final_path)
        
        # If the process completes without errors, print a success message
        print(f"Title updated for {final_path}")
    
    except Exception as e:
        # If an error occurs (e.g., the file can't be opened or modified), print an error message
        print(f"Error processing {final_path}: {e}")
