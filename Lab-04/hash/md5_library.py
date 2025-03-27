import hashlib

def caculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input('Nhập chuỗi cần băm: ')
md5_hash = caculate_md5(input_string)

print("Mã băm MD5 của chuỗi là '{}' là '{}'".format(input_string, md5_hash))