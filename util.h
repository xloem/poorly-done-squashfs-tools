#pragma once
typedef int (main_t)(int, char const*const*);

PyObject * PyWrapMain(char const * argv0, main_t main_f, PyObject *self, PyObject *params);
