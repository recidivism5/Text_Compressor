import io

# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)

binary_stream = io.BytesIO()
# Binary data and strings are different types, so a str
# must be encoded to binary using ascii, utf-8, or other.
binary_stream.write("Hello, world!\n".encode('ascii'))
binary_stream.write("Hello, world!\n".encode('utf-8'))

# Move cursor back to the beginning of the buffer
binary_stream.seek(0)

# Read all data from the buffer
stream_data = binary_stream.read()

# The stream_data is type 'bytes', immutable
print(type(stream_data))
print(stream_data)

# To modify the actual contents of the existing buffer
# use getbuffer() to get an object you can modify.
# Modifying this object updates the underlying BytesIO buffer
mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))  # class 'memoryview'
mutable_buffer[0] = 0xFF

# Re-read the original stream. Contents will be modified
# because we modified the mutable buffer
binary_stream.seek(0)
print(binary_stream.read())

# Pass "wb" to write a new file, or "ab" to append
with open("test.txt", "wb") as binary_file:
    # Write text or bytes to the file
    binary_file.write("Write text by encoding\n".encode('utf8'))
    binary_file.write("cringe.jpg\n".encode('ascii'))
    num_bytes_written = binary_file.write(b'\xDE\xAD\xBE\xEF\x74\x74\x74\x74')
    print("Wrote %d bytes." % num_bytes_written)