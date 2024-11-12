import pikepdf
import os
import paths


list_of_paths = paths.PATHS

for one_path in list_of_paths:
    path = one_path.replace("\\", os.sep)
    final_path = os.path.normpath(path)
    try:
        with pikepdf.Pdf.open(final_path, allow_overwriting_input=True) as pdf:
            pdf.docinfo["/Title"] = "motivacni_dopis_MP"
            pdf.save(final_path)
        print(f"Title updated for {final_path}")
    except Exception as e:
        print(f"Error processing {final_path}: {e}")