import numpy as np

class Optimization:
    """
    An abstract optimization tool, taking an EquationOfMotion,
    computing a CostFunction associated to it, imposing a
    ConstraintEquation on it, and optimizing the Shape evolution, in
    order to obtain a Shape that satisfies the ConstraintEquation
    and minimizes the CostFunction
    """
    def __init__(self):
        pass

    