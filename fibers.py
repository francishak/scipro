# -*- coding: utf-8 -*-
'''
Various Fiber type objects
'''

from numpy import array, float64
from scipy.interpolate import interpolate

class Yb3p:
    '''absorption and emission [pm^2] spectrum of Yb3+ doped fiber'''
    def __init__(self):
        self.wl = array([\
                848, 852, 856, 860, 864,    868, 872, 876, 880, 884, 888, 892,\
                896, 900, 904, 908, 912, 916, 920, 924, 928, 932, 936, 940,\
                944, 948, 952, 956, 960, 964, 968, 969, 970, 971, 972, 973,\
                974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985,\
                986, 988, 992, 996, 1000, 1004, 1008, 1012, 1016, 1020, 1024, 1028,\
                1032, 1036, 1040, 1044, 1048, 1052, 1056, 1060, 1064, 1068, 1072, 1076,\
                1080, 1084, 1088, 1092, 1096, 1100, 1104, 1108, 1112, 1116, 1120, 1124,\
                1128, 1132, 1136, 1140, 1144, 1148, 1152, 1156, 1160, 1164, 1168, 1172,\
                1176, 1180], dtype=float64)
        self.em_coeff = array([\
                2.2E-5, 3.5E-5, 6.3E-5, 1.1E-4, 1.7E-4, 2.7E-4, 4.4E-4, 6.9E-4, 0.0011, 0.0017, 0.0026, 0.0039,\
                0.0058, 0.0086, 0.012, 0.017, 0.022, 0.029, 0.034, 0.039, 0.044, 0.048, 0.05, 0.053,\
                0.057, 0.062, 0.074, 0.095, 0.13, 0.17, 0.26, 0.34, 0.46, 0.70, 1.08, 1.58,\
                2.14, 2.65, 2.97, 2.94, 2.71, 2.28, 1.78, 1.29, 0.91, 0.67, 0.53, 0.45,\
                0.41, 0.36, 0.33, 0.33, 0.36, 0.40, 0.46, 0.53, 0.60, 0.65, 0.65, 0.65,\
                0.60, 0.55, 0.49, 0.44, 0.39, 0.35, 0.33, 0.31, 0.30, 0.29, 0.27, 0.26,\
                0.23, 0.22, 0.21, 0.19, 0.18, 0.16, 0.14, 0.12, 0.11, 0.098, 0.088, 0.076,\
                0.071, 0.061, 0.055, 0.047, 0.042, 0.035, 0.031, 0.027, 0.023, 0.021, 0.018, 0.014,\
                0.014, 0.012 ], dtype=float64)
        self.ab_coeff = array([\
                0.033, 0.041, 0.057, 0.075, 0.090, 0.11, 0.14, 0.17, 0.21, 0.26, 0.31, 0.37,\
                0.43, 0.50, 0.57, 0.62, 0.65, 0.65, 0.62, 0.57, 0.51, 0.44, 0.38, 0.32,\
                0.28, 0.24, 0.23, 0.24, 0.26, 0.28, 0.35, 0.44, 0.57, 0.83, 1.21, 1.68,\
                2.17, 2.55, 2.69, 2.53, 2.22, 1.77, 1.32, 0.91, 0.61, 0.43, 0.32, 0.26,\
                0.23, 0.18, 0.14, 0.11, 0.099, 0.092, 0.088, 0.084, 0.078, 0.070, 0.059, 0.049,\
                0.038, 0.029, 0.022, 0.016, 0.012, 0.009, 0.0072, 0.0057, 0.0046, 0.0038, 0.0033, 0.0024,\
                0.0018, 0.0015, 0.0012, 9.5E-4, 7.3E-4, 5.6E-4, 4.2E-4, 3.2E-4, 2.4E-4, 1.9E-4, 1.4E-4, 1.1E-4,\
                8.5E-5, 6.3E-5, 4.9E-5, 3.6E-5, 2.8E-5, 2.0E-5, 1.6E-5, 1.1E-5, 8.6E-6, 6.8E-6, 4.9E-6, 3.5E-6,\
                3.1E-6, 2.2E-6 ], dtype=float64)
    
    def em(self, wl):
        '''return emission coefficient for wl [nm] \n em(wl)'''
        return interpolate.spline(self.wl, self.em_coeff, wl)
    
    def ab(self, wl):
        '''return absorption coefficient for wl [nm] \n ab(wl)'''
        return interpolate.spline(self.wl, self.ab_coeff, wl)
    
