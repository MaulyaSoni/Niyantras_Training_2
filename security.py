def check_medium(medium : str):
    
    if medium != "email" or medium != "sms" or medium != "push":
        raise Exception ("Invalid Input of pref medium  , try one of these (email , push , sms)")
    
    return medium