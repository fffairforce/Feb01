from sub import *
import pytest

test_case1 = [	(1.0, 2.0, -1.0),
				(2.0, 1.0,  1.0),
			    (3.0, 1.0,  2.0),
				(3.0, 1.0, -1.0),
				]

@pytest.mark.parametrize("n1,n2,out", test_case1)
def test_substract(n1, n2, out):
    assert substract(n1,n2) == out

@pytest.mark.parametrize("l, e",[
				([1,2,3,4,5,6,7],1),
				([2,1,6,5,99,-1],-1),
				([3,1,2],2),
				])
def test_min_of_list(l, e):
    assert(min_of_list(l) == e)

@pytest.mark.parametrize("l, e",[
				([1,2,3,4,5,6,7],7),
				([2,1,6,5,99,-1],99),
				([3,1,2],2),
				])
def test_max_of_list(l, e):
    assert(max_of_list(l) == e)


