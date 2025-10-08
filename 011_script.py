'''
Reads the number of blocks the builders have, and outputs the 
height of the pyramid that can be built using these blocks.
Each lower layer contains one block more than the layer above.
'''
blocks = int(input("Enter the number of blocks: "))

layer_blocks = 1
height = 0

while(blocks >= 0):
    if(blocks < layer_blocks): 
        break
    blocks -= layer_blocks
    layer_blocks += 1
    height += 1

print("The height of the pyramid:", height)