from dataclasses import dataclass
from pyjoycon import JoyCon, get_R_id, get_L_id
## requirements joycon-python hidapi pyglm

@dataclass
class JoyConPairStatus():
    y: bool
    x: bool
    b: bool
    a: bool
    r_sr: bool
    r_sl: bool
    r: bool
    zr: bool

    down: bool
    up: bool
    right: bool
    left: bool
    l_sr: bool
    l_sl: bool
    l: bool
    zl: bool

    minus: bool
    plus: bool
    r_stick: bool
    l_stick: bool
    home: bool
    capture: bool
    l_charging_grip: bool
    r_charging_grip: bool

    l_is_charging: bool
    l_battery_level: int
    r_is_charging: bool
    r_battery_level: int

    l_joystick_x: int
    l_joystick_y: int
    r_joystick_x: int
    r_joystick_y: int

    l_accel_x: int
    l_accel_y: int
    l_accel_z: int
    l_gyro_x: int
    l_gyro_y: int
    l_gyro_z: int

    r_accel_x: int
    r_accel_y: int
    r_accel_z: int
    r_gyro_x: int
    r_gyro_y: int
    r_gyro_z: int
       
    
    
class JoyConPair():
    def __init__(self,r_id=None,l_id=None,include_joysticks_in_buttons=False) -> None:
        self.include_joysticks_in_buttons = include_joysticks_in_buttons
        self.R_ID = get_R_id() if r_id is None else r_id
        self.L_ID = get_L_id() if l_id is None else l_id
        self.R = JoyCon(*self.R_ID)
        self.L = JoyCon(*self.L_ID)
        self.prev_raw_btns = self.raw_btns()
    def raw(self) -> list: return [self.L.get_status(),self.R.get_status()]
    def raw_btns(self) -> list: return filter(None, [self.L.get_status()["buttons"],self.L.get_status()["analog-sticks"] if self.include_joysticks_in_buttons else None,self.R.get_status()["buttons"],self.L.get_status()["analog-sticks"] if self.include_joysticks_in_buttons else None])
    def is_btns_new(self) -> bool:
        if self.prev_raw_btns == self.raw_btns():
            return False
        else:
            self.prev_raw_btns = self.raw_btns()
            return True
    def get(self) -> JoyConPairStatus:
        l,r = self.raw()
        return JoyConPairStatus(
            y= r["buttons"]["right"]["y"],
            x= r["buttons"]["right"]["x"],
            b= r["buttons"]["right"]["b"],
            a= r["buttons"]["right"]["a"],
            r_sr= r["buttons"]["right"]["sr"],
            r_sl= r["buttons"]["right"]["sl"],
            r= r["buttons"]["right"]["r"],
            zr= r["buttons"]["right"]["zr"],

            down= l["buttons"]["left"]["down"],
            up= l["buttons"]["left"]["up"],
            right= l["buttons"]["left"]["right"],
            left= l["buttons"]["left"]["left"],
            l_sr= l["buttons"]["left"]["sr"],
            l_sl= l["buttons"]["left"]["sl"],
            l= l["buttons"]["left"]["l"],
            zl= l["buttons"]["left"]["zl"],

            minus= l["buttons"]["shared"]["minus"],
            plus= r["buttons"]["shared"]["plus"],
            r_stick= r["buttons"]["shared"]["r_stick"],
            l_stick= l["buttons"]["shared"]["l_stick"],
            home= r["buttons"]["shared"]["home"],
            capture= l["buttons"]["shared"]["capture"],

            l_charging_grip= l["buttons"]["shared"]["charging-grip"],
            r_charging_grip= r["buttons"]["shared"]["charging-grip"],
            l_is_charging= l["battery"]["charging"],
            l_battery_level= l["battery"]["level"],
            r_is_charging= r["battery"]["charging"],
            r_battery_level= r["battery"]["level"],

            l_joystick_x= l["analog-sticks"]["left"]["horizontal"],
            l_joystick_y= l["analog-sticks"]["left"]["vertical"],
            r_joystick_x= r["analog-sticks"]["right"]["horizontal"],
            r_joystick_y= r["analog-sticks"]["right"]["vertical"],

            l_accel_x= l["accel"]["x"],
            l_accel_y= l["accel"]["y"],
            l_accel_z= l["accel"]["z"],
            l_gyro_x= l["gyro"]["x"],
            l_gyro_y= l["gyro"]["y"],
            l_gyro_z= l["gyro"]["z"],

            r_accel_x= r["accel"]["x"],
            r_accel_y= r["accel"]["y"],
            r_accel_z= r["accel"]["z"],
            r_gyro_x= r["gyro"]["x"],
            r_gyro_y= r["gyro"]["y"],
            r_gyro_z= r["gyro"]["z"],
        )

        