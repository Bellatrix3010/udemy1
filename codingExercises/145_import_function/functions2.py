freezing_point=0
boilling_point=100

def water_state(temperature):
    if temperature <= freezing_point:
        return "Solid"
    elif freezing_point < temperature < boilling_point:
        return "Liquid"
    else:
        return "Gas"
