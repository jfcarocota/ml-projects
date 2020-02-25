#perritos y michis
#attribute(weight)  attribute(feel)
#20kg               soft 0               dog 0
#15kg               soft 0               dog 0
#10kg               fluffy 1             cat 1
#8kg                fluffy 1             cat 1
# 
# 
# wight >= 15                  

import numpy
from sklearn import tree

attrib = [[20, 0], [15, 0], [10, 1], [8, 1]] #0 para soft y 1 para fluffy
tags = [0, 0, 1, 1]

clasifier = tree.DecisionTreeClassifier() #clasifica datos
clasifier = clasifier.fit(attrib, tags)
print(clasifier.predict([[10, 1]]))