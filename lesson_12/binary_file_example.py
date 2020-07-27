buffer_size = 32

src = open('test_sign.jpg', 'br')
dst = open('test_sign_copy.jpg', 'bw')

while True:
    data = src.read(buffer_size)
    if data:
        dst.write(data)
    else:
        break

dst.close()
src.close()

