def print_square():
    print(get_rectangle(5,5))
def print_rectangle(width,height):
    print(get_rectangle(width,height))       
def get_rectangle(width,height):
    output=""
    for x in range(height):
        for y in range(width):
            if x==height-1 or x==0 or y==width-1 or y==0:
                output+="*"
            else:
                output+=" "
        if x!=height-1:   
            output+="\n"
    return output
