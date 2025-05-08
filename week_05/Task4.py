def compress_string(input_string):
    compressed = []
    count = 1

    
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1

            
        else:
            compressed.append(input_string[i - 1])
            if count > 1:
                compressed.append(str(count))
            count = 1

            
    compressed.append(input_string[-1])
    if count > 1:
        compressed.append(str(count))
        
    compressed_string = ''.join(compressed)
    compression_ratio = round(len(compressed_string) / len(input_string), 2)

    return compressed_string, compression_ratio


input_string = input("Give a string to compress:\n")
compressed_result, ratio = compress_string(input_string)
print(f"Compressed string: {compressed_result}")
print(f"Compressing ratio {ratio}")