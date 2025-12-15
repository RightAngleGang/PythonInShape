
def get_area(space: Space):
    count = len(space.get_shape_manager().get_shapes())
    show_shapes(space)
    shapeIndex = int(input(f"Selectionnez la forme voulu pour avoir son aire/volume (0-{count - 1}) : "))
    
    value = space.get_shape_manager().get_shapes()[shapeIndex].compute()
    print(value)

def get_voulme(space: Space):
    pass