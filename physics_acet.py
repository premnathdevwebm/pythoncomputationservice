import json
import math

class PHY_acet:
    def __init__(self, arg):
        self.arg = arg
        
    def VB_Mag(self):
        argument = self.arg[0:]
        def CR_l(x,y):
            ans = x+(y*lc)
            return ans
        def CR_b(x,y):
            return x+(y*lc)
        def l2(x):
            return x**2
        def b2(x):
            return x**2
        
        lc = float(argument[1])
        CR1 = CR_l(float(argument[4]),float(argument[5]))
        CR2 = CR_l(float(argument[7]),float(argument[8]))
        CR3 = CR_l(float(argument[10]),float(argument[11]))
        CR4 = CR_l(float(argument[13]),float(argument[14]))
        CR5 = CR_l(float(argument[16]),float(argument[17]))
        
        CRl_Mean = round((CR1+CR2+CR3+CR4+CR5)/5,2)
        
        OR1=CR_l(float(argument[23]),float(argument[24]))
        OR2=CR_l(float(argument[27]),float(argument[28]))
        OR3=CR_l(float(argument[31]),float(argument[32]))
        OR4=CR_l(float(argument[35]),float(argument[36]))
        OR5=CR_l(float(argument[39]),float(argument[40]))
        
        CRb1= CR_b(OR1,(float(argument[14])))
        CRb2= CR_b(OR2,(float(argument[14])))
        CRb3= CR_b(OR3,(float(argument[14])))
        CRb4= CR_b(OR4,(float(argument[14])))
        CRb5= CR_b(OR5,(float(argument[14])))
        
        CRb_Mean = round((CRb1+CRb2+CRb3+CRb4+CRb5)/5,2)
        
        T1= float(argument[46])
        T2= float(argument[49])
        T3= float(argument[51])
        T4= float(argument[53])
        T5= float(argument[56])
        T6= float(argument[58])
        
        Mean_T1 = round((T1+T2+T3)/3,2)
        Mean_T2 = round((T4+T5+T6)/3,2)
        Mean_T= round((Mean_T1+Mean_T2)/2,2)
        
        length=round((l2(CRl_Mean))/10,2)
        breadth=round((b2(CRb_Mean))/100,2)
        
        lb=round((length+breadth)/12,3)
        lb_n= lb*10
        
        Inertia = round(((float(argument[44]))*lb_n)*10/1000,3)
        
        T= round(Mean_T**2,1)      
        Mh= round((39.43 * Inertia)/T,2)
        m=round((Mh/(2*CRl_Mean))*10,3)

        return (json.dumps({"Result":[{"Vibrational Magnetometer":"Length of the bar magnet ",
                                     "Mean(length)" : str(CRl_Mean),"Mean(breadth)":str(CRb_Mean),"Time period of oscillator":str(Mean_T),
                                     "Inertia":str(Inertia),"The magnetic moment of the given bar magnet(Mh)":str(Mh)+"x 10^-5 Am^2",
                                     "The pole strength of the given bar magnet(m)":str(m)+"x10^-4 Am"}]}))
    
    #result
    def half(self):
        argument = self.arg[0:]
        def TR(x,y):
            return(x+(y*lc)/100)
        def VA(x,y):
            return(x-y)
        def Va(x,y):
            return(x-y)
        def M(x,y):
            return((x+y)/2)
        def J(x):
            return((x*0.021))
        def deg(x,y):
            return(-(x/y))
        
        lc=float(argument[1])
        I_TR1=round(TR(float(argument[3]),float(argument[4])),2)
        I_TR2=round(TR(float(argument[14]),float(argument[15])),2)
        I_TR3=round(TR(float(argument[25]),float(argument[26])),2)
        I_TR4=round(TR(float(argument[36]),float(argument[37])),2)
        I_TR5=round(TR(float(argument[47]),float(argument[48])),2)

        F_TR1=TR(float(argument[6]),float(argument[7]))
        F_TR2=TR(float(argument[17]),float(argument[18]))
        F_TR3=TR(float(argument[28]),float(argument[29]))
        F_TR4=TR(float(argument[39]),float(argument[40]))
        F_TR5=TR(float(argument[50]),float(argument[51]))

        AI1=round(VA(I_TR2,I_TR1),2)
        AI2= round(VA(I_TR3,I_TR1),2)
        AI3=round(VA(I_TR4,I_TR1),2)
        AI4= round(VA(I_TR5,I_TR1),2)
        
        AF1= round(VA(F_TR2,F_TR1),2)
        AF2=round(VA(F_TR3,F_TR1),2)
        AF3=round(VA(F_TR4,F_TR1),2)
        AF4=round(VA(F_TR5,F_TR1),2) 
        
        Mean1=round(M(AI1,AF1),2)
        Mean2=round(M(AI2,AF2),2)
        Mean3=round(M(AI3,AF3),2)
        Mean4=round(M(AI4,AF4),2)
        
        L2= J(float(argument[6]))
        L3= J(float(argument[11]))
        L4= J(float(argument[16]))
        L5= J(float(argument[21]))
        S1=round(deg(Mean1,L2),2)
        S2= round(deg(Mean2,L3),2)
        S3= round(deg(Mean3,L4),2)
        S4= round(deg(Mean4,L5),2)
        S=(S1+S2+S3+S4)/4

        print(json.dumps({"ans":[{"Initial darkness: TR":str(I_TR1)+", "+ str(I_TR2)+", "+str(I_TR3)+", "+str(I_TR4)+", "+str(I_TR5),
                                  "Final darkness: TR":str(F_TR1)+", "+ str(F_TR2)+", "+str(F_TR3)+", "+str(F_TR4)+", "+str(F_TR5),
                                  "Initial darkness θ (deg)":str(AI1)+", "+ str(AI2)+", "+str(AI3)+", "+str(AI4),
                                  "Final darkness θ (deg)":str(AF1)+", "+ str(AF2)+", "+str(AF3)+", "+str(AF4),
                                  "Mean θ (deg)":str(Mean1)+", "+str(Mean2)+", "+str(Mean3)+", "+str(Mean4),
                                  "The specific rotator of an optically active solution is determined and found to be":str(S)+"deg dm-1 cc-1"}]}))
        
        #result
    def Air_wed(self):
        argument = self.arg[0:]
        def CR(x,y):
            return (x+(y*lc))
        def W5(x,y):
            return (y-x)
        def MW(x):
            return(x/5)
        
        lc = float(argument[1])
        CR1= CR(float(argument[3]),float(argument[4]))
        CR2= CR(float(argument[8]),float(argument[9]))
        CR3= CR(float(argument[13]),float(argument[14]))
        CR4= CR(float(argument[18]),float(argument[19]))
        CR5= CR(float(argument[23]),float(argument[24]))
        CR6= CR(float(argument[28]),float(argument[29]))
        CR7= CR(float(argument[33]),float(argument[34]))
        CR8= CR(float(argument[38]),float(argument[39]))
        CR9= CR(float(argument[43]),float(argument[44]))
        CR10=CR(float(argument[48]),float(argument[49]))
        CR11=CR(float(argument[53]),float(argument[54]))
        
        Width_2= (W5(CR1,CR2))
        Width_3= (W5(CR2,CR3))
        Width_4= (W5(CR3,CR4))
        Width_5= (W5(CR4,CR5))
        Width_6= (W5(CR5,CR6))
        Width_7= (W5(CR6,CR7))
        Width_8= (W5(CR7,CR8))
        Width_9= (W5(CR8,CR9))
        Width_10= (W5(CR9,CR10))
        Width_11= (W5(CR10,CR11))
        
        Mean_width2= MW(Width_2)
        Mean_width3= MW(Width_3)
        Mean_width4= MW(Width_4)
        Mean_width5= MW(Width_5)
        Mean_width6= MW(Width_6)
        Mean_width7= MW(Width_7)
        Mean_width8= MW(Width_8)
        Mean_width9= MW(Width_9)
        Mean_width10=MW (Width_10)
        Mean_width11= MW(Width_11)
        
        MeanBeta= round((Mean_width2 + Mean_width3+Mean_width4+Mean_width5+Mean_width6+Mean_width7+Mean_width8+Mean_width9+Mean_width10+Mean_width11)/12,4)
       
        R1 = CR(float(argument[59]),float(argument[60]))
        R2 = CR(float(argument[63]),float(argument[64]))
        
        l= round((R1-R2),3)
        t= ((5896*l)/(2*MeanBeta))
        ts=round(t/1000000,3)
        
        print(json.dumps({"ans":[{"Mean frindge width(β)":str(MeanBeta)+"x 10-2 m","The distance between edge of contact and wire(l)":str(l)+"m","Thickness of given specimen is found by forming interfernce fringe using air wedge arrangement - Thickness ofspeciemnt(t)=":str(ts)}]}))
    
    
    def prism(self):
        argument = self.arg[0:]
        def TR(x,y):
            return(x+(y*lc))  
        def VA(x,y):
            return (y-x)
        def VB(x,y):
            return(x-y)
        
        lc = float(argument[1])
        tr_al= TR(float(argument[2]),float(argument[3]))
        tr_bl= TR(float(argument[5]),float(argument[6]))
        tr_ar= TR(float(argument[9]),float(argument[10]))
        tr_br= TR(float(argument[12]),float(argument[13]))
        
        trA= round(VA(tr_al,tr_ar))
        trB=VB(tr_bl,tr_br)
        VA= round(trA,2)
        VB=round(trB/2,2)
        A= round((VA+VB)/4)

        Dtr_a=round(TR(float(argument[18]),float(argument[19])),2)
        Vtr_a=round(TR(float(argument[28]),float(argument[29])),2)
        Btr_a=round(TR(float(argument[38]),float(argument[39])),2)
        BGtr_a=round(TR(float(argument[48]),float(argument[49])),2)
        Gtr_a=round(TR(float(argument[58]),float(argument[59])),2)
        Ytr_a=round(TR(float(argument[68]),float(argument[69])),2)
        Otr_a=round(TR(float(argument[78]),float(argument[79])),2)
        Rtr_a=round(TR(float(argument[88]),float(argument[89])),2)

        Dtr_b=round(TR(float(argument[21]),float(argument[22])),2)
        Vtr_b=round(TR(float(argument[31]) ,float(argument[32])),2)
        Btr_b=round(TR(float(argument[41]),float(argument[42])),2)
        BGtr_b=round(TR(float(argument[51]),float(argument[52])),2)
        Gtr_b=round(TR(float(argument[61]),float(argument[62])),2)
        Ytr_b=round(TR(float(argument[71]),float(argument[72])),2)
        Otr_b=round(TR(float(argument[81]),float(argument[82])),2)
        Rtr_b=round(TR(float(argument[83]),float(argument[84])),2)


        vva= round((Dtr_a - Vtr_a),2)
        bva= round((Dtr_a - Btr_a),2)
        bgva=round((Dtr_a - BGtr_a),2)
        gva= round((Dtr_a - Gtr_a),2)
        yva= round((Dtr_a - Ytr_a),2)
        ova= round((Dtr_a - Otr_a),2)
        rva=round(( Dtr_a - Rtr_a),2)

        degree= Dtr_b - 366

        vvb= round((degree - Vtr_b),2)
        bvb= round((degree - Btr_b),2)
        bgvb= round((degree - BGtr_b),2)
        gvb= round((degree - Gtr_b),2)
        yvb= round((degree - Ytr_b),2)
        ovb= round((degree - Otr_b),2)
        rvb= round((degree - Rtr_b),2)

        MeanD1= round((vva+vvb)/2,2)
        MeanD2= round((bva+bvb)/2,2)
        MeanD3= round((bgva+bgvb)/2,2)
        MeanD4= round((gva+gvb)/2,2)
        MeanD5= round((yva+yvb)/2,2)
        MeanD6= round((ova+ovb)/2,2)
        MeanD7= round((rva+rvb)/2,2)

        V=round((math.sin(math.radians(A+MeanD1)/2))/(math.sin(math.radians(A/2))),4)
        B=round((math.sin(math.radians(A+MeanD2)/2))/(math.sin(math.radians(A/2))),4)        
        BG=round((math.sin(math.radians(A+MeanD3)/2))/(math.sin(math.radians(A/2))),4)        
        G=round((math.sin(math.radians(A+MeanD4)/2))/(math.sin(math.radians(A/2))),4)        
        Y=round((math.sin(math.radians(A+MeanD5)/2))/(math.sin(math.radians(A/2))),4)        
        O=round((math.sin(math.radians(A+MeanD6)/2))/(math.sin(math.radians(A/2))),4)
        R=round((math.sin(math.radians(A+MeanD7)/2))/(math.sin(math.radians(A/2))),4)      

        mu1=V
        mu2=BG
        mu3=Y
        mu4=R
        mu5=B
        mu6=G
        mu7=R
        mu8=O

        MU1 = round((mu1+mu5)/2,2)
        MU2=  round((mu2+mu6)/2,2)
        MU3=  round((mu3+mu7)/2,2)
        MU4=  round((mu8+mu4)/2,2)
        
        W1=round(((mu1-mu5)/(MU1-1)),4)
        W2=round(((mu2-mu6)/(MU2-1)),4)
        W3=round(((mu3-mu7)/(MU3-1)),4)
        W4=round(((mu8-mu4)/(MU4-1)),4)
        power=round((W1+W2+W3+W4)/4,4)
        
        print(json.dumps({"ans":[{"The angle of the given prism :(VA)":str(VA) +"degree","(VB)":str(VB)+"degree","A":str(A),"The dispersion power of the given prism W":str(power)+" No unit"}]}))

    def laser(self):
        argument= self.arg[0:]
        def TR(x,y):
            return(x+(y*0.01))  
        
        def VA(x,y):
            diff = abs(y-x)
            if diff > 30:
             return abs(math.radians(y)-math.radians(x))
            else:
             return abs(y-x)  
         
        def theta45(a,b,c):
            avg = (b+c)/2
            thetaa = math.degrees(math.atan(b/45))
            lamda = (math.sin(math.radians(thetaa))/(a*N))*10**10
            return lamda
        
        def theta50(a,b,c):
            avg = (b+c)/2
            thetaa = math.degrees(math.atan(b/50))
            lamda = (math.sin(math.radians(thetaa))/(a*N))*10**10
            return lamda
        
        def theta55(a,b,c):
            avg = (b+c)/2
            thetaa = math.degrees(math.atan(b/55))
            lamda = (math.sin(math.radians(thetaa))/(a*N))*10**10
            return lamda
        
        cr_al= round(TR(float(argument[1]),float(argument[2])),2)
        cr_bl= round(TR(float(argument[4]),float(argument[5])),2)
        cr_ar= round(TR(float(argument[11]),float(argument[12])),2)
        cr_br= round(TR(float(argument[14]),float(argument[15])),2)
        
        DA=round(VA(cr_al,cr_ar),2)
        DB=round(VA(cr_bl,cr_br),2)
        MeanA=round(((DA+DB)/4),2)
        
        N=math.sin(math.radians(3.52))/(5893)
        
        theta1=theta45(float(argument[21]),float(argument[22]),float(argument[25]))
        theta2=theta45(float(argument[30]),float(argument[32]),float(argument[35]))
        theta3=theta45(float(argument[39]),float(argument[40]),float(argument[43]))
        theta4=theta45(float(argument[48]),float(argument[49]),float(argument[52]))
        theta5=theta45(float(argument[57]),float(argument[58]),float(argument[61]))
        
        theta6=theta50(float(argument[66]),float(argument[67]),float(argument[70]))
        theta7=theta50(float(argument[75]),float(argument[76]),float(argument[79]))
        theta8=theta50(float(argument[84]),float(argument[85]),float(argument[88]))
        theta9=theta50(float(argument[93]),float(argument[94]),float(argument[97]))
        theta10=theta50(float(argument[102]),float(argument[103]),float(argument[106]))
        
        theta11=theta55(float(argument[111]),float(argument[112]),float(argument[115]))
        theta12=theta55(float(argument[120]),float(argument[121]),float(argument[124]))
        theta13=theta55(float(argument[129]),float(argument[130]),float(argument[133]))
        theta14=theta55(float(argument[138]),float(argument[139]),float(argument[142]))
        theta15=theta55(float(argument[147]),float(argument[148]),float(argument[151]))
        
        avg=(theta1+theta2+theta3+theta4+theta5+theta6+theta7+theta8+theta9+theta10+theta11+theta12+theta13+theta14+theta15)/15
        avground=round(avg,2)
        
        print(json.dumps({"ans":[{"Vernier A (Left)":str(cr_al)+", "+"(Right) : "+str(cr_ar),"Vernier B (Left)":str(cr_bl)+", "+"(Right) : "+str(cr_br),"Vernier A":str(DA)+", "+"Vernier B : "+str(DB),"Mean θ":str(MeanA),"N = sinθ / mλ":str(N),"Wave Length of given light Source in Amstrong":str(avground)+"Amstrong","Wave Length of given light Source in meter":str(avground)+"*10^-10meter"}]}))
    
    
    def lee(self):
        argument = self.arg[0:]
        
        def CR(x,y):
            return(x+(y*lc))     
        def CROr(x):
            return(x+(zc*lc))
        def m(a,b,c,d,e):
            return((a+b+c+d+e)/10)
        def mean(a,b,c,d,e):
            return((a+b+c+d+e)/5)
        
        lc=float(argument[1])
        zc=float(argument[23])
        
        R_CR1=round(CR(float(argument[4]),float(argument[5])),3)
        R_CR2=round(CR(float(argument[7]),float(argument[8])),3)
        R_CR3=CR(float(argument[10]),float(argument[11]))
        R_CR4=CR(float(argument[13]),float(argument[14]))
        R_CR5=CR(float(argument[16]),float(argument[17]))
        Mean_R=round(m(R_CR1,R_CR2,R_CR3,R_CR4,R_CR5),3)

        D_CR1=CR(float(argument[24]),float(argument[25]))
        D_CR2=CR(float(argument[28]),float(argument[29]))
        D_CR3=CR(float(argument[32]),float(argument[33]))
        D_CR4=CR(float(argument[36]),float(argument[37]))
        D_CR5=CR(float(argument[40]),float(argument[41]))
        
        CR1=round(CROr(D_CR1),2)
        CR2=round(CROr(D_CR2),2)
        CR3=round(CROr(D_CR3),2)
        CR4=round(CROr(D_CR4),2)
        CR5=round(CROr(D_CR5),2)
        Mean_D=round(mean(CR1,CR2,CR3,CR4,CR5),3)

        H_CR1=CR(float(argument[47]),float(argument[48]))
        H_CR2=CR(float(argument[51]),float(argument[52]))
        H_CR3=CR(float(argument[55]),float(argument[56]))
        H_CR4=CR(float(argument[59]),float(argument[60]))
        H_CR5=CR(float(argument[63]),float(argument[64]))
        
        HCR1=round(CROr(H_CR1),2)
        HCR2=round(CROr(H_CR2),2)
        HCR3=round(CROr(H_CR3),2)
        HCR4=round(CROr(H_CR4),2)
        HCR5=round(CROr(H_CR5),2)
        Mean_H=round(mean(HCR1,HCR2,HCR3,HCR4,HCR5),3)
        
        theta = float(argument[68])-float(argument[69])
        K1=round((float(argument[90])*10**-3*float(argument[91])*float(argument[92])*Mean_D*10**-3)/(3.14*theta*((Mean_R*10**-2)**2)),4)
        K2=round((Mean_R*10**-2+(2*Mean_H*10**-3))/(2*Mean_R*10**-2+(2*Mean_H*10**-3)),4)
        K=round(K1*K2,4)
        print(json.dumps({"ans":[{"Determination of radius of given Metallic disc using Vernier Caliper"" "+"CR":str(R_CR1)+", "+str(R_CR2)+", "+str(R_CR3)+", "+str(R_CR4)+", "+str(R_CR5), "Mean radius(r)":str(Mean_R)+" m","Determination of thickness of the bad conductor using Screw gauge"" "+"OR":str(D_CR1)+", "+str(D_CR2)+", "+str(D_CR3)+", "+str(D_CR4)+", "+str(D_CR5),"CR":str(CR1)+", "+str(CR2)+", "+str(CR3)+", "+str(CR4)+", "+str(CR5),"Mean diameter(d)":str(Mean_D),"Determination of thickness of Lee's disc using Screw gauge"" "+ "OR":str(H_CR1)+", "+str(H_CR2)+", "+str(H_CR3)+", "+str(H_CR4)+", "+str(H_CR5), "Correct Reading(CR)":str(HCR1)+", "+str(HCR2)+", "+str(HCR3)+", "+str(HCR4)+", "+str(HCR5),"Mean height(h)":str(Mean_H),"The thermal conductivity of a bad conductor using lee's disc method":str(K)+" W m k"}]}))

    #doubt
    def newton(self):
        argument = self.arg[0:]
        def CR(x,y):
            return (x+(y*lc))
        def D(x,y):
            return ((x-y)**2)
        def MW(x):
            return(x/5)
        lc=float(argument[1])
        CR1=CR(float(argument[2]),float(argument[3]))
        CR2=CR(float(argument[11]),float(argument[12]))
        CR3=CR(float(argument[20]),float(argument[21]))
        CR4=CR(float(argument[29]),float(argument[30]))
        CR5=CR(float(argument[38]),float(argument[39]))
        CR6=CR(float(argument[47]),float(argument[48]))
        CR7=CR(float(argument[56]),float(argument[57]))      
        CR8=CR(float(argument[65]),float(argument[69]))     
        CR9=CR(float(argument[74]),float(argument[75]))    
        CR10=CR(float(argument[83]),float(argument[84]))    
        CR11=CR(float(argument[92]),float(argument[93]))
        
        CRR1=CR(float(argument[5]),float(argument[6]))
        CRR2=CR(float(argument[14]),float(argument[15]))
        CRR3=CR(float(argument[23]),float(argument[24]))
        CRR4=CR(float(argument[32]),float(argument[33]))
        CRR5=CR(float(argument[41]),float(argument[42]))
        CRR6=CR(float(argument[50]),float(argument[51]))
        CRR7=CR(float(argument[59]),float(argument[60]))
        CRR8=CR(float(argument[68]),float(argument[69]))
        CRR9=CR(float(argument[77]),float(argument[78]))
        CRR10=CR(float(argument[86]),float(argument[87]))
        CRR11=CR(float(argument[95]),float(argument[96]))

        D1= round(D(CR1,CRR1),3)
        D2= round(D(CR2,CRR2),3)
        D3= round(D(CR3,CRR3),3)
        D4= round(D(CR4,CRR4),3)
        D5= round(D(CR5,CRR5),3)
        D6= round(D(CR6,CRR6),3)
        D7= round(D(CR7,CRR7),3)
        D8= round(D(CR8,CRR8),3)
        D9= round(D(CR9,CRR9),3)
        D10= round(D(CR10,CRR10),3)
        D11= round(D(CR11,CRR11),3)

        d1= ((D6-D1))
        d2= ((D7-D2))
        d3= ((D8-D3))
        d4= ((D9-D4))
        d5= ((D10-D5))

        MeanR1=round((d1+d2+d3+d4+d5)/5,6)
       
        CR_1=CR(float(argument[102]),float(argument[103]))
        CR_2=CR(float(argument[111]),float(argument[112]))
        CR_3=CR(float(argument[120]),float(argument[121]))
        CR_4=CR(float(argument[129]),float(argument[130]))
        CR_5=CR(float(argument[138]),float(argument[139]))
        CR_6=CR(float(argument[147]),float(argument[148]))
        CR_7=CR(float(argument[156]),float(argument[157]))
        CR_8=CR(float(argument[165]),float(argument[166]))
        CR_9=CR(float(argument[174]),float(argument[175]))
        CR_10=CR(float(argument[183]),float(argument[184]))
        CR_11=CR(float(argument[192]),float(argument[193]))

        CR_R1=CR(float(argument[105]),float(argument[106]))
        CR_R2=CR(float(argument[114]),float(argument[115]))
        CR_R3=CR(float(argument[123]),float(argument[124]))
        CR_R4=CR(float(argument[132]),float(argument[133]))
        CR_R5=CR(float(argument[141]),float(argument[142]))
        CR_R6=CR(float(argument[150]),float(argument[151]))
        CR_R7=CR(float(argument[159]),float(argument[160]))
        CR_R8=CR(float(argument[168]),float(argument[169]))
        CR_R9=CR(float(argument[177]),float(argument[178]))
        CR_R10=CR(float(argument[186]),float(argument[187]))
        CR_R11=CR(float(argument[195]),float(argument[196]))

        D_1= round(D(CR_1,CR_R1),3)
        D_2= round(D(CR_2,CR_R2),3)
        D_3= round(D(CR_3,CR_R4),3)
        D_4= round(D(CR_4,CR_R4),3)
        D_5= round(D(CR_5,CR_R5),3)
        D_6= round(D(CR_6,CR_R6),3)
        D_7= round(D(CR_7,CR_R7),3)
        D_8= round(D(CR_8,CR_R8),3)
        D_9= round(D(CR_9,CR_R9),3)
        D_10= round(D(CR_10,CR_R10),3)
        D_11= round(D(CR_11,CR_R11),3)

        d_1= ((D_6-D_1))
        d_2= ((D_7-D_2))
        d_3= ((D_8-D_3))
        d_4= ((D_9-D_4))
        d_5= ((D_10-D_5))
        MeanR2=round((d_1+d_2+d_3+d_4+d_5)/5,6)
        R1= (MeanR1/353580)
        R2=(MeanR2/353580)
        R= round(((R1+R2)/2),10)
        f1= 1/R1
        f2=1/R2
        f=f1+f2
        ftemp=1/(0.5*f)
        F=round(ftemp,10)
        print(json.dumps({"ans":[{"Mean[R1]":str(MeanR1)+"10^-4 m^2","Mean[R2]":str(MeanR2)+"10^-4 m^2","Radial of curvature of the given convex lens(R)=":str(R),"Focal length of the given convex lens(f)":str(F)}]}))

    def Radial(self):
            argument = self.arg[0:]
            def CR(x,y):
                return (x+(y*lc))
            
            lc=float(argument[1])
            OCR1=round(CR(float(argument[6]),float(argument[7])),3)
            OCR2=round(CR(float(argument[14]),float(argument[15])),3)
            OCR3=round(CR(float(argument[21]),float(argument[22])),3)
            OCR4=round(CR(float(argument[29]),float(argument[30])),3)
            
            ICR1=round(CR(float(argument[9]),float(argument[10])),3)
            ICR2=round(CR(float(argument[17]),float(argument[18])),3)
            ICR3=round(CR(float(argument[24]),float(argument[25])),3)
            ICR4=round(CR(float(argument[32]),float(argument[33])),3)
            
            D1=round(OCR1-OCR2,3)
            D2=round(ICR1-ICR2,3)
            D3=round(OCR4-OCR3,3)
            D4=round(ICR4-ICR3,3)
            
            R1=round((D1+D2)/2,3)
            R2=round((D3+D4)/2,3)
            t=float(argument[5])
            w1=float(argument[36])
            w2= float(argument[37])
            c1= float(argument[38])
            c2= float(argument[39])
            l= float(argument[40])
            
            Initial_temp=round(float(argument[2])+273)
            Final_temp=round(float(argument[4])+273)
            temp= Final_temp -  Initial_temp
            w=w2-w1
            k1=((w1*c1) + (w* (c2*temp)))/1000
            k2=(6.28*l*t)/100
            r=round(R2/R1,3)
            log= round((math.log10(r)),4)
            k3=2.303*log
            steam_temp= 373
            temp_1=(Final_temp +Initial_temp) / 2
            k4=temp_1 - steam_temp
            Kb=(k3/k4)
            Ka= round(k1/k2,3)
            K= round(Ka*Kb,5)
          
            print(json.dumps({"ans":[{"Microscope reading: Outer radius CR":str(OCR1)+", "+str(OCR2)+", "+str(OCR3)+", "+str(OCR4),
                                      "Inner radius CR":str(ICR1)+", "+str(ICR2)+", "+str(ICR3)+", "+str(ICR4),
                                      "Mean(R1)":str(R1),"Mean(R2)":str(R2),"The thermal condcutivity of rubber tube is determined by radial low mthod(k)=":str(K)+"w/m/k"}]}))
    

    def grating(self):
        argument = self.arg[0:]
        def TR(x,y):
            return(x+(y*lc))  
        def VA(x,y):
            return (y-x)
        def M(x,y):
            return((x+y)/4)
        def MM(x,y):
            return(-(x+y)/4)
        
        lc=float(argument[1])
        tr_al= TR(float(argument[3]),float(argument[4]))
        tr_bl= TR(float(argument[6]),float(argument[7]))
        tr_ar= TR(float(argument[13]),float(argument[14]))
        tr_br= TR(float(argument[16]),float(argument[17]))
        
        trA= VA(tr_al,tr_ar)
        trB=VA(tr_bl,tr_br)
        A= round(trA,2)
        B=round(trB,2)
        C= round((A+B)/4,2)
        N= round(((math.sin(math.radians(C)))/5893*10000)*10,3)

        Vl_a=round(TR(float(argument[23]),float(argument[24])),2)
        Bl_a=round(TR(float(argument[39]),float(argument[40])),2)
        Gl_a=round(TR(float(argument[55]),float(argument[56])),2)
        Yl_a=round(TR(float(argument[71]),float(argument[72])),2)
        Ol_a=round(TR(float(argument[87]),float(argument[88])),2)
        Rl_a=round(TR(float(argument[103]),float(argument[104])),2)

        Vl_b=round(TR(float(argument[26]),float(argument[27])),2)
        Bl_b=round(TR(float(argument[42]),float(argument[43])),2)
        Gl_b=round(TR(float(argument[58]),float(argument[59])),2)
        Yl_b=round(TR(float(argument[74]),float(argument[75])),2)  
        Ol_b=round(TR(float(argument[90]),float(argument[91])),2)    
        Rl_b=round(TR(float(argument[106]),float(argument[107])),2)

        Vr_a=round(TR(float(argument[29]),float(argument[30])),2)
        Br_a=round(TR(float(argument[45]),float(argument[46])),2) 
        Gr_a=round(TR(float(argument[61]),float(argument[62])),2) 
        Yr_a=round(TR(float(argument[77]),float(argument[78])),2)    
        Or_a=round(TR(float(argument[93]),float(argument[94])),2)
        Rr_a=round(TR(float(argument[109]),float(argument[110])),2)
        
        Vr_b=round(TR(float(argument[32]) ,float(argument[33])),2)
        Br_b=round(TR(float(argument[48]),float(argument[49])),2)
        Gr_b=round(TR(float(argument[64]),float(argument[65])),2)
        Yr_b=round(TR(float(argument[80]),float(argument[81])),2)
        Or_b=round(TR(float(argument[96]),float(argument[97])),2)
        Rr_b=round(TR(float(argument[112]),float(argument[113])),2)

        CRV_a=round(VA((Vl_a),(Vr_a)),2)
        CRB_a=round(VA((Bl_a),(Br_a)),2)
        CRG_a=round(VA((Gl_a),(Gr_a)),2)
        CRY_a=round(VA((Yl_a),(Yr_a)),2)
        CRO_a=round(VA((Ol_a),(Or_a)),2)
        CRR_a=round(VA((Rl_a),(Rr_a)),2)

        CRV_b=round(VA((Vl_b),(Vr_b)),2)
        CRB_b=round(VA((Bl_b),(Br_b)),2)
        CRG_b=round(VA((Gl_b),(Gr_b)),2)
        CRY_b=round(VA((Yl_b),(Yr_b)),2)
        CRO_b=round(VA((Ol_b),(Or_b)),2)
        CRR_b=round(VA((Rl_b),(Rr_b)),2)

        Mean1= round(M(CRV_a,CRV_b),2)
        Mean2= round(M(CRB_a,CRB_b),2)
        Mean3= round(M(CRG_a,CRG_b),2)
        Mean4= round(M(CRY_a,CRY_b),2)
        Mean5= round(M(CRO_a,CRO_b),2)
        Mean6= round(M(CRR_a,CRR_b),2)

        Violet = round((math.sin(math.radians(Mean1)))/5.908*100000,2)
        Blue = round((math.sin(math.radians(Mean2)))/5.908*100000,2)
        Green = round((math.sin(math.radians(Mean3)))/5.908*100000,2)
        Yellow = round((math.sin(math.radians(Mean4)))/5.908*100000,2)
        Orange = round((math.sin(math.radians(Mean5)))/5.908*100000,2)
        Red = round((math.sin(math.radians(Mean6)))/5.908*100000,2)

        print(json.dumps({"ans":[{"Mean":str(Mean1)+", "+str(Mean2)+", "+str(Mean3)+", "+str(Mean4)+", "+str(Mean5)+", "+str(Mean6),
                                "The wavelngth of prominent spectral lines of mercuy md spectrum are found tabulated. Violet":str(Violet)+"Å",
                                "Blue":str(Blue)+"Å"+", "+"Green : "+str(Green)+"Å"+", "+"Yellow : "+str(Yellow)+"Å"+", "+"Orange : "+str(Orange)+"Å"+", "+"Red : "+str(Red)+"Å"+", "}]}))
    
        
    def Deflection(self):
        argument = self.arg[0:]
        def Mean(a,b,c,d,e,f,g,h): 
            return((a+b+c+d+e+f+g+h)/8)
        
        thetha1=Mean(float(argument[3]),float(argument[4]),float(argument[5]),float(argument[6]),float(argument[7]),float(argument[8]),float(argument[9]),float(argument[10]))
        thetha2=Mean(float(argument[14]),float(argument[15]),float(argument[16]),float(argument[17]),float(argument[18]),float(argument[19]),float(argument[20]),float(argument[21]))
        thetha3=Mean(float(argument[25]),float(argument[26]),float(argument[27]),float(argument[28]),float(argument[29]),float(argument[30]),float(argument[31]),float(argument[32]))
        thetha4=Mean(float(argument[36]),float(argument[37]),float(argument[38]),float(argument[39]),float(argument[40]),float(argument[41]),float(argument[42]),float(argument[43]))
        thetha5=Mean(float(argument[47]),float(argument[48]),float(argument[49]),float(argument[50]),float(argument[51]),float(argument[52]),float(argument[53]),float(argument[54]))
        thetha6=Mean(float(argument[58]),float(argument[59]),float(argument[60]),float(argument[61]),float(argument[62]),float(argument[63]),float(argument[64]),float(argument[65]))
        
        tan1=round(math.tan(math.radians(thetha1)),3)
        tan2=round(math.tan(math.radians(thetha2)),3)
        tan3=round(math.tan(math.radians(thetha3)),3)
        tan4=round(math.tan(math.radians(thetha4)),3)
        tan5=round(math.tan(math.radians(thetha5)),3)
        tan6=round(math.tan(math.radians(thetha6)),3)
        
        H1=round(36.397*(1/tan1),3)
        H2=round(36.397*(1/tan2),3)
        H3=round(36.397*(1/tan3),3)
        H4=round(24.478*(1/tan4),3)
        H5=round(24.478*(1/tan5),3)
        H6=round(24.478*(1/tan6),3)
        Average= round((H1+H2+H3+H4+H5+H6)/6,3)
        H= round(((Average *4*(math.pi))/100),3)
        print(json.dumps({"ans":[{"Mean θ(degree)":str(thetha1)+", "+str(thetha2)+", "+str(thetha3)+", "+str(thetha4)+", "+str(thetha5)+", "+str(thetha6),"Mean(H)":str(Average),"The Horizontl component of earth's magnetic field(Bh)":str(H)+"x10^-5 tesla"}]}))

