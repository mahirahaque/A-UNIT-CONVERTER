#WE ARE MAKING A UNIT CONVERTER
history = []

#DISTANCE

def km_to_m(km):
    if km < 0: return "❎ Distance cannot be negative"
    result= km*1000
    history.append(f"{km} km = {result} m")
    return result

def m_to_km(m):
    if m < 0: return "❎ Distance cannot be negative"
    result= m*0.001
    history.append(f"{m} m = {result} km")
    return result

def km_to_miles(km):
    if km < 0: return "❎ Distance cannot be negative"
    result= km*0.621371
    history.append(f"{km} km = {result} miles")
    return result

def miles_to_km(km):
    if km < 0: return "❎ Distance cannot be negative"
    result= km*1.609344497892563
    history.append(f"{km} miles = {result} km")
    return result
#TEMPERATURE

def fahrenheit_to_celsius(cel):
    result= (cel-32)/0.5555555555555556
    history.append(f"{cel} °F = {result} °C")
    return result
    

def celsius_to_fahrenheit(cel):
    result= (cel*0.5555555555555556)+32
    history.append(f"{cel} °C = {result} °F ")
    return result

#WEIGHT

def kg_to_pounds(lbs):
    if lbs < 0: return "❎ Weight cannot be negative"
    result= lbs*2.20462
    history.append(f"{lbs} kg = {result} lbs ")
    return result

def pounds_to_kg(lbs):
    if lbs < 0: return "❎ Weight cannot be negative"
    result= lbs*0.453592
    history.append(f"{lbs} kg = {result} lbs ")
    return result

def kg_to_g(kg):
    if kg < 0: return "❎ Weight cannot be negative"
    result= kg * 1000
    history.append(f"{kg} kg = {result} g ")
    return result

def g_to_kg(g):
    if g < 0: return "❎ Weight cannot be negative"
    result= g * 0.001
    history.append(f"{g} g = {result} kg ")
    return result
#VOLUME

def l_to_gal(g):
    if g < 0: return "❎ Volume cannot be negative"
    result= g*0.264172
    history.append(f"{g} L = {result} gal ")
    return result


def cup_to_ml(cup):
    if cup < 0:
        return "❎ Volume cannot be negative"
    result= cup * 240
    history.append(f"{cup} cups = {result} mL ")
    return result

    

def ml_to_cup(ml):
    if ml < 0:
        return "❎ Volume cannot be negative"
    result= ml / 240
    history.append(f"{ml} mL = {result} cups ")
    return result

    


def gal_to_l(g):
    if g < 0: return "❎ Volume cannot be negative"
    result= g*3.7854
    history.append(f"{g} gal = {result} L ")
    return result

#TIME

def sec_to_min(s):
    if s < 0: return "❎ Time cannot be negative"
    result = s * 0.016666666666666667
    history.append(f"{s} sec = {result} min")
    return result

def min_to_sec(s):
    if s < 0: return "❎ Time cannot be negative"
    result = s * 60
    history.append(f"{s} min = {result} sec")
    return result

def hrs_to_min(h):
    if h < 0: return "❎ Time cannot be negative"
    result = h * 60
    history.append(f"{h} hrs = {result} min")
    return result

def min_to_hrs(h):
    if h < 0: return "❎ Time cannot be negative"
    result = h * 0.016666666666666667
    history.append(f"{h} min = {result} hrs")
    return result

def hrs_to_sec(h):
    if h < 0: return "❎ Time cannot be negative"
    result = h * 3600
    history.append(f"{h} hrs = {result} sec")
    return result

def sec_to_hrs(s):
    if s < 0: return "❎ Time cannot be negative"
    result = s * (1/3600)
    history.append(f"{s} sec = {result} hrs")
    return result

#PRESSURE

def pa_to_atm(pa):
    if pa < 0: return "❎ Pressure cannot be negative"
    result = pa / 101325
    history.append(f"{pa} Pa = {result} atm")
    return result

