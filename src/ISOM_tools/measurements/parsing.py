def get_measurement_info(filename: str):
    """_summary_

    Parameters
    ----------
    file_name : str
        The filename includes certain information regarding the measurements.
        It has the structue: sampleID_pieceID_diodeID_type_T_K.dat
        example '2159_MS48_H1_AM1.5G_293K.dat'
        occasionally, another id for the specific measurement is added following the temperature

    Returns
    -------
    info_dict: dict
        The method returns a dictionary, containing the information paresd out of the filename.
    """
    info_string = filename[:-4] #cut off the .dat file extension
    print(info_string)
    info_list = info_string.split('_')
    info_dict = {
        'sampleID': info_list[0],
        'pieceID': info_list[1],
        'diodeID': info_list[2],
        'type': info_list[3],
        'T_K': int(info_list[4][:-1]),#remove K char
    }
    if len(info_list)>5:
        measurementID = info_list[5]
        info_dict['measurementID'] = measurementID

    return info_dict
