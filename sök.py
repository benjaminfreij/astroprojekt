from ast import While
from click import progressbar
import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
from math import isclose 
import warnings
warnings.filterwarnings('ignore') #fick ett irriterande irrelevant varningsmeddelande konstant vid varje körning av programmet
from alive_progress import alive_bar
import time
from time import sleep
from progress.spinner import MoonSpinner
import tqdm


while True:
    #öppnar txt fil med allla KIC ids
    with open('kepler.txt') as f:
            first_line2= f.readline()
    print(first_line2)
    #söker efter all data med KIC id:et från txt filen
    search_result2 = lk.search_lightcurve(first_line2, author="Kepler")
    print(search_result2)
#om searchresulten ger för låg totalt dataset breakar loopen och id:et tas bort
    if len(search_result2) < 5:
        with open("kepler.txt", "r+") as f:
                    y = f.readlines()
                    f.seek(0)
                    for i in y:
                        if i != first_line2:
                            f.write(i)
                    f.truncate();
        print("otillräcklig data")
        break
 
    
    #laddar ner all data, samt sätter ihop det.
    lc2 = search_result2.download_all().stitch()


    
    #omvandlar datan till ett lådagram
    pg2 = lc2.to_periodogram(normalization='psd',minimum_frequency=1500,maximum_frequency=2700)
  
   
    #plottar 
    ax2 = pg2.plot();

    #plattar ihop plotten för enklare uthämtning av information
    snr2 = pg2.flatten()
    ax2 = snr2.plot();

    #omvandlar snr plot till ett seismology objekt
    seismology = snr2.to_seismology()

    #estimerar max hastighet
    seismology.estimate_numax()
    seismology.numax.value

    #dubbelkollar 
    seismology.diagnose_numax();

    #samma sak men med hastigheten
    try:
        seismology.estimate_deltanu()
    except ValueError: #Value errors kan uppstå när en nerladdad array egentligen är tom på nödvändig information, om det händer breakar loopen
        break

    seismology.diagnose_deltanu();

    #estimerat massa,radie, och tyngdacceleration. 
    seismology.estimate_mass()
    seismology.estimate_radius()
    seismology.estimate_logg()

    #öppnar output.txt och lägger till KIC id samt alla uträknade seismology värden. 
    with open("output.txt", "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            file_object.write(first_line2)
    with open("output.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0 :
                    file_object.write("")
                file_object.write(str(seismology))  
                file_object.write("\n")
    
    break

while True: 
    
    #öppnar första linjen av txt filen med id:n
    with open('kepler.txt') as f:
        first_line= f.readline()

    #söker efter efter önskad stjärna, samt laddar ner.
    search_result = lk.search_lightcurve(first_line, mission="Kepler", cadence='long')
    lc_collection = search_result.download_all()
    

    #fixar instrumentella störningar, samt designar storlek för plot. 
    lc = lc_collection.stitch().flatten(window_length = 901).remove_outliers()
    
    #hela denna delen gör ett låddiagram för att analysera spikar i datan. 

    #sätter en array för perioden av dessa spikar. Här är den satt till 1-20 dagar för att kunna hitta de mindre planeterna. 
    period = np.linspace(1,20,10000)
    bls = lc.to_periodogram(method = 'bls', period = period, frequency_factor=500);
    bls.plot();
    #när man har plottat detta kommer man se flera olika spikar, men man vill endast ha de som är kraftfullast.
    #därför tar man då endast värden vid max kraft. 
    pla_x_period = bls.period_at_max_power
    pla_x_t0 = bls.transit_time_at_max_power
    pla_x_dur = bls.duration_at_max_power

    planet_b_mask = bls.get_transit_mask(period=pla_x_period,
                                        transit_time=pla_x_t0,
                                        duration=pla_x_dur)
    masked_lc = lc[~planet_b_mask]
    ax = masked_lc.scatter();
    lc[planet_b_mask].scatter(ax=ax, c='r', label='Masked');

    plt.savefig(f"newdir/astrobild{16}")

    planet_b_model = bls.get_transit_model(period=pla_x_period,
                                        transit_time=pla_x_t0,
                                        duration=pla_x_dur)
    #gör ett scatter plot, de med alla de svarta prickarna. 
    ax = lc.fold(pla_x_period, pla_x_t0).scatter()
    planet_b_model.fold(pla_x_period, pla_x_t0).plot(ax=ax, c='r', lw=2)
    ax.set_xlim(-5, 5);
    
  
    



    #planet 2 sökning, ändrade parametrar
    period = np.linspace(1, 300, 10000)
    bls = masked_lc.to_periodogram('bls', period=period, frequency_factor=500)
    bls.plot();

    pla_y_period = bls.period_at_max_power
    pla_y_t0 = bls.transit_time_at_max_power
    pla_y_dur = bls.duration_at_max_power
    print(pla_x_period)
    print(pla_y_period)

    #omvandlar periodtiderna till float, så jag kan jämföra dem med isclose.
    planetx = float(str(pla_x_period)[:-2])
    planety = float(str(pla_y_period)[:-2])



    #jämför de 2 olika periodvärdena för att se om de är lika och är samma planet. 
    if isclose(planetx, planety, abs_tol=1):
        with open("output.txt", "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0 :
                    file_object.write("\n")
                file_object.write(first_line)
        with open("output.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("")
                    file_object.write(str(pla_x_period))  
                    file_object.write("\n")
        with open("kepler.txt", "r+") as t:
                k = t.readlines()
                t.seek(0)
                for i in k:
                    if i != first_line:
                        t.write(i)
                t.truncate();
    else:
        #borde göra denna delen till en funktion men den lägger till vars ett id om det är 2 planeter annars läggs bara en till. 
        if pla_y_period or pla_x_period > 0:
            if pla_x_period > 0:
                with open("output.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("\n")
                    file_object.write(first_line)

                with open("output.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("")
                    file_object.write(str(pla_x_period))  
                    file_object.write("\n")

            if pla_y_period > 0:
                with open("output.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("\n")
                    file_object.write(first_line)

                with open("output.txt", "a+") as file_object:
                    file_object.seek(0)
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("")
                    file_object.write(str(pla_y_period))  
                    file_object.write("\n")
                with open("kepler.txt", "r+") as f: #tar bort id:et
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != first_line:
                            f.write(i)
                    f.truncate();
    break
                    





