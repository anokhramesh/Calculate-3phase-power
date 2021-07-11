print("Find Power in 3ph System if lineVoltage and lineCurrent are Given")
print("*************************************************")
while True:
    pf = 0.08 # power factor
    V = float(input("Enter the Voltage here\n"))
    I = float(input("Enter the Current here\n"))
    KW = (1.732*V*I*pf)/1000 # Formula for finding KiloWatts in 3 phase system.
    #print("Power is = ",KW," Kilo Watts")
    formatted_KW = format(KW,".3f")
    print("Power is = ",formatted_KW," Kilo Watts")
    
