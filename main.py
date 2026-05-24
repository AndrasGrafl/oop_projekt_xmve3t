from FoglalasiRendszer import FoglalasiRendszer
from FelhasznaloiFelulet import FelhasznaloiFelulet

if __name__ == "__main__":
    rendszer = FoglalasiRendszer()
    felulet = FelhasznaloiFelulet(rendszer)
    felulet.user_interact()
