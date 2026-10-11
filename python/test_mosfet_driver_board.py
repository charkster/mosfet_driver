import pyvisa

rm = pyvisa.ResourceManager('@py')
samd21 = rm.open_resource('USB0::51966::16384::0123456789ABCDEF::0::INSTR')
samd21.write("DRV 1000")

