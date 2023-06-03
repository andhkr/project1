from tkinter import *
from PIL import ImageTk,Image

prjt = Tk()

prjt.title('Doctors')
iconi = PhotoImage(file='Images/doctor.png')  
prjt.iconphoto(True, iconi)
prjt.geometry('650x635')
prjt.configure(background='Light Blue')

# Create Frame
frame1=LabelFrame(prjt,padx=50)
frame1.grid(row=3,column=0,columnspan=4,pady=10,sticky=N+E+W+S)
frame2=LabelFrame(prjt,padx=50)
frame2.grid(row=4,column=0,columnspan=4,pady=10,sticky=N+E+W+S)
frame3=LabelFrame(prjt,padx=50,)
frame3.grid(row=5,column=0,columnspan=4,pady=10,sticky=N+E+W+S)



#create functions
def DocList():
    

    try:
        if location.get()=="Palakkad" or "Kozhikode":
            if location.get()=="Palakkad" :
                if Ds_Name.get()=='Cardiologist':
                    global mylabelf111
                    global mylabelf12
                    global mylabelf13
                    global mylabelf14
                    global mylabelf15
                    global mylabelf16
                    
                    global mylabelf211
                    global mylabelf22
                    global mylabelf23
                    global mylabelf24
                    global mylabelf25
                    global mylabelf26
                    
                    global mylabelf311
                    global mylabelf32
                    global mylabelf33
                    global mylabelf34
                    global mylabelf35
                    global mylabelf36

                    mylabelf111=Label(frame1,text='Dr. Enosh',font=("Halvetica",15))
                    mylabelf12=Label(frame1,text='MBBS,MD,DM cardiology',font=("Halvetica",15))
                    mylabelf13=Label(frame1,text='Cardiologist',font=("Halvetica",15))
                    mylabelf14=Label(frame1,text='Hospital : Govt. Hospital,near Stadium,palakkad',font=("Halvetica",15))
                    mylabelf15=Label(frame1,text='Time Slot:2PM to 5 PM',font=("Halvetica",15))
                    mylabelf16=Label(frame1,text='Land line:04912210767',font=("Halvetica",15))
                    
                    mylabelf211=Label(frame2,text='Dr. Supradeep ',font=("Halvetica",15))
                    mylabelf22=Label(frame2,text='MBBS , MD(general medicine), DM(cardiology)',font=("Halvetica",15))
                    mylabelf23=Label(frame2,text='Cardiologist',font=("Halvetica",15))
                    mylabelf24=Label(frame2,text='Hospital : Multi speciality , kanjikode',font=("Halvetica",15))
                    mylabelf25=Label(frame2,text='Time slot : 11 Am to 2pm , 7pm to 8 30 pm',font=("Halvetica",15))
                    mylabelf26=Label(frame2,text='Land line : 0491 2269896',font=("Halvetica",15))
                    
                    mylabelf311=Label(frame3,text='Dr Madhumita Ramesh',font=("Halvetica",15))
                    mylabelf32=Label(frame3,text='MD ,senior consultant , DM',font=("Halvetica",15))
                    mylabelf33=Label(frame3,text='Cardiologist',font=("Halvetica",15))
                    mylabelf34=Label(frame3,text='Hospital : Medico Global (medical college) , palakkad',font=("Halvetica",15))
                    mylabelf35=Label(frame3,text='Time slot: 11 30 AM to 1pm , 3pm to 4 30 pm',font=("Halvetica",15))
                    mylabelf36=Label(frame3,text='Land line : 0491 2296787',font=("Halvetica",15))
                    
                    mylabelf111.grid(row=0,column=0,sticky=W)
                    mylabelf12.grid(row=1,column=0,sticky=W)
                    mylabelf13.grid(row=2,column=0,sticky=W)
                    mylabelf14.grid(row=3,column=0,sticky=W)
                    mylabelf15.grid(row=4,column=0,sticky=W)
                    mylabelf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelf211.grid(row=0,column=0,sticky=W)
                    mylabelf22.grid(row=1,column=0,sticky=W)
                    mylabelf23.grid(row=2,column=0,sticky=W)
                    mylabelf24.grid(row=3,column=0,sticky=W)
                    mylabelf25.grid(row=4,column=0,sticky=W)
                    mylabelf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelf311.grid(row=0,column=0,sticky=W)
                    mylabelf32.grid(row=1,column=0,sticky=W)
                    mylabelf33.grid(row=2,column=0,sticky=W)
                    mylabelf34.grid(row=3,column=0,sticky=W)
                    mylabelf35.grid(row=4,column=0,sticky=W)
                    mylabelf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                    
                elif Ds_Name.get()=='Emergency Medicien and Trauma':
                    global mylabelef111
                    global mylabelef12
                    global mylabelef13
                    global mylabelef14
                    global mylabelef15
                    global mylabelef16
                    
                    global mylabelef211
                    global mylabelef22
                    global mylabelef23
                    global mylabelef24
                    global mylabelef25
                    global mylabelef26
                    
                    global mylabelef311
                    global mylabelef32
                    global mylabelef33
                    global mylabelef34
                    global mylabelef35
                    global mylabelef36

                    mylabelef111=Label(frame1,text='Dr.Vishwa Tej',font=("Halvetica",15))
                    mylabelef12=Label(frame1,text='MBBS, DNB(Emergency medicine)',font=("Halvetica",15))
                    mylabelef13=Label(frame1,text='EMERGENCY MEDICINE AND TRAUMA',font=("Halvetica",15))
                    mylabelef14=Label(frame1,text='Hospital: Govt ,near stadium, Palakkad',font=("Halvetica",15))
                    mylabelef15=Label(frame1,text='Time Slot:10AM to 2PM,3PM to 5PM',font=("Halvetica",15))
                    mylabelef16=Label(frame1,text='Land line : 0491 2511967',font=("Halvetica",15))
                    
                    mylabelef211=Label(frame2,text='Dr Vivek Mishra ',font=("Halvetica",15))
                    mylabelef22=Label(frame2,text='MBBS',font=("Halvetica",15))
                    mylabelef23=Label(frame2,text='EMERGENCY MEDICINE AND TRAUMA',font=("Halvetica",15))
                    mylabelef24=Label(frame2,text='Hospital : Multi speciality , Kanjikode',font=("Halvetica",15))
                    mylabelef25=Label(frame2,text='Time slot: 10 Am to 2 pm',font=("Halvetica",15))
                    mylabelef26=Label(frame2,text='Land line : 0491 2390967',font=("Halvetica",15))
                    
                    mylabelef311=Label(frame3,text='Dr Hema Chandran',font=("Halvetica",15))
                    mylabelef32=Label(frame3,text='MBBS',font=("Halvetica",15))
                    mylabelef33=Label(frame3,text='EMERGENCY MEDICINE AND TRAUMA',font=("Halvetica",15))
                    mylabelef34=Label(frame3,text='Hospital : District hospital , near Bus stand , palakkad',font=("Halvetica",15))
                    mylabelef35=Label(frame3,text='Time slot: 10am to 2pm, 6pm to 8pm',font=("Halvetica",15))
                    mylabelef36=Label(frame3,text='Land line : 0491 2317965 ',font=("Halvetica",15))
                    
                    mylabelef111.grid(row=0,column=0,sticky=W)
                    mylabelef12.grid(row=1,column=0,sticky=W)
                    mylabelef13.grid(row=2,column=0,sticky=W)
                    mylabelef14.grid(row=3,column=0,sticky=W)
                    mylabelef15.grid(row=4,column=0,sticky=W)
                    mylabelef16.grid(row=5,column=0,sticky=W)
                    
                    mylabelef211.grid(row=0,column=0,sticky=W)
                    mylabelef22.grid(row=1,column=0,sticky=W)
                    mylabelef23.grid(row=2,column=0,sticky=W)
                    mylabelef24.grid(row=3,column=0,sticky=W)
                    mylabelef25.grid(row=4,column=0,sticky=W)
                    mylabelef26.grid(row=5,column=0,sticky=W)
                    
                    mylabelef311.grid(row=0,column=0,sticky=W)
                    mylabelef32.grid(row=1,column=0,sticky=W)
                    mylabelef33.grid(row=2,column=0,sticky=W)
                    mylabelef34.grid(row=3,column=0,sticky=W)
                    mylabelef35.grid(row=4,column=0,sticky=W)
                    mylabelef36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                            
                elif Ds_Name.get()=='General Physician':
                    global mylabelgf111
                    global mylabelgf12
                    global mylabelgf13
                    global mylabelgf14
                    global mylabelgf15
                    global mylabelgf16
                    
                    global mylabelgf211
                    global mylabelgf22
                    global mylabelgf23
                    global mylabelgf24
                    global mylabelgf25
                    global mylabelgf26
                    
                    global mylabelgf311
                    global mylabelgf32
                    global mylabelgf33
                    global mylabelgf34
                    global mylabelgf35
                    global mylabelgf36

                    mylabelgf111=Label(frame1,text='Dr Shalini Pandey',font=("Halvetica",15))
                    mylabelgf12=Label(frame1,text='MBBS',font=("Halvetica",15))
                    mylabelgf13=Label(frame1,text='GENERAL PHYSICIAN',font=("Halvetica",15))
                    mylabelgf14=Label(frame1,text='Hospital: Govt ,near stadium, Palakkad',font=("Halvetica",15))
                    mylabelgf15=Label(frame1,text='Time Slot:9AM to 2PM,3PM to 5PM',font=("Halvetica",15))
                    mylabelgf16=Label(frame1,text='Land line : 0491 2238061',font=("Halvetica",15))
                    
                    mylabelgf211=Label(frame2,text='Dr Zakir Jahan ',font=("Halvetica",15))
                    mylabelgf22=Label(frame2,text='MBBS',font=("Halvetica",15))
                    mylabelgf23=Label(frame2,text='GENERAL PHYSICIAN',font=("Halvetica",15))
                    mylabelgf24=Label(frame2,text='Hospital : Multi speciality , Kanjikode',font=("Halvetica",15))
                    mylabelgf25=Label(frame2,text='Time slot: 9am to 1pm,7pm to 8:30pm ',font=("Halvetica",15))
                    mylabelgf26=Label(frame2,text='Land line : 0491 2378167 ',font=("Halvetica",15))
                    
                    mylabelgf311=Label(frame3,text='Dr Bindal',font=("Halvetica",15))
                    mylabelgf32=Label(frame3,text='MBBS , PGC( chest and TB)',font=("Halvetica",15))
                    mylabelgf33=Label(frame3,text='GENERAL PHYSICIAN',font=("Halvetica",15))
                    mylabelgf34=Label(frame3,text='Hospital : General Clinic , palakkad',font=("Halvetica",15))
                    mylabelgf35=Label(frame3,text='Time slot: 9am to 1pm, 5:30pm to 8:30pm',font=("Halvetica",15))
                    mylabelgf36=Label(frame3,text='Land line : 0491 2342967 ',font=("Halvetica",15))
                    
                    mylabelgf111.grid(row=0,column=0,sticky=W)
                    mylabelgf12.grid(row=1,column=0,sticky=W)
                    mylabelgf13.grid(row=2,column=0,sticky=W)
                    mylabelgf14.grid(row=3,column=0,sticky=W)
                    mylabelgf15.grid(row=4,column=0,sticky=W)
                    mylabelgf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelgf211.grid(row=0,column=0,sticky=W)
                    mylabelgf22.grid(row=1,column=0,sticky=W)
                    mylabelgf23.grid(row=2,column=0,sticky=W)
                    mylabelgf24.grid(row=3,column=0,sticky=W)
                    mylabelgf25.grid(row=4,column=0,sticky=W)
                    mylabelgf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelgf311.grid(row=0,column=0,sticky=W)
                    mylabelgf32.grid(row=1,column=0,sticky=W)
                    mylabelgf33.grid(row=2,column=0,sticky=W)
                    mylabelgf34.grid(row=3,column=0,sticky=W)
                    mylabelgf35.grid(row=4,column=0,sticky=W)
                    mylabelgf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                    
                elif Ds_Name.get()=='Obstetrics and Gynaecologist':
                    global mylabelof111
                    global mylabelof12
                    global mylabelof13
                    global mylabelof14
                    global mylabelof15
                    global mylabelof16
                
                    global mylabelof211
                    global mylabelof22
                    global mylabelof23
                    global mylabelof24
                    global mylabelof25
                    global mylabelof26
                    
                    global mylabelof311
                    global mylabelof32
                    global mylabelof33
                    global mylabelof34
                    global mylabelof35
                    global mylabelof36

                    mylabelof111=Label(frame1,text='Dr Peehuna Datta',font=("Halvetica",15))
                    mylabelof12=Label(frame1,text='Senior consultant ',font=("Halvetica",15))
                    mylabelof13=Label(frame1,text='Obstetrics and Gynaecologist',font=("Halvetica",15))
                    mylabelof14=Label(frame1,text='Hospital: Govt ,near stadium, Palakkad',font=("Halvetica",15))
                    mylabelof15=Label(frame1,text='Time Slot:9:30AM to 3PM',font=("Halvetica",15))
                    mylabelof16=Label(frame1,text='Land line : 0491 2318967 ',font=("Halvetica",15))
                    
                    mylabelof211=Label(frame2,text='Dr Sitara Chowhan ',font=("Halvetica",15))
                    mylabelof22=Label(frame2,text='Consultant gynaecologist, MBBS , DGO',font=("Halvetica",15))
                    mylabelof23=Label(frame2,text='Obstetrics and Gynaecologist',font=("Halvetica",15))
                    mylabelof24=Label(frame2,text='Hospital : Multi speciality , Kanjikode',font=("Halvetica",15))
                    mylabelof25=Label(frame2,text='Time slot: 9am to 5pm',font=("Halvetica",15))
                    mylabelof26=Label(frame2,text='Land line : 0491 2200667  ',font=("Halvetica",15))
                    
                    mylabelof311=Label(frame3,text='Dr Janvi Suresh',font=("Halvetica",15))
                    mylabelof32=Label(frame3,text='MBBS , DGO',font=("Halvetica",15))
                    mylabelof33=Label(frame3,text='Obstetrics and Gynaecologist',font=("Halvetica",15))
                    mylabelof34=Label(frame3,text='Hospital: Medico global(medical college),PALAKKAD',font=("Halvetica",15))
                    mylabelof35=Label(frame3,text='Time slot : 9am to 5pm',font=("Halvetica",15))
                    mylabelof36=Label(frame3,text='Land line : 0491 2298957  ',font=("Halvetica",15))
                    
                    mylabelof111.grid(row=0,column=0,sticky=W)
                    mylabelof12.grid(row=1,column=0,sticky=W)
                    mylabelof13.grid(row=2,column=0,sticky=W)
                    mylabelof14.grid(row=3,column=0,sticky=W)
                    mylabelof15.grid(row=4,column=0,sticky=W)
                    mylabelof16.grid(row=5,column=0,sticky=W)
                    
                    mylabelof211.grid(row=0,column=0,sticky=W)
                    mylabelof22.grid(row=1,column=0,sticky=W)
                    mylabelof23.grid(row=2,column=0,sticky=W)
                    mylabelof24.grid(row=3,column=0,sticky=W)
                    mylabelof25.grid(row=4,column=0,sticky=W)
                    mylabelof26.grid(row=5,column=0,sticky=W)
                    
                    mylabelof311.grid(row=0,column=0,sticky=W)
                    mylabelof32.grid(row=1,column=0,sticky=W)
                    mylabelof33.grid(row=2,column=0,sticky=W)
                    mylabelof34.grid(row=3,column=0,sticky=W)
                    mylabelof35.grid(row=4,column=0,sticky=W)
                    mylabelof36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                    elif Ds_Name.get()=='Radiologist':
                    global mylabelrf111
                    global mylabelrf12
                    global mylabelrf13
                    global mylabelrf14
                    global mylabelrf15
                    global mylabelrf16
                
                    global mylabelrf211
                    global mylabelrf22
                    global mylabelrf23
                    global mylabelrf24
                    global mylabelrf25
                    global mylabelrf26
                    
                    global mylabelrf311
                    global mylabelrf32
                    global mylabelrf33
                    global mylabelrf34
                    global mylabelrf35
                    global mylabelrf36

                    mylabelrf111=Label(frame1,text='Dr Amit Aggarwal',font=("Halvetica",15))
                    mylabelrf12=Label(frame1,text='MBBS , DMRD , Consultant Radiologist',font=("Halvetica",15))
                    mylabelrf13=Label(frame1,text='Radiologist',font=("Halvetica",15))
                    mylabelrf14=Label(frame1,text='Hospital: Govt ,near stadium, Palakkad',font=("Halvetica",15))
                    mylabelrf15=Label(frame1,text='Time Slot:9AM to 1PM,5PM to 6:30PM',font=("Halvetica",15))
                    mylabelrf16=Label(frame1,text='Land line : 0491 2298767 ',font=("Halvetica",15))
            
                    mylabelrf211=Label(frame2,text='Dr Mitsuri',font=("Halvetica",15))
                    mylabelrf22=Label(frame2,text='MBBS , DMRD',font=("Halvetica",15))
                    mylabelrf23=Label(frame2,text='Radiologist',font=("Halvetica",15))
                    mylabelrf24=Label(frame2,text='Hospital : Multi speciality , Palakkad',font=("Halvetica",15))
                    mylabelrf25=Label(frame2,text='Time slot: 10AM to 1PM, 4PM to 5PM',font=("Halvetica",15))
                    mylabelrf26=Label(frame2,text='Land line : 0491 2378787   ',font=("Halvetica",15))
                    
                    mylabelrf311=Label(frame3,text='Dr Sudeep Rathod',font=("Halvetica",15))
                    mylabelrf32=Label(frame3,text='MBBS , DMRD',font=("Halvetica",15))
                    mylabelrf33=Label(frame3,text='Radiologist',font=("Halvetica",15))
                    mylabelrf34=Label(frame3,text='Hospital: Medico global(medical college),PALAKKAD',font=("Halvetica",15))
                    mylabelrf35=Label(frame3,text='Time slot : 10am to 1pm,3pm to 5:30pm',font=("Halvetica",15))
                    mylabelrf36=Label(frame3,text='Land line : 0491 2289067   ',font=("Halvetica",15))
                    
                    mylabelrf111.grid(row=0,column=0,sticky=W)
                    mylabelrf12.grid(row=1,column=0,sticky=W)
                    mylabelrf13.grid(row=2,column=0,sticky=W)
                    mylabelrf14.grid(row=3,column=0,sticky=W)
                    mylabelrf15.grid(row=4,column=0,sticky=W)
                    mylabelrf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelrf211.grid(row=0,column=0,sticky=W)
                    mylabelrf22.grid(row=1,column=0,sticky=W)
                    mylabelrf23.grid(row=2,column=0,sticky=W)
                    mylabelrf24.grid(row=3,column=0,sticky=W)
                    mylabelrf25.grid(row=4,column=0,sticky=W)
                    mylabelrf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelrf311.grid(row=0,column=0,sticky=W)
                    mylabelrf32.grid(row=1,column=0,sticky=W)
                    mylabelrf33.grid(row=2,column=0,sticky=W)
                    mylabelrf34.grid(row=3,column=0,sticky=W)
                    mylabelrf35.grid(row=4,column=0,sticky=W)
                    mylabelrf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                elif Ds_Name.get()=='ENT':
                    global mylabelnf111
                    global mylabelnf12
                    global mylabelnf13
                    global mylabelnf14
                    global mylabelnf15
                    global mylabelnf16
                
                    global mylabelnf211
                    global mylabelnf22
                    global mylabelnf23
                    global mylabelnf24
                    global mylabelnf25
                    global mylabelnf26
                
                    global mylabelnf311
                    global mylabelnf32
                    global mylabelnf33
                    global mylabelnf34
                    global mylabelnf35
                    global mylabelnf36

                    mylabelnf111=Label(frame1,text='Dr Mitesh Patel',font=("Halvetica",15))
                    mylabelnf12=Label(frame1,text='MBBs , DNB ,D.L.O',font=("Halvetica",15))
                    mylabelnf13=Label(frame1,text='ENT',font=("Halvetica",15))
                    mylabelnf14=Label(frame1,text='Hospital: Govt ,near stadium, Palakkad',font=("Halvetica",15))
                    mylabelnf15=Label(frame1,text='Time Slot:11AM to 1PM,6PM to 7:30PM',font=("Halvetica",15))
                    mylabelnf16=Label(frame1,text='Land line : 0491 2234967',font=("Halvetica",15))
            
                    mylabelnf211=Label(frame2,text='Dr Kalpana Mehan',font=("Halvetica",15))
                    mylabelnf22=Label(frame2,text='MBBs , MS (ENT) , DNB',font=("Halvetica",15))
                    mylabelnf23=Label(frame2,text='ENT',font=("Halvetica",15))
                    mylabelnf24=Label(frame2,text='Hospital : Multi speciality , Kanjikode',font=("Halvetica",15))
                    mylabelnf25=Label(frame2,text='Time slot: 11am to 1pm, 6pm to 7:30pm',font=("Halvetica",15))
                    mylabelnf26=Label(frame2,text='Land line : 0491 2254967   ',font=("Halvetica",15))
                    
                    mylabelnf311=Label(frame3,text='Dr David',font=("Halvetica",15))
                    mylabelnf32=Label(frame3,text='MBBS , MS (ENT)',font=("Halvetica",15))
                    mylabelnf33=Label(frame3,text='ENT',font=("Halvetica",15))
                    mylabelnf34=Label(frame3,text='Hospital : Clinic , Palakkad',font=("Halvetica",15))
                    mylabelnf35=Label(frame3,text='Time slot : 11am to 1pm,6:30pm to 8:30pm',font=("Halvetica",15))
                    mylabelnf36=Label(frame3,text='Land line : 0491 2278967    ',font=("Halvetica",15))
                    
                    mylabelnf111.grid(row=0,column=0,sticky=W)
                    mylabelnf12.grid(row=1,column=0,sticky=W)
                    mylabelnf13.grid(row=2,column=0,sticky=W)
                    mylabelnf14.grid(row=3,column=0,sticky=W)
                    mylabelnf15.grid(row=4,column=0,sticky=W)
                    mylabelnf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelnf211.grid(row=0,column=0,sticky=W)
                    mylabelnf22.grid(row=1,column=0,sticky=W)
                    mylabelnf23.grid(row=2,column=0,sticky=W)
                    mylabelnf24.grid(row=3,column=0,sticky=W)
                    mylabelnf25.grid(row=4,column=0,sticky=W)
                    mylabelnf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelnf311.grid(row=0,column=0,sticky=W)
                    mylabelnf32.grid(row=1,column=0,sticky=W)
                    mylabelnf33.grid(row=2,column=0,sticky=W)
                    mylabelnf34.grid(row=3,column=0,sticky=W)
                    mylabelnf35.grid(row=4,column=0,sticky=W)
                    mylabelnf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                                        
    
                
                else:
                    raise Exception('Please Enter Speciality among:'+'\n'+'Cardiologist'+'\n'+'General Physician'+'\n'+'Radiologist'+'\n'+'ENT'+'\n'+'Emergency Medicine Trauma'+'\n'+'Obstetrics and Gynaecologist')
             elif location.get()=="Kozhikode":  
                if Ds_Name.get()=='Cardiologist':
                    global mylabelKf111
                    global mylabelKf12
                    global mylabelKf13
                    global mylabelKf14
                    global mylabelKf15
                    global mylabelKf16
                    
                    global mylabelKf211
                    global mylabelKf22
                    global mylabelKf23
                    global mylabelKf24
                    global mylabelKf25
                    global mylabelKf26
                    
                    global mylabelKf311
                    global mylabelKf32
                    global mylabelKf33
                    global mylabelKf34
                    global mylabelKf35
                    global mylabelKf36

                    mylabelKf111=Label(frame1,text='Dr. SatyaNarayanaRao',font=("Halvetica",15))
                    mylabelKf12=Label(frame1,text='MBBS,MD,MS',font=("Halvetica",15))
                    mylabelKf13=Label(frame1,text='Cardiologist',font=("Halvetica",15))
                    mylabelKf14=Label(frame1,text='Hospital : Government hospital,Kozhikode ',font=("Halvetica",15))
                    mylabelKf15=Label(frame1,text='Time Slot: 8:00 AM-5:00 PM ',font=("Halvetica",15))
                    mylabelKf16=Label(frame1,text='Land line :0471 2318744 ',font=("Halvetica",15))
                    
                    mylabelKf211=Label(frame2,text='Dr. Hema Sunder Gupta  ',font=("Halvetica",15))
                    mylabelKf22=Label(frame2,text='Senior Consultant ,MBBS,MD,MS(Cardiology) ',font=("Halvetica",15))
                    mylabelKf23=Label(frame2,text='Cardiologist',font=("Halvetica",15))
                    mylabelKf24=Label(frame2,text='Hospital :Starcare,Kozhikode,, 673017 ',font=("Halvetica",15))
                    mylabelKf25=Label(frame2,text='Time slot : 4:30 PM-11.30 PM' ,font=("Halvetica",15))
                    mylabelKf26=Label(frame2,text='Land line : 0471 2975498 ',font=("Halvetica",15))
                    
                    mylabelKf311=Label(frame3,text='Dr. Vaibhav Mittal ',font=("Halvetica",15))
                    mylabelKf32=Label(frame3,text='MBBS ',font=("Halvetica",15))
                    mylabelKf33=Label(frame3,text='Cardiologist',font=("Halvetica",15))
                    mylabelKf34=Label(frame3,text='Hospital :  Baby Memorial College,kozhikode',font=("Halvetica",15))
                    mylabelKf35=Label(frame3,text='Time slot: 8:30AM-2PM ',font=("Halvetica",15))
                    mylabelKf36=Label(frame3,text='Land line : 0471 2237695 ',font=("Halvetica",15))
                    
                    mylabelKf111.grid(row=0,column=0,sticky=W)
                    mylabelKf12.grid(row=1,column=0,sticky=W)
                    mylabelKf13.grid(row=2,column=0,sticky=W)
                    mylabelKf14.grid(row=3,column=0,sticky=W)
                    mylabelKf15.grid(row=4,column=0,sticky=W)
                    mylabelKf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelKf211.grid(row=0,column=0,sticky=W)
                    mylabelKf22.grid(row=1,column=0,sticky=W)
                    mylabelKf23.grid(row=2,column=0,sticky=W)
                    mylabelKf24.grid(row=3,column=0,sticky=W)
                    mylabelKf25.grid(row=4,column=0,sticky=W)
                    mylabelKf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelKf311.grid(row=0,column=0,sticky=W)
                    mylabelKf32.grid(row=1,column=0,sticky=W)
                    mylabelKf33.grid(row=2,column=0,sticky=W)
                    mylabelKf34.grid(row=3,column=0,sticky=W)
                    mylabelKf35.grid(row=4,column=0,sticky=W)
                    mylabelKf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                    
                elif Ds_Name.get()=='Emergency Medicien and Trauma':
                    global mylabelKef111
                    global mylabelKef12
                    global mylabelKef13
                    global mylabelKef14
                    global mylabelKef15
                    global mylabelKef16
                    
                    global mylabelKef211
                    global mylabelKef22
                    global mylabelKef23
                    global mylabelKef24
                    global mylabelKef25
                    global mylabelKef26
                    
                    global mylabelKef311
                    global mylabelKef32
                    global mylabelKef33
                    global mylabelKef34
                    global mylabelKef35
                    global mylabelKef36

                    mylabelKef111=Label(frame1,text='Dr. Hrishikesh Parappol ',font=("Halvetica",15))
                    mylabelKef12=Label(frame1,text='MBBS, DNB(Emergency medicine)',font=("Halvetica",15))
                    mylabelKef13=Label(frame1,text='EMERGENCY MEDICINE AND TRAUMA',font=("Halvetica",15))
                    mylabelKef14=Label(frame1,text='Hospital: Govt ,near stadium, Kozhikode',font=("Halvetica",15))
                    mylabelKef15=Label(frame1,text='Time Slot:8AM-5PM',font=("Halvetica",15))
                    mylabelKef16=Label(frame1,text='Land line : 0471 2157952',font=("Halvetica",15))
                    
                    mylabelKef211=Label(frame2,text='Dr.Divyasree  ',font=("Halvetica",15))
                    mylabelKef22=Label(frame2,text='MBBS',font=("Halvetica",15))
                    mylabelKef23=Label(frame2,text='EMERGENCY MEDICINE AND TRAUMA',font=("Halvetica",15))
                    mylabelKef24=Label(frame2,text='Hospital : Multi speciality , Kozhikode',font=("Halvetica",15))
                    mylabelKef25=Label(frame2,text='Time slot: 8AM-2PM',font=("Halvetica",15))
                    mylabelKef26=Label(frame2,text='Land line : 0471 2495813',font=("Halvetica",15))
                    
                    mylabelKef311=Label(frame3,text='Dr. Ashok Sudhakaran ',font=("Halvetica",15))
                    mylabelKef32=Label(frame3,text='MBBS',font=("Halvetica",15))
                    mylabelKef33=Label(frame3,text='EMERGENCY MEDICINE AND TRAUMA',font=("Halvetica",15))
                    mylabelKef34=Label(frame3,text='Hospital :Kozhikode CoOperative Hospital,Kozhikode',font=("Halvetica",15))
                    mylabelKef35=Label(frame3,text='Time slot: 3PM-8PM',font=("Halvetica",15))
                    mylabelKef36=Label(frame3,text='Land line : 0471 2725498 ',font=("Halvetica",15))
                    
                    mylabelKef111.grid(row=0,column=0,sticky=W)
                    mylabelKef12.grid(row=1,column=0,sticky=W)
                    mylabelKef13.grid(row=2,column=0,sticky=W)
                    mylabelKef14.grid(row=3,column=0,sticky=W)
                    mylabelKef15.grid(row=4,column=0,sticky=W)
                    mylabelKef16.grid(row=5,column=0,sticky=W)
                    
                    mylabelKef211.grid(row=0,column=0,sticky=W)
                    mylabelKef22.grid(row=1,column=0,sticky=W)
                    mylabelKef23.grid(row=2,column=0,sticky=W)
                    mylabelKef24.grid(row=3,column=0,sticky=W)
                    mylabelKef25.grid(row=4,column=0,sticky=W)
                    mylabelKef26.grid(row=5,column=0,sticky=W)
                    
                    mylabelKef311.grid(row=0,column=0,sticky=W)
                    mylabelKef32.grid(row=1,column=0,sticky=W)
                    mylabelKef33.grid(row=2,column=0,sticky=W)
                    mylabelKef34.grid(row=3,column=0,sticky=W)
                    mylabelKef35.grid(row=4,column=0,sticky=W)
                    mylabelKef36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                            
                elif Ds_Name.get()=='General Physician':
                    global mylabelKgf111
                    global mylabelKgf12
                    global mylabelKgf13
                    global mylabelKgf14
                    global mylabelKgf15
                    global mylabelKgf16
                    
                    global mylabelKgf211
                    global mylabelKgf22
                    global mylabelKgf23
                    global mylabelKgf24
                    global mylabelKgf25
                    global mylabelKgf26
                    
                    global mylabelKgf311
                    global mylabelKgf32
                    global mylabelKgf33
                    global mylabelKgf34
                    global mylabelKgf35
                    global mylabelKgf36

                    mylabelKgf111=Label(frame1,text='Dr.Somesh Nambiar ',font=("Halvetica",15))
                    mylabelKgf12=Label(frame1,text='MBBS, MD in General Medicine',font=("Halvetica",15))
                    mylabelKgf13=Label(frame1,text='GENERAL PHYSICIAN',font=("Halvetica",15))
                    mylabelKgf14=Label(frame1,text='Hospital: Baby Memorial Hospital,Kozhikode ',font=("Halvetica",15))
                    mylabelKgf15=Label(frame1,text='Time Slot:8PM-2PM',font=("Halvetica",15))
                    mylabelKgf16=Label(frame1,text='Land line : 0471 2917575 ',font=("Halvetica",15))
                    
                    mylabelKgf211=Label(frame2,text='Dr.Radhakrishnan Ellath  ',font=("Halvetica",15))
                    mylabelKgf22=Label(frame2,text='MBBS,MD ',font=("Halvetica",15))
                    mylabelKgf23=Label(frame2,text='GENERAL PHYSICIAN',font=("Halvetica",15))
                    mylabelKgf24=Label(frame2,text='Hospital : Government hospital   Kozhikode',font=("Halvetica",15))
                    mylabelKgf25=Label(frame2,text='Time slot: 1PM-6:30PM',font=("Halvetica",15))
                    mylabelKgf26=Label(frame2,text='Land line :  0471 2834473  ',font=("Halvetica",15))
                    
                    mylabelKgf311=Label(frame3,text='Dr.Hamood harthi ',font=("Halvetica",15))
                    mylabelKgf32=Label(frame3,text='MSc in Physiology ',font=("Halvetica",15))
                    mylabelKgf33=Label(frame3,text='GENERAL PHYSICIAN',font=("Halvetica",15))
                    mylabelKgf34=Label(frame3,text='Hospital : Malabar Hospital,Kozhikode',font=("Halvetica",15))
                    mylabelKgf35=Label(frame3,text='Time slot: 5PM-10PM',font=("Halvetica",15))
                    mylabelKgf36=Label(frame3,text='Land line : 0471 2382869  ',font=("Halvetica",15))
                    
                    mylabelKgf111.grid(row=0,column=0,sticky=W)
                    mylabelKgf12.grid(row=1,column=0,sticky=W)
                    mylabelKgf13.grid(row=2,column=0,sticky=W)
                    mylabelKgf14.grid(row=3,column=0,sticky=W)
                    mylabelKgf15.grid(row=4,column=0,sticky=W)
                    mylabelKgf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelKgf211.grid(row=0,column=0,sticky=W)
                    mylabelKgf22.grid(row=1,column=0,sticky=W)
                    mylabelKgf23.grid(row=2,column=0,sticky=W)
                    mylabelKgf24.grid(row=3,column=0,sticky=W)
                    mylabelKgf25.grid(row=4,column=0,sticky=W)
                    mylabelKgf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelKgf311.grid(row=0,column=0,sticky=W)
                    mylabelKgf32.grid(row=1,column=0,sticky=W)
                    mylabelKgf33.grid(row=2,column=0,sticky=W)
                    mylabelKgf34.grid(row=3,column=0,sticky=W)
                    mylabelKgf35.grid(row=4,column=0,sticky=W)
                    mylabelKgf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                    
                elif Ds_Name.get()=='Obstetrics and Gynaecologist':
                    global mylabelKof111
                    global mylabelKof12
                    global mylabelKof13
                    global mylabelKof14
                    global mylabelKof15
                    global mylabelKof16
                
                    global mylabelKof211
                    global mylabelKof22
                    global mylabelKof23
                    global mylabelKof24
                    global mylabelKof25
                    global mylabelKof26
                    
                    global mylabelKof311
                    global mylabelKof32
                    global mylabelKof33
                    global mylabelKof34
                    global mylabelKof35
                    global mylabelKof36

                    mylabelKof111=Label(frame1,text='Dr. Abdul Vadoodh',font=("Halvetica",15))
                    mylabelKof12=Label(frame1,text='MBBS, DNB Gynecology  ',font=("Halvetica",15))
                    mylabelKof13=Label(frame1,text='Obstetrics and Gynaecologist',font=("Halvetica",15))
                    mylabelKof14=Label(frame1,text='Hospital:Government Women Hospital,Kozhikode',font=("Halvetica",15))
                    mylabelKof15=Label(frame1,text='Time Slot:11AM-5PM',font=("Halvetica",15))
                    mylabelKof16=Label(frame1,text='Land line : 0471 2468629 ',font=("Halvetica",15))
                    
                    mylabelKof211=Label(frame2,text='Dr. Greeshma Chandran  ',font=("Halvetica",15))
                    mylabelKof22=Label(frame2,text='MBBS, MD Gynecology',font=("Halvetica",15))
                    mylabelKof23=Label(frame2,text='Obstetrics and Gynaecologist',font=("Halvetica",15))
                    mylabelKof24=Label(frame2,text='Hospital :  Starcare Hospital,Kozhikode ',font=("Halvetica",15))
                    mylabelKof25=Label(frame2,text='Time slot: 3PM-5PM',font=("Halvetica",15))
                    mylabelKof26=Label(frame2,text='Land line : 0491 2200667  ',font=("Halvetica",15))
                    
                    mylabelKof311=Label(frame3,text='Dr. Radhamani ',font=("Halvetica",15))
                    mylabelKof32=Label(frame3,text='MBBS,MD Gynecology',font=("Halvetica",15))
                    mylabelKof33=Label(frame3,text='Obstetrics and Gynaecologist',font=("Halvetica",15))
                    mylabelKof34=Label(frame3,text='Hospital:Malabar Hospital,Kozhikode',font=("Halvetica",15))
                    mylabelKof35=Label(frame3,text='Time slot : 10AM-12PM',font=("Halvetica",15))
                    mylabelKof36=Label(frame3,text='Land line : 0471 2154458   ',font=("Halvetica",15))
                    
                    mylabelKof111.grid(row=0,column=0,sticky=W)
                    mylabelKof12.grid(row=1,column=0,sticky=W)
                    mylabelKof13.grid(row=2,column=0,sticky=W)
                    mylabelKof14.grid(row=3,column=0,sticky=W)
                    mylabelKof15.grid(row=4,column=0,sticky=W)
                    mylabelKof16.grid(row=5,column=0,sticky=W)
                    
                    mylabelKof211.grid(row=0,column=0,sticky=W)
                    mylabelKof22.grid(row=1,column=0,sticky=W)
                    mylabelKof23.grid(row=2,column=0,sticky=W)
                    mylabelKof24.grid(row=3,column=0,sticky=W)
                    mylabelKof25.grid(row=4,column=0,sticky=W)
                    mylabelKof26.grid(row=5,column=0,sticky=W)
                    
                    mylabelKof311.grid(row=0,column=0,sticky=W)
                    mylabelKof32.grid(row=1,column=0,sticky=W)
                    mylabelKof33.grid(row=2,column=0,sticky=W)
                    mylabelKof34.grid(row=3,column=0,sticky=W)
                    mylabelKof35.grid(row=4,column=0,sticky=W)
                    mylabelKof36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                    
                elif Ds_Name.get()=='Radiologist':
                    global mylabelKrf111
                    global mylabelKrf12
                    global mylabelKrf13
                    global mylabelKrf14
                    global mylabelKrf15
                    global mylabelKrf16
                
                    global mylabelKrf211
                    global mylabelKrf22
                    global mylabelKrf23
                    global mylabelKrf24
                    global mylabelKrf25
                    global mylabelKrf26
                    
                    global mylabelKrf311
                    global mylabelKrf32
                    global mylabelKrf33
                    global mylabelKrf34
                    global mylabelKrf35
                    global mylabelKrf36

                    mylabelKrf111=Label(frame1,text='Dr.Asish Mehra ',font=("Halvetica",15))
                    mylabelKrf12=Label(frame1,text='MBBS, PG in Radiology',font=("Halvetica",15))
                    mylabelKrf13=Label(frame1,text='Radiologist',font=("Halvetica",15))
                    mylabelKrf14=Label(frame1,text='Hospital: Government hospital,Kozhikode',font=("Halvetica",15))
                    mylabelKrf15=Label(frame1,text='Time Slot:10AM-4PM',font=("Halvetica",15))
                    mylabelKrf16=Label(frame1,text='Land line :  0471 2815378  ',font=("Halvetica",15))
            
                    mylabelKrf211=Label(frame2,text='Shibu Mannarath ',font=("Halvetica",15))
                    mylabelKrf22=Label(frame2,text='Doctor Of Medicine',font=("Halvetica",15))
                    mylabelKrf23=Label(frame2,text='Radiologist',font=("Halvetica",15))
                    mylabelKrf24=Label(frame2,text='Hospital :IQRAA Imaging Kozhikode ',font=("Halvetica",15))
                    mylabelKrf25=Label(frame2,text='Time slot: 24hrs',font=("Halvetica",15))
                    mylabelKrf26=Label(frame2,text='Land line : 0471 2654698   ',font=("Halvetica",15))
                    
                    mylabelKrf311=Label(frame3,text='Dr. Surya Sudhakaran ',font=("Halvetica",15))
                    mylabelKrf32=Label(frame3,text='MBBS, MS Radiology ',font=("Halvetica",15))
                    mylabelKrf33=Label(frame3,text='Radiologist',font=("Halvetica",15))
                    mylabelKrf34=Label(frame3,text='Hospital: Starcare Hospital, Kozhikode,',font=("Halvetica",15))
                    mylabelKrf35=Label(frame3,text='Time slot : 6PM-10PM',font=("Halvetica",15))
                    mylabelKrf36=Label(frame3,text='Land line :  0471 2268726   ',font=("Halvetica",15))
                    
                    mylabelKrf111.grid(row=0,column=0,sticky=W)
                    mylabelKrf12.grid(row=1,column=0,sticky=W)
                    mylabelKrf13.grid(row=2,column=0,sticky=W)
                    mylabelKrf14.grid(row=3,column=0,sticky=W)
                    mylabelKrf15.grid(row=4,column=0,sticky=W)
                    mylabelKrf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelKrf211.grid(row=0,column=0,sticky=W)
                    mylabelKrf22.grid(row=1,column=0,sticky=W)
                    mylabelKrf23.grid(row=2,column=0,sticky=W)
                    mylabelKrf24.grid(row=3,column=0,sticky=W)
                    mylabelKrf25.grid(row=4,column=0,sticky=W)
                    mylabelKrf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelKrf311.grid(row=0,column=0,sticky=W)
                    mylabelKrf32.grid(row=1,column=0,sticky=W)
                    mylabelKrf33.grid(row=2,column=0,sticky=W)
                    mylabelKrf34.grid(row=3,column=0,sticky=W)
                    mylabelKrf35.grid(row=4,column=0,sticky=W)
                    mylabelKrf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
                elif Ds_Name.get()=='ENT':
                    global mylabelKnf111
                    global mylabelKnf12
                    global mylabelKnf13
                    global mylabelKnf14
                    global mylabelKnf15
                    global mylabelKnf16
                
                    global mylabelKnf211
                    global mylabelKnf22
                    global mylabelKnf23
                    global mylabelKnf24
                    global mylabelKnf25
                    global mylabelKnf26
                
                    global mylabelKnf311
                    global mylabelKnf32
                    global mylabelKnf33
                    global mylabelKnf34
                    global mylabelKnf35
                    global mylabelKnf36

                    mylabelKnf111=Label(frame1,text='Dr. Aneesh Mishra',font=("Halvetica",15))
                    mylabelKnf12=Label(frame1,text='MBBS, MS ENT',font=("Halvetica",15))
                    mylabelKnf13=Label(frame1,text='ENT',font=("Halvetica",15))
                    mylabelKnf14=Label(frame1,text='Hospital: Government hospital,Kozhikode,',font=("Halvetica",15))
                    mylabelKnf15=Label(frame1,text='Time Slot:9AM-3PM',font=("Halvetica",15))
                    mylabelKnf16=Label(frame1,text='Land line : 0471 2697125 ',font=("Halvetica",15))
            
                    mylabelKnf211=Label(frame2,text='Dr. Umesh Pavukandy',font=("Halvetica",15))
                    mylabelKnf22=Label(frame2,text='MBBS,PG ENT ',font=("Halvetica",15))
                    mylabelKnf23=Label(frame2,text='ENT',font=("Halvetica",15))
                    mylabelKnf24=Label(frame2,text='Hospital : Malabar Hospital,Kozhikode',font=("Halvetica",15))
                    mylabelKnf25=Label(frame2,text='Time slot: 1PM-8PM',font=("Halvetica",15))
                    mylabelKnf26=Label(frame2,text='Land line :  0471 2572568  ',font=("Halvetica",15))
                    
                    mylabelKnf311=Label(frame3,text='Dr. Amal Thomas',font=("Halvetica",15))
                    mylabelKnf32=Label(frame3,text='MBBS, MS ENT ',font=("Halvetica",15))
                    mylabelKnf33=Label(frame3,text='ENT',font=("Halvetica",15))
                    mylabelKnf34=Label(frame3,text='Hospital :Baby Memorial College,Kozhikode',font=("Halvetica",15))
                    mylabelKnf35=Label(frame3,text='Time slot : 10AM-4PM',font=("Halvetica",15))
                    mylabelKnf36=Label(frame3,text='Land line :  0471 2788951    ',font=("Halvetica",15))
                    
                    mylabelKnf111.grid(row=0,column=0,sticky=W)
                    mylabelKnf12.grid(row=1,column=0,sticky=W)
                    mylabelKnf13.grid(row=2,column=0,sticky=W)
                    mylabelKnf14.grid(row=3,column=0,sticky=W)
                    mylabelKnf15.grid(row=4,column=0,sticky=W)
                    mylabelKnf16.grid(row=5,column=0,sticky=W)
                    
                    mylabelKnf211.grid(row=0,column=0,sticky=W)
                    mylabelKnf22.grid(row=1,column=0,sticky=W)
                    mylabelKnf23.grid(row=2,column=0,sticky=W)
                    mylabelKnf24.grid(row=3,column=0,sticky=W)
                    mylabelKnf25.grid(row=4,column=0,sticky=W)
                    mylabelKnf26.grid(row=5,column=0,sticky=W)
                    
                    mylabelKnf311.grid(row=0,column=0,sticky=W)
                    mylabelKnf32.grid(row=1,column=0,sticky=W)
                    mylabelKnf33.grid(row=2,column=0,sticky=W)
                    mylabelKnf34.grid(row=3,column=0,sticky=W)
                    mylabelKnf35.grid(row=4,column=0,sticky=W)
                    mylabelKnf36.grid(row=5,column=0,sticky=W)
                    prjt.configure(background='Light Blue')
