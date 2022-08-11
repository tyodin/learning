import colour
from colour.plotting import *
colour_style()
plot_single_illuminant_sd('FL12')
# plot_single_illuminant_sd('E')
# plot_visible_spectrum()  # doctest: +ELLIPSIS
# plot_visible_spectrum('CIE 1931 2 Degree Standard Observer')
# n = colour.xy_to_CCT([0.380,0.380])
# print ('%.1f'%n)
# m = colour.CCT_to_xy(2700)
# print (m)