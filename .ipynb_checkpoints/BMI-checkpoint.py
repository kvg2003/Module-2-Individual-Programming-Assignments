def body_mass_index(weight, height):
    '''Body Mass Index.
    5 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    s = sorted(set(height), key=height.index)
    if len(s) >= 2:
        h = (s[0] * 12) + s[1]
    if len(s) <= 1:
        h = (s[0] * 12) + s[0]
    
    return float( (float(weight) * 703) / int(h) ** 2 )