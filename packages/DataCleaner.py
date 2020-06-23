from tqdm import tqdm # this module allows to display a progress bar

def cleanData(input_file: str = '.\\Data\\OMC20200621.txt',
              OptSp_output_file: str = '.\\Data\\OpticalSpaceData.txt',
              Rad_output_file: str='.\\Data\\RadarData.txt') -> None :

    ''' takes the original data file (input_file) and splits it in two different files :
        -   'OptSp_output_file' groups all optical observations from the ground
            as well as spatial observations, but does not keep the satellite position
            (2nd line of the spatial observation)
        -   'Rad_output_file' groups all radar observations, Ranging (R) and Doppler (V)
        '''
    with open(input_file, 'r') as inputFile: # read the raw data
        with open(OptSp_output_file, 'w') as OSfile: # create the output files
            with open(Rad_output_file, 'w') as Rfile:
                for line in tqdm(inputFile): # navigate through the whole file, line by line
                    if line.startswith('O') or line.startswith('S'): # first character of optical or space observation
                        OSfile.write(line) # copy the line in the new output file
                    elif line.startswith('R') or line.startswith('V'): # first character of radar observation
                        Rfile.write(line) # copy the line in the new output file

if __name__ == "__main__":
    cleanData()