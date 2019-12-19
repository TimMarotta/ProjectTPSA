import geopandas
import matplotlib.pyplot as plt
import descartes

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
print(world.head())
plt.plot(world)
