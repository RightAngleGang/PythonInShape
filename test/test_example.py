from example import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(2, 3) == 7
    assert addition(-1, 1) == 0


### Nomenclature
# File : test_XXX
# Function : test_XXXX
### Execution
# In terminal : pytest
