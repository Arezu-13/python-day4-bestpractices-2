import simple_math

def test_simple_math():
    """Created to test the accuracy of the simple_math.py
    and get familiar with pytest's most important functionality.
    
    Returns
    -------
    Checks the inserted value of the parameter `n` and the
    corresponding expected output of `y` based on the 
    simple_math.py module's defined function.
    """
    assert simple_math.simple_math(0) == 1