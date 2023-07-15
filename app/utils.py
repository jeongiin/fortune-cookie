import os

def get_fortunes_file_path():
    fortunes_file_folder = os.environ.get('DATAPATH')
    if fortunes_file_folder is None:
        fortunes_file_folder = '../data'
    fortunes_file_path = os.path.join(fortunes_file_folder, "fortunes.txt")
    print(fortunes_file_path)
    if os.path.exists(fortunes_file_path):
        print("Fortunes data exists")
        return (True, fortunes_file_path)
    
    return (False, fortunes_file_path)

def get_my_fortunes_log_file_path():
    fortunes_log_file_folder = os.environ.get('LOGPATH')
    if fortunes_log_file_folder is None:
        fortunes_log_file_folder = '../data'
    fortunes_log_file_path = os.path.join(fortunes_log_file_folder, "my_fortunes.txt")
    print(fortunes_log_file_path)
    if os.path.exists(fortunes_log_file_path):
        print("Log of Fortunes data exists")
        return (True, fortunes_log_file_path)
    
    return (False, fortunes_log_file_path)