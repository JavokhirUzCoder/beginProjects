#  pip install eel
#  pip install eel[jinja2] 

import eel  
eel.init("web")



@eel.expose
def MainFunc(code):
    import sys
    from io import StringIO
    import contextlib

    Result = ""
    @contextlib.contextmanager
    def stdoutIO(stdout = None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    with stdoutIO() as s:
        try:
            exec(code)
        except:
            Result = "Something wrong with the code"
        else:
            Result = str(s.getvalue())

    return Result

# def MainFunc(code):
#     import sys
#     from io import StringIO
#     import contextlib

#     Result = ""
#     @contextlib.contextmanager
#     def stdoutIO(stdout = None):
#         old = sys.stdout
#         if stdout is None:
#             stdout = StringIO()
#         sys.stdout = stdout
#         yield stdout
#         sys.stdout = old

#     with stdoutIO() as s:
#         try:
#             exec(code)
#         except:
#             Result = "Something wrong with the code"
#         else:
#             Result = str(s.getvalue())
#     # print (Result)
#     return Result




eel.start("index.html", size =(700, 700))


