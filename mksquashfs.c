#include <Python.h>
#include "util.h"

main_t squashfs_main;

static PyObject * mksquashfs(PyObject *self, PyObject *params)
{
    return PyWrapMain("mksquashfs", squashfs_main, self, params);
}

static PyObject * sqfstar(PyObject *self, PyObject *params)
{
    return PyWrapMain("sqfstar", squashfs_main, self, params);
}

static PyMethodDef mksquashfsMethods[] = {
    {"mksquashfs", mksquashfs, METH_VARARGS, "create and append to a squashfs"},
    {"sqfstar", sqfstar, METH_VARARGS, "create a squashfs from a tar archive"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef unsquashfsmodule = {
    PyModuleDef_HEAD_INIT,
    "mksquashfs",   /* name of module */
    NULL, /*mksquashfs_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    mksquashfsMethods
};

PyMODINIT_FUNC
PyInit_mksquashfs(void)
{
    return PyModule_Create(&unsquashfsmodule);
}
