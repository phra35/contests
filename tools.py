import numpy as np

# A make-believe `score_func` for use with scikit-learn's `SelectKBest` tool.
# Simply stores a list of importances and regurgitates them when called.
class scores():
    def __init__(self, imp):
        self.imp = np.array(imp)
    def __call__(self, X, y): 
        return self.imp
   
