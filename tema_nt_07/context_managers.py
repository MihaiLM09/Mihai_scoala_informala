# class just_some_exceptions:
#     def __init__(self):
#         print('Sa vedem daca merge?')
#
#     def __enter__(self):
#         print('Incepem')
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type == None:
#             print('Am terminat cu bine')
#         else:
#             print('Avem o eroare')
#
# # normal
# with just_some_exceptions() as jsx:
#     print('A mers foarte bine!')
# print('Chiar am rezolvat.')
#
# # exceptie
# with just_some_exceptions() as jsx:
#     print('Pare ca nu e ok!')
#     a = 10/0
# print('Nu e ok.')

###########################################

# class just_some_exceptions:
#     def __enter__(*args):
#         print('enter')
#         return 'treci la treaba'
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#         if exc_type is not None:
#             print('error', exc_type)
#         return True
#
# with just_some_exceptions() as jse:
#     print(jse)
#     #raise KeyError
#     raise IndexError

##########################################

import contextlib

@contextlib.contextmanager
def just_some_exception():
    try:
        print('start')
        yield 'incearca mai mult'
    except KeyError:
        print('KeyError')
        pass
    except IndexError:
        print('IndexError')
    print('stop')

with just_some_exception() as jse:
    print(jse)
    raise KeyError
    #raise IndexError





