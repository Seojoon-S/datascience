import matplotlib.pyplot as plt
plt.title("plotting")
plt.plot([1,2,3,4], [10,20,30,40], color = "red", label = "asc")
plt.plot([1,2,3,4], [40,30,20,10], color = "blue", label = "desc")
plt.legend()
plt.show()
