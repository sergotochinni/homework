import logg


def check_in(n1: str, n2: str):
    try:
        m1, m2 = int(n1), int(n2)
    except ValueError:
        try:
            m1, m2 = float(n1), float(n2)
        except ValueError:
            logg.logging.warning(f"Incorrect data entered: '{n1}', '{n2}'!")
            return 0, 0, False
        else: # float
            return m1, m2, True
    else: # int
        return m1, m2, True


def check_zero(n2):
    if n2 == 0: 
        logg.logging.warning("Incorrect data entered: '0'!")
        return True
    return False


def check_in_complex(n1real, n1img, n2real, n2img):
    try:
        m1 = complex(int(n1real), int(n1img))
        m2 = complex(int(n2real), int(n2img))
    except ValueError:
        logg.logging.warning(f"Incorrect data entered: '{n1real}', '{n1img}', '{n2real}', '{n2img}'!")
        return 0, 0, False
    else:
        return m1, m2, True
