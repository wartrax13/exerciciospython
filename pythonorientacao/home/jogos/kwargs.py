def teste_args_kwargs(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg:2', arg2)
    print('arg:3', arg3)


args = ('um', 2, 3)
teste_args_kwargs(*args)

kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
teste_args_kwargs(**kwargs)