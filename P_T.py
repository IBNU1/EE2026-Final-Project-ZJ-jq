from PIL import Image
image_file = Image.open('pixil-frame-0.png','r')
convert_RGB_IMAGE = image_file.convert('RGB')
loaded_image = convert_RGB_IMAGE.load()
text_copy = open('menu_copy.txt','a')
def RGB_NUMBER(array_input):
    binary_array = []
    for number in array_input:
        binary_array.append((bin(number)[2:]))
    return binary_array
input_array = (242, 28, 28)
print(RGB_NUMBER(input_array))
test_array = RGB_NUMBER(input_array)



def interate_values(input_image):

    for y in range(input_image.height):
        for x in range(input_image.width):
            values = RGB_NUMBER(input_image.getpixel((x,y)))
            print("13'd{}: PIXEL_INDEX <= [5'b{},6'b{},5'b{}]\n".format((input_image.width*y+x),values[0],values[1],values[2]))
            text_copy.write("13'd{}: PIXEL_DATA <= [5'b{},6'b{},5'b{}];\n".format((input_image.width*y+x),values[0],values[1],values[2]))
    #now we just return the new image
    return 0
interate_values(convert_RGB_IMAGE)
