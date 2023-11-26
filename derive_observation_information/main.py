from ObsData_pkg.Assemble_Func import Monthly_Observation_DeriveAndSave
from ObsData_pkg.visualization import plot_AllSpecies_observations_loc,plot_EachSpecies_observations_loc
from ObsData_pkg.iostream import import_biweekly_data


if __name__ == '__main__':
    Aimed_Years = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
                   2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    # Monthly_Observation_DeriveAndSave(Aimed_Years=Aimed_Years)
    SPEC = [  'SO4', 'NH4', 'NO3', 'OM', 'BC', 'DUST','SS','PM25']
    plot_AllSpecies_observations_loc(SPEC=SPEC)
    color = ['blue','orange','green','red','purple','pink','olive','cyan']
    count = 0
    for species in SPEC:

        plot_EachSpecies_observations_loc(species=species,color = color[count])
        count += 1