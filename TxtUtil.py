
def write_line(content , file_path):
    f = open(file_path , 'a')
    f.write(content + "\n")