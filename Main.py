def  human_read_format(size):
    if size // 1024 < 1024 and size % 1024 < 512:
        return str(size % 1024) + 'Б'
    elif size // 1024 < 1024 and size % 1024 > 512:
        return str(size % 1024 + 1) + 'Б'
    elif size // 1024 < 1024 and size % 1024 > 512:
        return str(size % 1024 + 1) + 'Б'

print(human_read_format(125))