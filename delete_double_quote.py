import sys
file_address = ''
ext = ''
if len(sys.argv) > 1:
    file_address = sys.argv[1]
    tmp = file_address.split('.')
    file_name, ext = '.'.join(tmp), tmp[-1]
else:
    print('Err:\tFile Name Needed as the Second Argument.')
    sys.exit(-1)
file_address_new = file_name + '_new.' + ext
with open(file_address) as f1:
    with open(file_address_new, 'w+') as f2:
        for line in f1:
            f2.write('\''.join(line.split('\"')))