def atm_to_pa(atm):
    if atm < 0: return "❎ Pressure cannot be negative"
    result = atm * 101325
    history.append(f"{atm} atm = {result} Pa")
    return result

def pa_to_bar(pa):
    if pa < 0: return "❎ Pressure cannot be negative"
    result = pa / 100000
    history.append(f"{pa} Pa = {result} bar")
    return result




def bar_to_pa(bar):
    if bar < 0: return "❎ Pressure cannot be negative"
    result = bar * 100000
    history.append(f"{bar} bar = {result} Pa")
    return result

def mmhg_to_pa(mmhg):
    if mmhg < 0: return "❎ Pressure cannot be negative"
    result = mmhg * 133.322
    history.append(f"{mmhg} mmHg = {result} Pa")
    return result

def pa_to_mmhg(pa):
    if pa < 0: return "❎ Pressure cannot be negative"
    result = pa / 133.322
    history.append(f"{pa} Pa = {result} mmHg")
    return result

#ENERGY


def joule_to_cal(j):
    if j < 0: return "❎ Energy cannot be negative"
    result = j * 0.239006
    history.append(f"{j} J = {result} cal")
    return result

def cal_to_joule(cal):
    if cal < 0: return "❎ Energy cannot be negative"
    result = cal * 4.184
    history.append(f"{cal} cal = {result} J")
    return result

def kwh_to_joule(kwh):
    if kwh < 0: return "❎ Energy cannot be negative"
    result = kwh * 3_600_000
    history.append(f"{kwh} kWh = {result} J")
    return result

def joule_to_kwh(j):
    if j < 0: return "❎ Energy cannot be negative"
    result = j / 3_600_000
    history.append(f"{j} J = {result} kWh")
    return result

#DIGITAL STORAGE


def bit_to_byte(bit):
    if bit < 0: return "❎ Storage cannot be negative"
    result = bit / 8
    history.append(f"{bit} bits = {result} bytes")
    return result

def byte_to_bit(byte):
    if byte < 0: return "❎ Storage cannot be negative"
    result = byte * 8
    history.append(f"{byte} bytes = {result} bits")
    return result

def kb_to_mb(kb):
    if kb < 0: return "❎ Storage cannot be negative"
    result = kb / 1024
    history.append(f"{kb} KB = {result} MB")
    return result

def mb_to_kb(mb):
    if mb < 0: return "❎ Storage cannot be negative"
    result = mb * 1024
    history.append(f"{mb} MB = {result} KB")
    return result

def mb_to_gb(mb):
    if mb < 0: return "❎ Storage cannot be negative"
    result = mb / 1024
    history.append(f"{mb} MB = {result} GB")
    return result

def gb_to_mb(gb):
    if gb < 0: return "❎ Storage cannot be negative"
    result = gb * 1024
    history.append(f"{gb} GB = {result} MB")
    return result

#AREA


def m2_to_km2(m2):
    if m2 < 0: return "❎ Area cannot be negative"
    result = m2 * 0.000001
    history.append(f"{m2} m² = {result} km²")
    return result

def km2_to_m2(km2):
    if km2 < 0: return "❎ Area cannot be negative"
    result = km2 * 1_000_000
    history.append(f"{km2} km² = {result} m²")
    return result

    

def ft2_to_m2(ft2):
    if ft2 < 0: return "❎ Area cannot be negative"
    result = ft2 * 0.092903
    history.append(f"{ft2} ft² = {result} m²")
    return result

def m2_to_ft2(m2):
    if m2 < 0: return "❎ Area cannot be negative"
    result = m2 * 10.7639
    history.append(f"{m2} m² = {result} ft²")
    return result

def acre_to_m2(acres):
    if acres < 0: return "❎ Area cannot be negative"
    result = acres * 4046.86
    history.append(f"{acres} acres = {result} m²")
    return result

def m2_to_acre(m2):
    if m2 < 0: return "❎ Area cannot be negative"
    result = m2 * 0.000247105
    history.append(f"{m2} m² = {result} acres")
    return result


