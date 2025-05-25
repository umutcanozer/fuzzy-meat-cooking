import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

meat_type = ctrl.Antecedent(np.linspace(0, 2, 100), 'meat_type')
cooking_method = ctrl.Antecedent(np.linspace(0, 2, 100), 'cooking_method')
cooking_pref = ctrl.Antecedent(np.linspace(0, 2, 100), 'cooking_pref')
fat_level = ctrl.Antecedent(np.linspace(0, 2, 100), 'fat_level')
thickness = ctrl.Antecedent(np.arange(1, 6.1, 0.1), 'thickness')

time = ctrl.Consequent(np.arange(5, 31, 1), 'time')
temp = ctrl.Consequent(np.arange(120, 251, 1), 'temp')

meat_type['dana']  = fuzz.trimf(meat_type.universe, [0.0, 0.0, 0.4])
meat_type['kuzu']  = fuzz.trimf(meat_type.universe, [0.6, 1.0, 1.4])
meat_type['tavuk'] = fuzz.trimf(meat_type.universe, [1.6, 2.0, 2.0])

cooking_method['izgara']  = fuzz.trimf(cooking_method.universe, [0.0, 0.0, 0.4])
cooking_method['tavada']  = fuzz.trimf(cooking_method.universe, [0.6, 1.0, 1.4])
cooking_method['firinda'] = fuzz.trimf(cooking_method.universe, [1.6, 2.0, 2.0])

cooking_pref['az']   = fuzz.trimf(cooking_pref.universe, [0.0, 0.0, 0.4])
cooking_pref['orta'] = fuzz.trimf(cooking_pref.universe, [0.6, 1.0, 1.4])
cooking_pref['cok']  = fuzz.trimf(cooking_pref.universe, [1.6, 2.0, 2.0])

fat_level['yagsiz'] = fuzz.trimf(fat_level.universe, [0.0, 0.0, 0.4])
fat_level['orta']   = fuzz.trimf(fat_level.universe, [0.6, 1.0, 1.4])
fat_level['yagli']  = fuzz.trimf(fat_level.universe, [1.6, 2.0, 2.0])

thickness['ince'] = fuzz.trimf(thickness.universe, [1, 1, 2.0])
thickness['orta'] = fuzz.trimf(thickness.universe, [2, 3.5, 5])
thickness['kalin'] = fuzz.trimf(thickness.universe, [5, 6, 6])

time['kisa'] = fuzz.trimf(time.universe, [5, 5, 12])
time['orta'] = fuzz.trimf(time.universe, [10, 17.5, 25])
time['uzun'] = fuzz.trimf(time.universe, [22, 30, 30])

temp['dusuk'] = fuzz.trimf(temp.universe, [120, 120, 160])
temp['orta'] = fuzz.trimf(temp.universe, [150, 180, 210])
temp['yuksek'] = fuzz.trimf(temp.universe, [200, 250, 250])

