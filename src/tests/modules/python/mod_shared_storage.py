import freeradius
import shared


def authorize(p):
    freeradius.log(
        freeradius.L_DBG,
        "Python - shared_attribute=" + str(hasattr(shared, "shared_attribute")),
    )
    if hasattr(shared, "shared_attribute"):
        return freeradius.RLM_MODULE_OK
    setattr(shared, "shared_attribute", True)
    return freeradius.RLM_MODULE_NOOP
