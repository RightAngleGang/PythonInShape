
def get_area(space: Space):
    count = len(space.get_shape_manager().get_shapes())
    if count == 0:
        print("Aucune forme disponible dans l'espace.")
        return
    show_shapes(space)
    shapeIndex = int(input(f"Selectionnez la forme voulu pour avoir son aire/volume (0-{count - 1}) : "))
    
    value = space.get_shape_manager().get_shapes()[shapeIndex].compute()
    print(value)

def get_voulme(space: Space):
    pass