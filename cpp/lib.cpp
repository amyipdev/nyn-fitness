#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <cstddef>
#include <iostream>

#include "common.h"
#include "mathtools.h"

#define CN_ATTR 16

// Throwing nullptr = bailing out
static f64 *getCVector(PyObject *vec) {
    if (PyList_Size(vec) != CN_ATTR)
        return nullptr;
    f64 *res = new f64[CN_ATTR];
    for (Py_ssize_t i = 0; i < CN_ATTR; ++i) {
        PyObject *item = PyList_GetItem(vec, i);
        if (!PyFloat_Check(item))
            return nullptr;
        res[i] = PyFloat_AsDouble(item);
        if (PyErr_Occurred()) {
            delete[] res;
            return nullptr;
        }
    }
    return res;
}

static PyObject *getPythonVector(f64 *vec) {
    PyObject *v = PyList_New(16);
    for (Py_ssize_t i = 0; i < CN_ATTR; ++i)
        PyList_SetItem(v, i, PyFloat_FromDouble(vec[i]));
    return v;
}

static PyObject *nyn_recommender_test(PyObject *self, PyObject *args) {
    Py_RETURN_NONE;
}

static PyObject *fast_unit_vector(PyObject *self, PyObject *args) {
    PyObject *v;
    PyArg_ParseTuple(args, "O", &v);
    f64 *vec = getCVector(v);
    if (vec == nullptr) {
        PyErr_Clear();
        Py_RETURN_NONE;
    }
    makeVectorUnitInPlace(vec, CN_ATTR);
    return getPythonVector(vec);
}

static PyMethodDef NYNMethods[] = {
    {"test", nyn_recommender_test, METH_VARARGS, "Test the module."},
    {"gen_uv", fast_unit_vector, METH_VARARGS, "Generate unit vector."},
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