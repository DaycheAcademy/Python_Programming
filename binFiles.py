with open('numbers', 'bw') as bin_file:
    bin_file.write(bytes(range(17)))

with open('numbers', 'br') as bin_file:
    for num in bin_file:
        print(num)

a = 65534           # 0x FF FE
b = 65535           # 0x FF FF
c = 65536           # 0x 00 01 00 00
d = 98763246        # 0x 05 E3 01 EE

with open('bigNumbers', 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))


with open('bigNumbers', 'br') as bin_file:
    a_new = int.from_bytes(bin_file.read(2), 'big')
    b_new = int.from_bytes(bin_file.read(2), 'big')
    c_new = int.from_bytes(bin_file.read(4), 'big')
    d_new = int.from_bytes(bin_file.read(4), 'big')
    d_new_wrong = int.from_bytes(bin_file.read(4), 'big')

print(a_new)
print(b_new)
print(c_new)
print(d_new)
print(d_new_wrong)  # 0x 05 E3 01 EE  ----> 0x EE 01 E3 05
                                        #   0x EE 01 E3 05
                                        

