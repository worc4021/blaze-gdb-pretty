import gdb
import gdb.printing
import re
import numpy as np
from typing import Tuple, List

class BlazeVectorPrinter():
    def __init__(self, val: gdb.Value):
        self.val = val

    def to_string(self):
        val = self.val
        
        ttype = val.type
        if ttype.code == gdb.TYPE_CODE_REF:
            ttype = ttype.target()
        ttype = ttype.unqualified().strip_typedefs()

        if ttype.tag.startswith('blaze::DynamicVector'):
            length = int(val['size_'])
            data = val['v_']
            vec = np.zeros(length, dtype=np.float64)
            for i in range(length):
                elem = (data + i).dereference()
                vec[i] = float(elem)
            return f"blaze::DynamicVector: \n{vec}"
        elif ttype.tag.startswith('blaze::DenseMatrix'):
            m = int(val['m_'])
            n = int(val['n_'])
            data = val['v_']
            mat = np.zeros((m,n), dtype=np.float64)
            for i in range(m):
                for j in range(n):
                    elem = (data + i * n + j).dereference()
                    mat[i,j] = float(elem)
            return f"blaze::DenseMatrix: \n{mat}"
        elif ttype.tag.startswith('blaze::DynamicMatrix'):
            m = int(val['m_'])
            n = int(val['n_'])
            data = val['v_']
            mat = np.zeros((m,n), dtype=np.float64)
            for i in range(m):
                for j in range(n):
                    elem = (data + i * n + j).dereference()
                    mat[i,j] = float(elem)
            return f"blaze::DynamicMatrix: \n{mat}"
        else:
            return f"Could not deal with {ttype.tag}"
        

    def display_hint(self):
        return 'blaze::DenseVector'


def my_blaze_lookup(val : gdb.Value):
    if str(val.type.strip_typedefs()).startswith('blaze::'):
        return BlazeVectorPrinter(val)

class MyBlazeVectorPrintout(gdb.Command):
    def __init__(self):
        super(MyBlazeVectorPrintout, self).__init__("blaze-print", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        arglist = gdb.string_to_argv(arg)
        if len(arglist) != 1:
            print("Usage: blaze-print <variable>")
            return
    
        val = gdb.parse_and_eval(arglist[0])

        ttype = val.type
        if ttype.code == gdb.TYPE_CODE_REF:
            ttype = ttype.target()
        ttype = ttype.unqualified().strip_typedefs()
        if ttype.tag.startswith('blaze::DynamicVector'):
            length = int(val['size_'])
            data = val['v_']
            vec = np.zeros(length, dtype=np.float64)
            for i in range(length):
                elem = (data + i).dereference()
                vec[i] = float(elem)
            print(f"blaze::DynamicVector: \n{vec}")
        elif ttype.tag.startswith('blaze::DenseMatrix'):
            m = int(val['m_'])
            n = int(val['n_'])
            data = val['v_']
            mat = np.zeros((m,n), dtype=np.float64)
            for i in range(m):
                for j in range(n):
                    elem = (data + i * n + j).dereference()
                    mat[i,j] = float(elem)
            print(f"blaze::DenseMatrix: \n{mat}")
        elif ttype.tag.startswith('blaze::DynamicMatrix'):
            m = int(val['m_'])
            n = int(val['n_'])
            data = val['v_']
            mat = np.zeros((m,n), dtype=np.float64)
            for i in range(m):
                for j in range(n):
                    elem = (data + i * n + j).dereference()
                    mat[i,j] = float(elem)
            print(f"blaze::DynamicMatrix: \n{mat}")
        else:
            print(f"Could not deal with {ttype.tag}")


import sys
print(sys.version)
print("Registering commands.")
gdb.pretty_printers.append(my_blaze_lookup)
MyBlazeVectorPrintout()
print("Done. Version %LOCALBUILD%")