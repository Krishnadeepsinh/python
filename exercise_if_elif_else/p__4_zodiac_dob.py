'''
4) write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20

'''
dob_date=int(input("ENTER THE DATE OF BIRTH"))
dob_month=int(input("ENTER THE BIRTH MONTH : "))

if (dob_date>=21 and dob_month==3) or (dob_date<=19 and dob_month==4) :
    print("ARIES")

elif (dob_date>=20 and dob_month==4) or (dob_date<=20 and dob_month==5) :
    print("TAURUS")

elif (dob_date>=21 and dob_month==5) or (dob_date<=21 and dob_month==6) :
    print("GEMINI")

elif (dob_date>=22 and dob_month==6) or (dob_date<=22 and dob_month==7) :
    print("CANCER")

elif (dob_date>=23 and dob_month==7) or (dob_date<=22 and dob_month==8) :
    print("LEO")

elif (dob_date>=23 and dob_month==8) or (dob_date<=22 and dob_month==9) :
    print("VIRGO")

elif (dob_date>=23 and dob_month==9) or (dob_date<=22 and dob_month==10) :
    print("LIBRA")

elif (dob_date>=24 and dob_month==10) or (dob_date<=21 and dob_month==11) :
    print("SCORPIO")

elif (dob_date>=22 and dob_month==11) or (dob_date<=21 and dob_month==12) :
    print("SAGITTARIUS")

elif (dob_date>=22 and dob_month==12) or (dob_date<=19 and dob_month==1) :
    print("CAPRICORN")


elif (dob_date>=20 and dob_month==1) or (dob_date<=18 and dob_month==2) :
    print("AQUARIUS")


elif (dob_date>=19 and dob_month==2) or (dob_date<=20 and dob_month==3) :
    print("AQUARIUS")


else:

    print("INVAILD DOB ")
