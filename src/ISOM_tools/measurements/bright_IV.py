from .parsing import get_measurement_info
import pandas as pd
import numpy as np

def bright_IV_prep(filename: str, surface: float):
    """Reads the .dat file, normalizes data and extracts KPIs out of measurement.

    Parameters
    ----------
    filename : str
    surface : float
        in cm^2

    Returns
    -------
    data_prepared: dict
        Dictionary containing measurement information and data.
    """
    data = read_IV_dat(filename)
    info = get_measurement_info(filename)
    #add surface to info dict
    info['area'] = surface
    #Now we want to at the current density in mA/cm2 as a new colum
    data["J"] = data["I"]*1000/surface #mA/cm2
    #get KPIs append KPIs to info dict
    info['J_SC'] = get_Jsc(data)
    info['V_OC']  = get_Voc(data)
    info['MPP']  = get_MPP(data)
    info['FF']  = get_FF(data)
    data_prepared = {
        'information': info,
        'data': data
    }
    return data_prepared

def read_IV_dat(filename: str):
    """Reads the IV.dat files.

    Parameters
    ----------
    filename : str

    Returns
    -------
    df : pandas.DataFrame
    """
    df = pd.read_csv(filename, sep='\t',header=2,names=["V", "I"])
    return df

def get_Jsc(data: pd.DataFrame):
    """Returns the Short-Circuit current density
      as the current density at the voltage closest to 0V.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe containing at least Voltage V and Current Density J as columns.

    Returns
    -------
    Jsc : float
        Determined short-circuit current density for given JV.
    """
    index_Jsc = (data['V']).idxmin()
    Jsc = data['J'][index_Jsc]
    return Jsc

def get_Voc(data: pd.DataFrame):
    """Returns the Voc for a given JV curve.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe containing at least Voltage V and Current Density J as columns.

    Returns
    -------
    Voc : float
        Determined Open-Circuit Voltage at J=0.
    """
    index_Voc = (data['J']-0).abs().idxmin()
    #interpolate the inverse: voltage and current to get voltage at 0
    Voc = np.interp([0],data['J'][index_Voc-1:index_Voc+2],data['V'][index_Voc-1:index_Voc+2])[0] 
    return Voc

def get_MPP(data: pd.DataFrame):
    """Caluclates the MPP for the measured JV curve.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe containing at least Voltage V and Current Density J as columns.

    Returns
    -------
    V_MPP, J_MPP : tuple
        Maximum Power Operation Point.
    """
    data['P'] = data['V']*data['J']
    print('done')
    index_Voc = (data['J']-0).abs().idxmin()
    index_MPP = data['Power'][:index_Voc].abs().idxmax() #what is the MPP position within the negative quadrant, below Voc
    V_MPP = data['V'][index_MPP]
    J_MPP = data['J'][index_MPP]
    return V_MPP, J_MPP

def get_FF(data: pd.DataFrame):
    """Calculates the FF for the measured JV curve.

    Parameters
    ----------
    data : _type_
        _description_

    Returns
    -------
    FF : float
        Determined FillFactor.
    """
    V_MPP, J_MPP = get_MPP(data)
    Jsc = get_Jsc(data)
    Voc = get_Voc(data)
    FF = (V_MPP*J_MPP)/(Voc*Jsc)
    return FF