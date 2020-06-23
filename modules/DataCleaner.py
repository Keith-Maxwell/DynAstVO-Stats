from tqdm import tqdm # this module allows to display a progress bar

def cleanData(file_name: str = '.\\Data\\OMC20200621.txt',
              OSout_file_name: str = '.\\Data\\OpticalSpaceData.txt',
              Rout_file_name: str='.\\Data\\RadarData.txt') -> None :

    ''' takes the original data file (file_name) and splits it in two different files :
        -   'OSout_file_name' groups all optical observations from the ground
            as well as spatial observations, but does not keep the satellite position
            (2nd line of the spatial observation)
        -   'Rout_file_name' groups all radar observations, Ranging (R) and Doppler (V)
        '''
    with open(file_name, 'r') as inputFile: # read the raw data
        with open(OSout_file_name, 'w') as OSfile: # create the output files
            with open(Rout_file_name, 'w') as Rfile:
                for line in tqdm(inputFile): # navigate through the whole file, line by line
                    if line.startswith('O') or line.startswith('S'): # first character of optical or space observation
                        OSfile.write(line) # copy the line in the new output file
                    elif line.startswith('R') or line.startswith('V'): # first character of radar observation
                        Rfile.write(line) # copy the line in the new output file

if __name__ == "__main__":
    cleanData()