rules = [
    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & cooking_pref['az']   & fat_level['yagsiz'] & thickness['ince'],  (time['kisa'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & cooking_pref['az']   & fat_level['orta']   & thickness['orta'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['kalin'], (time['orta'], temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['orta']   & thickness['ince'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['ince'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['orta']   & thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['az']   & fat_level['yagsiz'] & thickness['ince'],  (time['kisa'],  temp['yuksek'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['orta'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['orta'] & fat_level['orta']   & thickness['kalin'], (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['kalin'], (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['az']   & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['orta']   & thickness['orta'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['yagsiz'] & thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['az']   & fat_level['yagsiz'] & thickness['ince'],  (time['kisa'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['orta']   & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['yagli']  & thickness['orta'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['az']   & fat_level['yagsiz'] & thickness['orta'],  (time['kisa'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['orta'] & fat_level['orta']   & thickness['kalin'], (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['cok']  & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['yuksek'])),

    ctrl.Rule(meat_type['kuzu'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['yagli']  & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['orta']   & thickness['kalin'], (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['orta']   & thickness['ince'],  (time['uzun'],  temp['yuksek'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['yagsiz'] & thickness['orta'],  (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['tavuk'] & cooking_method['tavada']  & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['tavada']  & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['kalin'], (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['tavada']  & cooking_pref['cok']  & fat_level['orta']   & thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['orta']   & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(thickness['ince'], (time['kisa'],  temp['orta'])),
    ctrl.Rule(thickness['orta'], (time['orta'],  temp['orta'])),
    ctrl.Rule(thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(fat_level['yagsiz'] & cooking_method['izgara'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(fat_level['orta']   & cooking_method['izgara'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(fat_level['yagli']  & cooking_method['izgara'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(fat_level['yagsiz'] & cooking_method['firinda'], (time['uzun'],  temp['orta'])),
    ctrl.Rule(fat_level['yagli']  & cooking_method['tavada'],  (time['orta'],  temp['orta'])),

    ctrl.Rule(meat_type['dana'] & cooking_method['izgara'] & fat_level['yagli'] & thickness['kalin'], (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada'] & fat_level['orta'] & thickness['ince'], (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & fat_level['yagsiz'] & thickness['orta'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['az']   & fat_level['orta']   & thickness['kalin'], (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['az']   & fat_level['yagli']  & thickness['ince'],  (time['kisa'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['orta'] & fat_level['yagli']  & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['tavada'] & cooking_pref['cok']  & fat_level['orta']   & thickness['ince'],  (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['az']   & fat_level['orta']   & thickness['ince'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['az']   & fat_level['yagli']  & thickness['orta'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['yagli']  & thickness['ince'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['dana'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['orta']   & thickness['kalin'], (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['az']   & fat_level['orta']   & thickness['kalin'], (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['orta']   & thickness['ince'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['yagsiz'] & thickness['kalin'], (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['az']   & fat_level['yagli']  & thickness['ince'],  (time['kisa'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['az']   & fat_level['orta']   & thickness['ince'],  (time['kisa'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['orta'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['tavada']  & cooking_pref['cok']  & fat_level['orta']   & thickness['orta'],  (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['kuzu'] & cooking_method['firinda'] & cooking_pref['az']   & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['firinda'] & cooking_pref['az']   & fat_level['yagli']  & thickness['kalin'], (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['kalin'], (time['uzun'],  temp['yuksek'])),
    ctrl.Rule(meat_type['kuzu'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['ince'],  (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['orta']   & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['orta'] & fat_level['yagli']  & thickness['ince'],  (time['orta'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['orta'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['izgara'] & cooking_pref['cok']  & fat_level['yagsiz'] & thickness['ince'],  (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(meat_type['tavuk'] & cooking_method['tavada']  & cooking_pref['cok']  & fat_level['yagsiz'] & thickness['ince'],  (time['uzun'],  temp['yuksek'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['tavada']  & cooking_pref['cok']  & fat_level['orta']   & thickness['ince'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['tavada']  & cooking_pref['cok']  & fat_level['yagli']  & thickness['kalin'], (time['uzun'],  temp['orta'])),

    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['yagsiz'] & thickness['ince'],  (time['orta'],  temp['yuksek'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & cooking_pref['orta'] & fat_level['orta']   & thickness['orta'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['orta']   & thickness['ince'],  (time['uzun'],  temp['orta'])),
    ctrl.Rule(meat_type['tavuk'] & cooking_method['firinda'] & cooking_pref['cok']  & fat_level['yagli']  & thickness['ince'],  (time['uzun'],  temp['yuksek'])),

    ctrl.Rule(cooking_pref['az']   & cooking_method['izgara'], (time['kisa'],  temp['orta'])),
    ctrl.Rule(cooking_pref['orta'] & cooking_method['izgara'], (time['orta'],  temp['orta'])),
    ctrl.Rule(cooking_pref['cok']  & cooking_method['izgara'], (time['uzun'],  temp['orta'])),
    ctrl.Rule(cooking_pref['cok']  & cooking_method['tavada'], (time['uzun'],  temp['orta'])),

    ctrl.Rule(fat_level['yagli'] & thickness['ince'] & cooking_method['tavada'], (time['kisa'],  temp['orta'])),
    ctrl.Rule(fat_level['yagsiz'] & thickness['kalin'] & cooking_method['firinda'], (time['uzun'],  temp['yuksek'])),
]

cooking_ctrl = ctrl.ControlSystem(rules)

def predict_cooking(meat_type, cooking_method, cooking_pref, fat_level, thickness):
    cooking_sim = ctrl.ControlSystemSimulation(cooking_ctrl)
    cooking_sim.input['meat_type'] = meat_type
    cooking_sim.input['cooking_method'] = cooking_method
    cooking_sim.input['cooking_pref'] = cooking_pref
    cooking_sim.input['fat_level'] = fat_level
    cooking_sim.input['thickness'] = thickness

    try:
        cooking_sim.compute()
        return cooking_sim.output['time'], cooking_sim.output['temp']
    except KeyError:
        return None, None



__all__ = [
    "predict_cooking",
    "meat_type",
    "cooking_method",
    "cooking_pref",
    "fat_level",
    "thickness",
    "time",
    "temp"
]