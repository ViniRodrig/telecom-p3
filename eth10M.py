def decode(sig):
    out = []
    counter = 0
    for i in range(len(sig)):
        counter += 1
        if sig[i-1] != sig[i] and counter >= 7:
            out.append(sig[i])
            counter = 0
    preamble = True
    byte_reset = 0b1_0000_0000
    byte = byte_reset
    frame = []

    for i in range(len(out)):
        if preamble and out[i-1:i+1] == [1, 1]:
            preamble = False
        elif not preamble:
            byte = byte >> 1 | out[i] << 8
            if byte & 1 == 1:
                frame.append(byte >> 1)
                byte = byte_reset

    return bytes(frame)
