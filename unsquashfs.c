#include <Python.h>
#include "util.h"

main_t squashfs_main;

/*static PyObject *
unsquashfs_main(char const * argv0, PyObject *self, PyObject *params)
{
    int sts, argc;
    char const * * argv;
    params = PySequence_Fast(params, NULL);
    argc = PySequence_Fast_GET_SIZE(params) + 1;
    argv = PyMem_RawMalloc(sizeof(char const *) * argc);
    argv[0] = argv0;
    for (int argi = 1; argi < argc; ++ argi) {
        PyObject * paramobj = PySequence_Fast_GET_ITEM(params, argi - 1);
        argv[argi] = PyUnicode_AsUTF8(paramobj);
    }
    sts = setjmp(exit_jmp);
    if (sts == 0) {
        sts = squashfs_main(argc, argv);
    }
    PyMem_RawFree(argv);
    return PyLong_FromLong(sts);
}
*/

static PyObject * unsquashfs(PyObject *self, PyObject *params)
{
    return PyWrapMain("unsquashfs", squashfs_main, self, params);
}

static PyObject * sqfscat(PyObject *self, PyObject *params)
{
    return PyWrapMain("sqfscat", squashfs_main, self, params);
}

static PyMethodDef unsquashfsMethods[] = {
    {"unsquashfs", unsquashfs, METH_VARARGS, "uncompress, extract and list a squashfs"},
    {"sqfscat", sqfscat, METH_VARARGS, "cat files from a squashfs"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef unsquashfsmodule = {
    PyModuleDef_HEAD_INIT,
    "unsquashfs",   /* name of module */
    NULL, /*unsquashfs_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    unsquashfsMethods
};

PyMODINIT_FUNC
PyInit_unsquashfs(void)
{
    return PyModule_Create(&unsquashfsmodule);
}
