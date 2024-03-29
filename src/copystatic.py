import os
import shutil

def copy_files_recursive(source_dir_path, target_dir_path):
    if not os.path.exists(target_dir_path):
        os.mkdir(target_dir_path)
    for file in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, file)
        target_path = os.path.join(target_dir_path, file)
        print(f"* {from_path} -> {target_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, target_path)
        else:
            copy_files_recursive(from_path, target_path)
