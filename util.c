#include <Python.h>
#include "util.h"

#include <setjmp.h>

static jmp_buf exit_jmp;
void exit(int sts)
{
    longjmp(exit_jmp, sts);
}

PyObject * PyWrapMain(char const * argv0, main_t main_f, PyObject *self, PyObject *params)
{
    int sts, argc;
    char const * * argv;
    PyObject **paramsp;
    params = PySequence_Fast(params, NULL);
    argc = PySequence_Fast_GET_SIZE(params) + 1;
    argv = PyMem_RawMalloc(sizeof(char const *) * argc);
    argv[0] = argv0;
    paramsp = PySequence_Fast_ITEMS(params);
    for (int argi = 1; argi < argc; ++ argi) {
        argv[argi] = PyUnicode_AsUTF8(paramsp[argi - 1]);
    }
    sts = setjmp(exit_jmp);
    if (sts == 0) {
        sts = main_f(argc, argv);
    }
    PyMem_RawFree(argv);
    return PyLong_FromLong(sts);
}
