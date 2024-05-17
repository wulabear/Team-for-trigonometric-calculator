import ctypes
import os.path


path = (os.path.dirname(__file__))
#导入几个dll

asin = ctypes.CDLL(path+'\dll\\taylor_asin.dll')
asin.taylor_asin.argtypes = [ctypes.c_double, ctypes.c_double]
asin.taylor_asin.restype = ctypes.c_double


atan = ctypes.CDLL(path+'\dll\\taylor_atan.dll')
atan.taylor_atan.argtypes = [ctypes.c_double, ctypes.c_double]
atan.taylor_atan.restype = ctypes.c_double


sin = ctypes.CDLL(path+'\dll\\taylor_sin.dll')
sin.taylor_sin.argtypes = [ctypes.c_double, ctypes.c_double]
sin.taylor_sin.restype = ctypes.c_double


cos = ctypes.CDLL(path+'\dll\\taylor_cos.dll')
cos.taylor_cos.argtypes = [ctypes.c_double, ctypes.c_double]
cos.taylor_cos.restype = ctypes.c_double

def sine(x,term):
    return sin.taylor_sin(x,term)
def cosine(x,term):
    return cos.taylor_cos(x,term)
def arcsine(x,term):
    return asin.taylor_asin(x,term)
def arctan(x,term):
    return atan.taylor_atan(x,term)