#TEMPERATURE

def celsius_to_kelvin(c):
    result=  c + 273.15
    history.append(f"{c} °C = {result} K")
    return result

def kelvin_to_celsius(k):
    if k < 0: return "❎ Kelvin cannot be negative"
    result= k - 273.15
    history.append(f"{k} K = {result} °C ")
    return result
#VOLUME

def litre_to_ml(l):
    if l < 0: return "❎ Volume cannot be negative"
    result= l * 1000
    history.append(f"{l} L = {result} mL")
    return result
    

def ml_to_litre(ml):
    if ml < 0: return "❎ Volume cannot be negative"
    result= ml / 1000
    history.append(f"{ml} mL = {result} L")
    return result
#LENGTH

def ft_to_m(ft):
    if ft < 0:
        return "❎ Distance cannot be negative"
    result= ft * 0.3048
    history.append(f"{ft} ft = {result} m")
    return result

def m_to_ft(m):
    if m < 0:
        return "❎ Distance cannot be negative"
    result= m / 0.3048
    history.append(f"{m} m = {result} ft")
    return result


def inch_to_cm(inch):
    if inch < 0:
        return "❎ Distance cannot be negative"
    result= inch * 2.54
    history.append(f"{inch} inches = {result} cm")
    return result

def cm_to_inch(cm):
    if cm < 0:
        return "❎ Distance cannot be negative"
    result= cm / 2.54
    history.append(f"{cm} cm = {result} inches")
    return result

#SPEED

def kmh_to_ms(kmh):
    if kmh < 0: return "❎ Speed cannot be negative"
    result= kmh / 3.6
    history.append(f"{kmh} km/h = {result} m/s")
    return result


def ms_to_kmh(ms):
    if ms < 0: return "❎ Speed cannot be negative"
    result= ms * 3.6
    history.append(f"{ms} m/s = {result} km/h")
    return result

def mph_to_kmh(mph):
    if mph < 0: return "❎ Speed cannot be negative"
    result= mph * 1.60934
    history.append(f"{mph} mph = {result} kmh")
    return result

def kmh_to_mph(kmh):
    if kmh < 0: return "❎ Speed cannot be negative"
    result= kmh / 1.60934
    history.append(f"{kmh} kmh = {result} mph")
    return result



print("☆"*72)
print(" 🎀 Welcome to the Ultimate Unit Converter Program 🎀 ")
print("☆"*72)


