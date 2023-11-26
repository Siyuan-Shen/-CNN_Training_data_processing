from GeoSpecies_pkg.Assemble_Func import Monthly_geophysicalBiases_derive_save, Monthly_geophysicalSpecies_derive_save


if __name__ == '__main__':
    Aimed_Years = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
                   2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    SPEC = ['PM25']#['DUST','SS', 'SO4', 'NH4', 'NO3', 'BC','OM']
    for species in SPEC:
        print(species)
        Monthly_geophysicalSpecies_derive_save(Aimed_Years=Aimed_Years,species=species)
        Monthly_geophysicalBiases_derive_save(species=species)