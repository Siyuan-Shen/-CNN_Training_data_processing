from GC_input_pkg.Assemble_Func import calculate_interporlate_indices,derive_interpolated_GC_Map
import argparse




######## To change year, also change the start umber of Months
parser=argparse.ArgumentParser()
parser.add_argument('--YEAR',  nargs='+',type = str)
parser.add_argument('--MONTH',  nargs='+',type = str)
parser.add_argument('--START_NUMBER_OF_MONTHS', type = int)
parser.add_argument('--Tracer', type = str)

YEAR = parser.parse_args().YEAR
MONTH= parser.parse_args().MONTH
START_NUMBER_OF_MONTHS = parser.parse_args().START_NUMBER_OF_MONTHS
Tracer = parser.parse_args().Tracer 



if __name__ == '__main__':
    #calculate_interporlate_indices()
    derive_interpolated_GC_Map(YEAR=YEAR,MONTH=MONTH,START_NUMBER_OF_MONTHS=START_NUMBER_OF_MONTHS,Tracer=Tracer)