while True:
    print("\n🦋 MENU 🦋")
    print("1. Length / Distance")
    print("2. Weight / Mass")
    print("3. Temperature")
    print("4. Time")
    print("5. Speed")
    print("6. Volume / Capacity")
    print("7. Area")
    print("8. Pressure")
    print("9. Energy / Work")
    print("10. Digital Storage")
    print("11. Show conversion history")
    print("12. Show previous conversion")
    print("13. Quit")

    try:
        category = int(input("☆ Enter your category choice: "))
    except ValueError:
        print("❎ Please enter a valid number.")
        continue

    if category < 1 or category > 13:
        print("❎ Invalid input! Please choose a number from the menu.")
        continue
    if category == 13:
        print("🙏 Thank you for using the Ultimate Unit Converter 🙏")
        break
    if category == 11:
        if not history:
            print("No Conversions yet")
        else:
            print("History of Unit Conversions")
            for h in history:
                print("▪", h)
        continue        
    if category == 12:
        if not history:
            print("No conversions yet")
        else:
            print("previous conversion: ", history[-1])
        continue    
        

    
    try:
        value = float(input("🔢 Enter the value you want to convert: "))
    except ValueError:
        print("❎ Please enter a valid number.")
        continue

    if category == 1:  # Length / Distance
        print("1. km → m\n2. m → km\n3. km → miles\n4. miles → km\n5. ft → m\n6. m → ft\n7. inch → cm\n8. cm → inch")
        choice = input("Enter your conversion choice: ")
        
        if choice == "1":
            print(f"{value} km = {km_to_m(value)} m")
        elif choice == "2":
            print(f"{value} m = {m_to_km(value)} km")
        elif choice == "3":
            print(f"{value} km = {km_to_miles(value)} miles")
        elif choice == "4":
            print(f"{value} miles = {miles_to_km(value)} km")
        elif choice == "5":
            print(f"{value} ft = {ft_to_m(value)} m")  
        elif choice == "6":
            print(f"{value} m = {m_to_ft(value)} ft")  
        elif choice == "7":
            print(f"{value} in = {inch_to_cm(value)} cm")  
        elif choice == "8":
            print(f"{value} cm = {cm_to_inch(value)} in")  
        else:
            print("❎ Invalid choice.")

    elif category == 2:  # Weight / Mass
        print("1. kg → g\n2. g → kg\n3. kg → lbs\n4. lbs → kg")
        
        
        choice = int(input("Enter your conversion choice: "))
        
            
        if choice==1:
                print(f"{value} kg = {kg_to_g(value)} g")
        elif choice==2:
                print(f"{value} g = {g_to_kg(value)} kg")
        elif choice==3:
                print(f"{value} kg = {kg_to_pounds(value)} lbs")
        elif choice==4:
                print(f"{value} lbs = {pounds_to_kg(value)} kg")
        else:
                print(" ❎ Invalid choice")
        
            
        

    elif category == 3:  # Temperature
        print("1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius\n3. Celsius → Kelvin\n4. Kelvin → Celsius")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            print(f"{value} ℃ = {celsius_to_fahrenheit(value)} ℉ ")
        elif choice==2:
            print(f"{value} ℉ = {fahrenheit_to_celsius(value)} ℃ ")
        elif choice==3:
            print(f"{value} ℃ = {celsius_to_kelvin(value)} K")
        elif choice==4:
            print(f"{value} K = {kelvin_to_celsius(value)} ℃ ")
        else:
            print(" ❎ Invalid choice")
        

    elif category == 4:  # Time
        print("1. Hours → Minutes\n2. Minutes → Hours\n3. Seconds → Minutes\n4. Hours → Seconds\n5. Minutes → Seconds\n6. Seconds → Hours")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            if value==1:
                print(" 1 hr = 60 mins")
            else:
                print(f"{value} hrs = {hrs_to_min(value)} mins")
        elif choice==2:
            if value==1:
                print(" 1 min = 0.0167 hr")
            else:
                print(f"{value} mins = {min_to_hrs(value)} hrs")
        elif choice==3:
            print(f"{value} sec = {sec_to_min(value)} min")
        elif choice==4:
                        print(f"{value} hrs = {hrs_to_sec(value)} sec")
        elif choice==5:
                        print(f"{value} min = {min_to_sec(value)} sec")
        elif choice==6:
                        print(f"{value} sec = {sec_to_hrs(value)} hrs")
        else:
            print(" ❎ Invalid choice")



    elif category == 5:  # Speed
        print("1. km/h → m/s\n2. m/s → km/h\n3. mph → km/h\n4. km/h → mph")
        choice = int(input("Enter your conversion choice: "))
        if choice == 1:
                       print(f"✅ {value} km/h = {kmh_to_ms(value)} m/s ✅")
        elif choice == 2:
                       print(f"✅ {value} m/s = {ms_to_kmh(value)} km/h ✅")
        elif choice == 3:
                       print(f"✅ {value} mph = {mph_to_kmh(value)} km/h ✅")
        elif choice == 4:
                       print(f"✅ {value} km/h = {kmh_to_mph(value)} mph ✅")
        else:
                        print("❎ Invalid choice.")
        

    elif category == 6:  # Volume / Capacity
        print("1. Liter → mL\n2. mL → Liter\n3. Gallon → Liter\n4. Liter → Gallon\n5. Cup → mL\n6. mL → Cup")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            print(f"✅ {value} L = {litre_to_ml(value)} mL ✅")
        elif choice==2:
            print(f"✅ {value} mL = {ml_to_litre(value)} L ✅")
        elif choice==3:
            print(f"✅ {value} gal = {gal_to_l(value)} L ✅")
        elif choice==4:
            print(f"✅ {value} L = {l_to_gal(value)} gal ✅")
        elif choice==5:
            print(f"✅ {value} cup = {cup_to_ml(value)} mL ✅")
        elif choice==6:
            print(f"✅ {value} mL = {ml_to_cup(value)} cup ✅")
        else:
            print("❎ Invalid choice.")

    elif category == 7:  # Area
        print("1. m² → km²\n2. km² → m²\n3. ft² → m²\n4. m² → ft²\n5. Acre → m²\n6. m² → Acre")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            print(f"✅ {value} m² = {m2_to_km2(value)} km² ✅")
        elif choice==2:
            print(f"✅ {value} km² = {km2_to_m2(value)} m² ✅")
        elif choice==3:
            print(f"✅ {value} ft² = {ft2_to_m2(value)} m² ✅")
        elif choice==4:
            print(f"✅ {value} m² = {m2_to_ft2(value)} ft² ✅")
        elif choice==5:
            print(f"✅ {value} acre = {acre_to_m2(value)} m² ✅")
        elif choice==6:
            print(f"✅ {value} m² = {m2_to_acre(value)} acre ✅")
        else:
            print("❎ Invalid choice.")

    elif category == 8:  # Pressure
        print("1. Pa → atm\n2. atm → Pa\n3. Pa → bar\n4. bar → Pa\n5. mmHg → Pa\n6. Pa → mmHg")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            print(f"✅ {value} Pa = {pa_to_atm(value)} atm ✅")
        elif choice==2:
            print(f"✅ {value} atm = {atm_to_pa(value)} Pa ✅")
        elif choice==3:
            print(f"✅ {value} Pa = {pa_to_bar(value)} bar ✅")
        elif choice==4:
            print(f"✅ {value} bar = {bar_to_pa(value)} Pa ✅")
        elif choice==5:
            print(f"✅ {value} mmHg = {mmhg_to_pa(value)} Pa ✅")
        elif choice==6:
            print(f"✅ {value} Pa = {pa_to_mmhg(value)} mmHg ✅")
        else:
            print("❎ Invalid choice.")
            
            

    elif category == 9:  # Energy / Work
        print("1. Joule → Calorie\n2. Calorie → Joule\n3. kWh → Joule\n4. Joule → kWh")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            print(f"✅ {value} J = {joule_to_cal(value)} cal ✅")
        elif choice==2:
            print(f"✅ {value} cal = {cal_to_joule(value)} J ✅")
        elif choice==3:
            print(f"✅ {value} kWh = {kwh_to_joule(value)} J ✅")
        elif choice==4:
            print(f"✅ {value} J = {joule_to_kwh(value)} kWh ✅")
        else:
            print("❎ Invalid choice.")
            

    elif category == 10:  # Digital Storage
        print("1. Bit → Byte\n2. Byte → Bit\n3. KB → MB\n4. MB → KB\n5. MB → GB\n6. GB → MB")
        choice = int(input("Enter your conversion choice: "))
        if choice==1:
            print(f"✅ {value} bits = {bit_to_byte(value)} byte ✅")
        elif choice==2:
            print(f"✅ {value} byte = {byte_to_bit(value)} bits ✅")
        elif choice==3:
            print(f"✅ {value} KB = {kb_to_mb(value)} MB ✅")
        elif choice==4:
            print(f"✅ {value} MB = {mb_to_kb(value)} KB ✅")
        elif choice==5:
            print(f"✅ {value} MB = {mb_to_gb(value)} GB ✅")
        elif choice==6:
            print(f"✅ {value} GB = {gb_to_mb(value)} MB ✅")
        else:
            print("❎ Invalid choice.")
            

            

    else:
        print("❎ Invalid input!")

            
        
        
