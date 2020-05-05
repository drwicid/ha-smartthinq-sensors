import enum

from .device import STATE_OPTIONITEM_NONE, STATE_OPTIONITEM_OFF


# DishWasher State
class STATE_DISHWASHER(enum.Enum):
    POWER_OFF = STATE_OPTIONITEM_NONE
    COMPLETE = "Completed"
    ERROR = "Error"
    INITIAL = "Select Course"
    PAUSE = "Paused"
    RUNNING = "Washing"


# DishWasher Process
class STATE_DISHWASHER_PROCESS(enum.Enum):
    OFF = STATE_OPTIONITEM_NONE
    CANCEL = "Cancelled"
    COMPLETE = "Completed"
    DRYING = "Drying"
    NIGHTDRY = "Night Dry"
    RESERVE = "Reserve"
    RINSING = "Rising"
    RUNNING = "Running"


# DishWasher Load
class STATE_DISHWASHER_HALFLOAD(enum.Enum):
    OFF = STATE_OPTIONITEM_OFF
    LOWER = "Half load lower"
    UPPER = "Half load upper"


# DishWasher Error
class STATE_DISHWASHER_ERROR(enum.Enum):
    OFF = STATE_OPTIONITEM_NONE
    NO_ERROR = "Normal"
    ERROR_AE = "AE - Contact Service Center"
    ERROR_BE = "BE - Contact Service Center"
    ERROR_FE = "FE - Contact Service Center"
    ERROR_HE = "HE - Contact Service Center"
    ERROR_IE = "No water - Please make sure the water has enough pressure to reach the washer."
    ERROR_LE = "LE - Contact Service Center"
    ERROR_NE = "NE - Contact Service Center"
    ERROR_OE = "Drain error - Please make sure the pipe is not clogged/frozen"
    ERROR_TE = "tE - Contact Service Center"


"""------------------for DishWasher"""
DISHWASHERSTATES = {
    "-": STATE_DISHWASHER.POWER_OFF,
    "ERROR": STATE_DISHWASHER.ERROR,
    "@DW_STATE_POWER_OFF_W": STATE_DISHWASHER.POWER_OFF,
    "@DW_STATE_INITIAL_W": STATE_DISHWASHER.INITIAL,
    "@DW_STATE_RUNNING_W": STATE_DISHWASHER.RUNNING,
    "@DW_STATE_PAUSE_W": STATE_DISHWASHER.PAUSE,
    "@DW_STATE_COMPLETE_W": STATE_DISHWASHER.COMPLETE,
}

DISHWASHERPROCESS = {
    "-": STATE_DISHWASHER_PROCESS.OFF,
    "@DW_STATE_INITIAL_W": STATE_DISHWASHER_PROCESS.OFF,
    "@DW_STATE_RESERVE_W": STATE_DISHWASHER_PROCESS.RESERVE,
    "@DW_STATE_RUNNING_W": STATE_DISHWASHER_PROCESS.RUNNING,
    "@DW_STATE_RINSING_W": STATE_DISHWASHER_PROCESS.RINSING,
    "@DW_STATE_DRYING_W": STATE_DISHWASHER_PROCESS.DRYING,
    "@DW_STATE_COMPLETE_W": STATE_DISHWASHER_PROCESS.COMPLETE,
    "@DW_STATE_NIGHTDRY_W": STATE_DISHWASHER_PROCESS.NIGHTDRY,
    "@DW_STATE_CANCEL_W": STATE_DISHWASHER_PROCESS.CANCEL,
}

DISHWASHERHALFLOAD = {
    "@CP_OFF_EN_W": STATE_DISHWASHER_HALFLOAD.OFF,
    "@DW_OPTION_HALF_LOAD_LOWER_W": STATE_DISHWASHER_HALFLOAD.LOWER,
    "@DW_OPTION_HALF_LOAD_UPPER_W": STATE_DISHWASHER_HALFLOAD.UPPER,
}

DISHWASHERERRORS = {
    "No Error": STATE_DISHWASHER_ERROR.NO_ERROR,
    "@DW_ERROR_HE_LABEL": STATE_DISHWASHER_ERROR.ERROR_HE,
    "@DW_ERROR_IE_LABEL": STATE_DISHWASHER_ERROR.ERROR_IE,
    "@DW_ERROR_OE_LABEL": STATE_DISHWASHER_ERROR.ERROR_OE,
    "@DW_ERROR_FE_LABEL": STATE_DISHWASHER_ERROR.ERROR_FE,
    "@DW_ERROR_TE_LABEL": STATE_DISHWASHER_ERROR.ERROR_TE,
    "@DW_ERROR_AE_LABEL": STATE_DISHWASHER_ERROR.ERROR_AE,
    "@DW_ERROR_LE_LABEL": STATE_DISHWASHER_ERROR.ERROR_LE,
    "@DW_ERROR_NE_LABEL": STATE_DISHWASHER_ERROR.ERROR_NE,
    "@DW_ERROR_BE_LABEL": STATE_DISHWASHER_ERROR.ERROR_BE,
}