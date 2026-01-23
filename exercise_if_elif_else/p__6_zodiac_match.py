'''
6)write a program display marriage compatibility for male female using birth dates as per below link,  accept birth day and birth month from user as separate input for both male & female. decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility

https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg

'''
dob_date=int(input("ENTER THE DATE FOR MALE  : "))
dob_month=int(input("ENTER THE MONTH FOR MALE: "))

male_zodiac=" "
female_zodiac=" "
invaild_male=True
invaild_female=True

#find male zodiac




if(dob_month==1 and dob_date>31) or(dob_month==2 and dob_date>28) or (dob_month==3 and dob_date>31) or (dob_month==4 and dob_date>30) or (dob_month==5 and dob_date>31) or (dob_month==6 and dob_date>30) or (dob_month==7 and dob_date>31)or \
(dob_month==8 and dob_date>31) or (dob_month==9 and dob_date>30) or (dob_month==10 and dob_date>31) or (dob_month==11 and dob_date>30) or  (dob_month==12 and dob_date>31) :
    print("Invalid information entered")
    run=False
else:

    if (dob_date>=21 and dob_month==3) or (dob_date<=19 and dob_month==4) :
        male_zodiac="Aries"

    elif (dob_date>=20 and dob_month==4) or (dob_date<=20 and dob_month==5) :
        male_zodiac="Taurus"

    elif (dob_date>=21 and dob_month==5) or (dob_date<=21 and dob_month==6) :
        male_zodiac="Gemini"

    elif (dob_date>=22 and dob_month==6) or (dob_date<=22 and dob_month==7) :
        male_zodiac="Cancer"

    elif (dob_date>=23 and dob_month==7) or (dob_date<=22 and dob_month==8) :
        male_zodiac="Leo"

    elif (dob_date>=23 and dob_month==8) or (dob_date<=22 and dob_month==9) :
        male_zodiac="Virgo"

    elif (dob_date>=23 and dob_month==9) or (dob_date<=22 and dob_month==10) :
        male_zodiac="Libra"

    elif (dob_date>=24 and dob_month==10) or (dob_date<=21 and dob_month==11) :
        male_zodiac="Scorpio"

    elif (dob_date>=22 and dob_month==11) or (dob_date<=21 and dob_month==12) :
        male_zodiac="Sagittarius"

    elif (dob_date>=22 and dob_month==12) or (dob_date<=19 and dob_month==1) :
        male_zodiac="Capricorn"


    elif (dob_date>=20 and dob_month==1) or (dob_date<=18 and dob_month==2) :
        male_zodiac=" Aquarius"


    elif (dob_date>=19 and dob_month==2) or (dob_date<=20 and dob_month==3) :
        male_zodiac=" Pisces"


    else:
        print("INVAILD DOB ")
        invaild_male=False

###########################################################
#female zodiac

dob_date=int(input("ENTER THE DATE FOR FEMALE  : "))
dob_month=int(input("ENTER THE MONTH FOR FEMALE: "))


if(dob_month==1 and dob_date>31) or(dob_month==2 and dob_date>28) or (dob_month==3 and dob_date>31) or (dob_month==4 and dob_date>30) or (dob_month==5 and dob_date>31) or (dob_month==6 and dob_date>30) or (dob_month==7 and dob_date>31)or \
(dob_month==8 and dob_date>31) or (dob_month==9 and dob_date>30) or (dob_month==10 and dob_date>31) or (dob_month==11 and dob_date>30) or  (dob_month==12 and dob_date>31) :
    print("Invalid information entered")
    run=False
else:
    if (dob_date>=21 and dob_month==3) or (dob_date<=19 and dob_month==4) :
      female_zodiac="Aries"

    elif (dob_date>=20 and dob_month==4) or (dob_date<=20 and dob_month==5) :
      female_zodiac="Taurus"

    elif (dob_date>=21 and dob_month==5) or (dob_date<=21 and dob_month==6) :
     female_zodiac="Gemini"

    elif (dob_date>=22 and dob_month==6) or (dob_date<=22 and dob_month==7) :
      female_zodiac="Cancer"

    elif (dob_date>=23 and dob_month==7) or (dob_date<=22 and dob_month==8) :
     female_zodiac="Leo"

    elif (dob_date>=23 and dob_month==8) or (dob_date<=22 and dob_month==9) :
        female_zodiac="Virgo"

    elif (dob_date>=23 and dob_month==9) or (dob_date<=22 and dob_month==10) :
     female_zodiac="Libra"

    elif (dob_date>=24 and dob_month==10) or (dob_date<=21 and dob_month==11) :
      female_zodiac="Scorpio"

    elif (dob_date>=22 and dob_month==11) or (dob_date<=21 and dob_month==12) :
        female_zodiac="Sagittarius"

    elif (dob_date>=22 and dob_month==12) or (dob_date<=19 and dob_month==1) :
     female_zodiac="Capricorn"


    elif (dob_date>=20 and dob_month==1) or (dob_date<=18 and dob_month==2) :
        female_zodiac="Aquarius"


    elif (dob_date>=19 and dob_month==2) or (dob_date<=20 and dob_month==3) :
       female_zodiac="Pisces"


    else:
        print("INVAILD DOB ")
        invaild_female=False    

print(male_zodiac,female_zodiac)

if invaild_male==False or invaild_female==False:
    print("THE DATA INSERTED IS NOT CORRECT ")

else:
    if male_zodiac == "Aries":
        if female_zodiac in ["Taurus", "Capricorn", "Cancer", "Scorpio"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Virgo", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Leo":
        if female_zodiac in ["Virgo", "Capricorn"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Taurus", "Aquarius", "Cancer", "Scorpio", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Sagittarius":
        if female_zodiac in ["Taurus", "Virgo", "Capricorn"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Cancer", "Scorpio", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Taurus":
        if female_zodiac in ["Aries", "Sagittarius", "Gemini", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Leo", "Libra"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Virgo":
        if female_zodiac in ["Aries", "Sagittarius", "Gemini", "Libra", "Pisces"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Leo", "Aquarius"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Capricorn":
        if female_zodiac in ["Aries", "Sagittarius", "Gemini", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Leo", "Libra"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Gemini":
        if female_zodiac in ["Taurus", "Cancer", "Scorpio", "Pisces"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Sagittarius", "Virgo", "Capricorn"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Libra":
        if female_zodiac in ["Virgo", "Capricorn", "Cancer", "Scorpio"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Aries", "Taurus", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Aquarius":
        if female_zodiac in ["Taurus", "Virgo", "Capricorn", "Cancer"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Scorpio", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Cancer":
        if female_zodiac in ["Aries", "Gemini", "Libra", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Leo", "Sagittarius"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male_zodiac == "Scorpio":
        if female_zodiac in ["Gemini", "Libra", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Aries", "Leo"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")
            
    elif male_zodiac == "Pisces":
        if female_zodiac in ["Gemini", "Libra", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female_zodiac in ["Aries", "Leo", "Sagittarius", "Virgo"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")