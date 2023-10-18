#!/usr/bin/python
import sys, getopt, time
import json
from FirstYearPhysics import FirstYPhysics
from physics_acet import PHY_acet
from Chemistry_acet import Chem_acet
def main(argv,title):
    argument = ''
    usage = 'usage: script.py -f <sometext>'
    try:
        opts, args = getopt.getopt(argv,"hf:",["foo="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-f", "--foo"):
            argument = arg.split()
            try:
                if((argument[len(argument) -1] == "Vibrational_magnetometer_acet")):
                    PHY_acet(argument).VB_Mag()
                elif((argument[len(argument) -1] == "Prism_acet")):
                    PHY_acet(argument).prism()  
                elif((argument[len(argument) -1] == "Air_wedge_acet")):
                    PHY_acet(argument).Air_wed()
                elif((argument[len(argument) -1] == "Laser_acet")):
                    PHY_acet(argument).laser()
                elif((argument[len(argument) -1] == "Newton_ring_acet")):
                    PHY_acet(argument).newton()
                elif((argument[len(argument) -1] == "Radial_flow_acet")):
                    PHY_acet(argument).Radial()
                elif((argument[len(argument) -1] == "Grating_acet")):
                    PHY_acet(argument).grating()
                elif((argument[len(argument) -1] == "Deflection_mag_acet")):
                    PHY_acet(argument).Deflection()
                elif((argument[len(argument) -3] == "Lee's")and (argument[len(argument)-2]=="Disc")and (argument[len(argument) -1]=="Method_acet")):
                    PHY_acet(argument).lee()
                elif((argument[len(argument) -1] == "Polarimeter_acet")):
                    PHY_acet(argument).half()
                elif((argument[len(argument) -2] == "Acetic") and(argument[len(argument) -1] == "acid_acet") ):
                    Chem_acet(argument).Acetic_acid()
                elif((argument[len(argument) -2] == "Dissolved")and(argument[len(argument) -1] == "Oxygen_acet") ):
                    Chem_acet(argument).oxygen()
                elif((argument[len(argument) -2] == "EDTA")and(argument[len(argument) -1] == "Water_acet") ):
                    Chem_acet(argument).edta()
                elif((argument[len(argument) -1] == "Carbonates_acet")):
                    Chem_acet(argument).Carbonate()
                elif((argument[len(argument) -1] == "MOHR_acet")):
                    Chem_acet(argument).mohr()
                elif((argument[len(argument) -2] == "Bleaching")and (argument[len(argument)-1 ]== "powder_acet")):
                    Chem_acet(argument).Bleaching_powder()
                elif((argument[len(argument) -1] == "Copper_acet")):
                    Chem_acet(argument).copper()
                elif((argument[len(argument) -1] == "Conductometric_acet")):
                    Chem_acet(argument).Conductometry()
                elif((argument[len(argument) -2] == "EDTA")and(argument[len(argument)-1]=="Magnesium_acet")):
                    Chem_acet(argument).Magnesium()
                elif((argument[len(argument) -1] == "Calcium_acet")):
                    Chem_acet(argument).calcium()
                elif((argument[len(argument) -2] == "Vibration") and (argument[len(argument) -1] == "Magnetometer")):
                    FirstYPhysics(argument).vibration_magnetometer()
                elif((argument[len(argument) -3] == "Air") and (argument[len(argument) -2] == "Wedge") and (argument[len(argument) -1] == "Experiment")):
                    FirstYPhysics(argument).Air_wedge()
                elif((argument[len(argument) -1] == "Polarimeter")):
                    FirstYPhysics(argument).Polarimeter()
                elif((argument[len(argument) -2] == "Newton") and (argument[len(argument) -1] == "Rings")):
                    FirstYPhysics(argument).Newton_Rings()
                elif((argument[len(argument) -3] == "Lee's") and (argument[len(argument) -2] == "Disc") and (argument[len(argument) -1] == "Method")):
                    FirstYPhysics(argument).lee()
                elif((argument[len(argument) -2] == "Magnetic") and (argument[len(argument) -1] == "Field")):
                    FirstYPhysics(argument).Coil()
                elif((argument[len(argument) -2] == "Thermal") and (argument[len(argument) -1] == "Conductivity")):
                    FirstYPhysics(argument).Thermal()
                elif((argument[len(argument) -2] == "Laser") and (argument[len(argument) -1] == "Grating")):
                    FirstYPhysics(argument).Laser_grating()
                elif((argument[len(argument) -2] == "Spectrometer") and (argument[len(argument) -1] == "Grating")):
                    FirstYPhysics(argument).Spectometer_grating()
                elif((argument[len(argument) -2] == "Spectrometer") and (argument[len(argument) -1] == "Prism")):
                    FirstYPhysics(argument).Spectrometer_prism()                
                else:
                    pass
            except ValueError:
                print(json.dumps({"error":"value added error"}))
if __name__ == "__main__":
    main(sys.argv[1:],sys.argv[2:])