#include <Python.h>

static PyObject *nyn_recommender_test(PyObject *self, PyObject *args) {
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef NYNMethods[] = {
    {"test", nyn_recommender_test, METH_VARARGS, "Test the module."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef nyn_recommender_module {
    PyModuleDef_HEAD_INIT,
    "nyn_recommender",
    0, /* documentation pointer */
    -1, /* global/static variable state */
    NYNMethods
};

PyMODINIT_FUNC PyInit_nyn_recommender() {
    return PyModule_Create(&nyn_recommender_module);
}