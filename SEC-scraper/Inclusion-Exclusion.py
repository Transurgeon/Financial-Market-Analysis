import matplotlib
import matplotlib_venn as vplt
from matplotlib import pyplot as plt

def generate_dict(count):
    hash = {}
    
    iterations = pow(2, count) - 1
    for i in range(1, iterations+1):
        hash[format(i, '0'+str(count)+'b')] = 1
    print(hash)
    return(hash)


generate_dict(1)
generate_dict(2)
generate_dict(3)
generate_dict(4)

v = vplt.venn2(subsets=generate_dict(2), set_labels = ('A', 'B', 'C'))
plt.show()

v = vplt.venn3(subsets=generate_dict(3), set_labels = ('A', 'B', 'C'))
plt.show()
    