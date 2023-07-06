from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

#Remove Wargarin and add Edoxaban

for patient in trial_patients:
    prescription = patients[patient]
    #Exception should be just here
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial")    
    print(patient, prescription)