# Raising Exception if the Doctors with inputed Speciality are not availabe and by that telling the user that which type of specialists are availabe.
                else:
                    raise Exception('Please Enter Speciality among:'+'\n'+'Cardiologist'+'\n'+'General Physician'+'\n'+'Radiologist'+'\n'+'ENT'+'\n'+'Emergency Medicine Trauma'+'\n'+'Obstetrics and Gynaecologist')  
# Raising Exception if the inputed city's data is not available and telling to user that please use these given city: 
            else:
                raise Exception('Please Enter City:'+'\n'+'Palakkad'+'\n'+'Kozhikode')
    except  Exception as e:
        global mylabel1
        mylabel1=Label(frame1,text=e,fg='Dark Red',font=("Halvetica",15))
        mylabel1.grid(row=0,column=0,columnspan=4,pady=10)
        prjt.configure(background='Red')
        
  def Clear():
    location.delete(0,END)
    Ds_Name.delete(0,END)
    try:
            mylabelf111.grid_forget()
            mylabelf12.grid_forget()
            mylabelf13.grid_forget()
            mylabelf14.grid_forget()
            mylabelf15.grid_forget()
            mylabelf16.grid_forget()
            
            mylabelf211.grid_forget()
            mylabelf22.grid_forget()
            mylabelf23.grid_forget()
            mylabelf24.grid_forget()
            mylabelf25.grid_forget()
            mylabelf26.grid_forget()
                            
            mylabelf311.grid_forget()
            mylabelf32.grid_forget()
            mylabelf33.grid_forget()
            mylabelf34.grid_forget()
            mylabelf35.grid_forget()
            mylabelf36.grid_forget()
    except Exception :
        pass
    try:
            mylabelef111.grid_forget()
            mylabelef12.grid_forget()
            mylabelef13.grid_forget()
            mylabelef14.grid_forget()
            mylabelef15.grid_forget()
            mylabelef16.grid_forget()
            
            mylabelef211.grid_forget()
            mylabelef22.grid_forget()
            mylabelef23.grid_forget()
            mylabelef24.grid_forget()
            mylabelef25.grid_forget()
            mylabelef26.grid_forget()
                            
            mylabelef311.grid_forget()
            mylabelef32.grid_forget()
            mylabelef33.grid_forget()
            mylabelef34.grid_forget()
            mylabelef35.grid_forget()
            mylabelef36.grid_forget()
    except Exception:
        pass
    try:
            mylabelgf111.grid_forget()
            mylabelgf12.grid_forget()
            mylabelgf13.grid_forget()
            mylabelgf14.grid_forget()
            mylabelgf15.grid_forget()
            mylabelgf16.grid_forget()
            
            mylabelgf211.grid_forget()
            mylabelgf22.grid_forget()
            mylabelgf23.grid_forget()
            mylabelgf24.grid_forget()
            mylabelgf25.grid_forget()
            mylabelgf26.grid_forget()
                            
            mylabelgf311.grid_forget()
            mylabelgf32.grid_forget()
            mylabelgf33.grid_forget()
            mylabelgf34.grid_forget()
            mylabelgf35.grid_forget()
            mylabelgf36.grid_forget()
    except Exception:
        pass
    try:
            mylabelof111.grid_forget()
            mylabelof12.grid_forget()
            mylabelof13.grid_forget()
            mylabelof14.grid_forget()
            mylabelof15.grid_forget()
            mylabelof16.grid_forget()
            
            mylabelof211.grid_forget()
            mylabelof22.grid_forget()
            mylabelof23.grid_forget()
            mylabelof24.grid_forget()
            mylabelof25.grid_forget()
            mylabelof26.grid_forget()
                            
            mylabelof311.grid_forget()
            mylabelof32.grid_forget()
            mylabelof33.grid_forget()
            mylabelof34.grid_forget()
            mylabelof35.grid_forget()
            mylabelof36.grid_forget()
    except Exception:
         pass
        try:
            mylabelrf111.grid_forget()
            mylabelrf12.grid_forget()
            mylabelrf13.grid_forget()
            mylabelrf14.grid_forget()
            mylabelrf15.grid_forget()
            mylabelrf16.grid_forget()
            
            mylabelrf211.grid_forget()
            mylabelrf22.grid_forget()
            mylabelrf23.grid_forget()
            mylabelrf24.grid_forget()
            mylabelrf25.grid_forget()
            mylabelrf26.grid_forget()
                            
            mylabelrf311.grid_forget()
            mylabelrf32.grid_forget()
            mylabelrf33.grid_forget()
            mylabelrf34.grid_forget()
            mylabelrf35.grid_forget()
            mylabelrf36.grid_forget()
    except Exception:
        pass   
    try:
            mylabelnf111.grid_forget()
            mylabelnf12.grid_forget()
            mylabelnf13.grid_forget()
            mylabelnf14.grid_forget()
            mylabelnf15.grid_forget()
            mylabelnf16.grid_forget()
            
            mylabelnf211.grid_forget()
            mylabelnf22.grid_forget()
            mylabelnf23.grid_forget()
            mylabelnf24.grid_forget()
            mylabelnf25.grid_forget()
            mylabelnf26.grid_forget()
                        
            mylabelnf311.grid_forget()
            mylabelnf32.grid_forget()
            mylabelnf33.grid_forget()
            mylabelnf34.grid_forget()
            mylabelnf35.grid_forget()
            mylabelnf36.grid_forget()
    except Exception:
        pass 
        
    try:
            mylabelKf111.grid_forget()
            mylabelKf12.grid_forget()
            mylabelKf13.grid_forget()
            mylabelKf14.grid_forget()
            mylabelKf15.grid_forget()
            mylabelKf16.grid_forget()
            
            mylabelKf211.grid_forget()
            mylabelKf22.grid_forget()
            mylabelKf23.grid_forget()
            mylabelKf24.grid_forget()
            mylabelKf25.grid_forget()
            mylabelKf26.grid_forget()
                            
            mylabelKf311.grid_forget()
            mylabelKf32.grid_forget()
            mylabelKf33.grid_forget()
            mylabelKf34.grid_forget()
            mylabelKf35.grid_forget()
            mylabelKf36.grid_forget()
    except Exception :
        pass
    try:
            mylabelKef111.grid_forget()
            mylabelKef12.grid_forget()
            mylabelKef13.grid_forget()
            mylabelKef14.grid_forget()
            mylabelKef15.grid_forget()
            mylabelKef16.grid_forget()
            
            mylabelKef211.grid_forget()
            mylabelKef22.grid_forget()
            mylabelKef23.grid_forget()
            mylabelKef24.grid_forget()
            mylabelKef25.grid_forget()
            mylabelKef26.grid_forget()
                            
            mylabelKef311.grid_forget()
            mylabelKef32.grid_forget()
            mylabelKef33.grid_forget()
            mylabelKef34.grid_forget()
            mylabelKef35.grid_forget()
            mylabelKef36.grid_forget()
    except Exception:
        pass
    try:
            mylabelKgf111.grid_forget()
            mylabelKgf12.grid_forget()
            mylabelKgf13.grid_forget()
            mylabelKgf14.grid_forget()
            mylabelKgf15.grid_forget()
            mylabelKgf16.grid_forget()
            
            mylabelKgf211.grid_forget()
            mylabelKgf22.grid_forget()
            mylabelKgf23.grid_forget()
            mylabelKgf24.grid_forget()
            mylabelKgf25.grid_forget()
            mylabelKgf26.grid_forget()
                            
            mylabelKgf311.grid_forget()
            mylabelKgf32.grid_forget()
            mylabelKgf33.grid_forget()
            mylabelKgf34.grid_forget()
            mylabelKgf35.grid_forget()
            mylabelKgf36.grid_forget()
    except Exception:
        pass
    try:
            mylabelKof111.grid_forget()
            mylabelKof12.grid_forget()
            mylabelKof13.grid_forget()
            mylabelKof14.grid_forget()
            mylabelKof15.grid_forget()
            mylabelKof16.grid_forget()
            
            mylabelKof211.grid_forget()
            mylabelKof22.grid_forget()
            mylabelKof23.grid_forget()
            mylabelKof24.grid_forget()
            mylabelKof25.grid_forget()
            mylabelKof26.grid_forget()
                            
            mylabelKof311.grid_forget()
            mylabelKof32.grid_forget()
            mylabelKof33.grid_forget()
            mylabelKof34.grid_forget()
            mylabelKof35.grid_forget()
            mylabelKof36.grid_forget()
    except Exception:
        pass
    try:
            mylabelKrf111.grid_forget()
            mylabelKrf12.grid_forget()
            mylabelKrf13.grid_forget()
            mylabelKrf14.grid_forget()
            mylabelKrf15.grid_forget()
            mylabelKrf16.grid_forget()
            
            mylabelKrf211.grid_forget()
            mylabelKrf22.grid_forget()
            mylabelKrf23.grid_forget()
            mylabelKrf24.grid_forget()
            mylabelKrf25.grid_forget()
            mylabelKrf26.grid_forget()
                            
            mylabelKrf311.grid_forget()
            mylabelKrf32.grid_forget()
            mylabelKrf33.grid_forget()
            mylabelKrf34.grid_forget()
            mylabelKrf35.grid_forget()
            mylabelKrf36.grid_forget()
    except Exception:
        pass   
    try:
            mylabelKnf111.grid_forget()
            mylabelKnf12.grid_forget()
            mylabelKnf13.grid_forget()
            mylabelKnf14.grid_forget()
            mylabelKnf15.grid_forget()
            mylabelKnf16.grid_forget()
            
            mylabelKnf211.grid_forget()
            mylabelKnf22.grid_forget()
            mylabelKnf23.grid_forget()
            mylabelKnf24.grid_forget()
            mylabelKnf25.grid_forget()
            mylabelKnf26.grid_forget()
                        
            mylabelKnf311.grid_forget()
            mylabelKnf32.grid_forget()
            mylabelKnf33.grid_forget()
            mylabelKnf34.grid_forget()
            mylabelKnf35.grid_forget()
            mylabelKnf36.grid_forget()
    except Exception:
        pass 
    try:
        mylabel1.grid_forget()
    except Exception :
        pass
    

# Create Entry boxexs
location=Entry(prjt,width=20)
location.grid(row=0,column=1,pady=5)
Ds_Name=Entry(prjt,width=20)
Ds_Name.grid(row=0,column=3,pady=5)

# # creating labels
loctl=Label(prjt,text='Location')
loctl.grid(row=0,column=0,pady=5)
Ds=Label(prjt,text='Doctor Speciality')
Ds.grid(row=0,column=2,pady=5)



# create buttons
Sbtn=Button(prjt,text='Search',command=DocList)
Sbtn.grid(row=1,column=0,columnspan=4,pady=10,ipadx=202)

okbtn=Button(prjt,text='Ok',command=Clear)
okbtn.grid(row=6,column=0,columnspan=4,pady=10)
    





prjt.mainloop()
