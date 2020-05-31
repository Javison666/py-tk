import shelve

s = shelve.open('store.da')

def get_data(key):
    v=None
    try:
        v=s.get(key, None)
    finally:
        return v

def set_data(key, value):
    s[key] = value
