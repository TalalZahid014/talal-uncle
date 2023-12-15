from nltk.metrics import jaccard_distance

set1 = set('biLal is trash')
set2 = set('bll i th')

distance = jaccard_distance(set1, set2)

print(distance)