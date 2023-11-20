// SPDX-License-Identifier: AGPL-3.0-or-later
//
// nyn-fitness: the dynamic recommendation fitness app
// Copyright (C) 2023 Amy Parker <amy@amyip.net>
//   				  Kevin Ramirez <thekevinramirez@csu.fullerton.edu>
//   				  Nicholas Goulart <nick.goulart@csu.fullerton.edu>
//   				  Theresa Nguyen <ttnguyen1011@csu.fullerton.edu>
//   				  Dat Lam <Dlam42@csu.fullerton.edu>
//   				  Srinidhi Chevvuri <srinidhi.chevvuri@csu.fullerton.edu>
//
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation; either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA or visit the
// GNU Project at https://gnu.org/licenses. The GNU Affero General Public
// License version 3 is available at, for your convenience,
// https://www.gnu.org/licenses/agpl-3.0.en.html.

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <cstddef>
#include <iostream>
#include <deque>
#include <algorithm>

#include "common.h"
#include "mathtools.h"

#define CN_ATTR 16

class WorkoutSortable {
    private:
        Py_ssize_t id;
        f64 score;
    public:
        WorkoutSortable(Py_ssize_t vid, f64 *w, f64 *u) {
            id = vid;
            score = dotProduct(w, u, CN_ATTR);
        }
        friend bool operator<(const WorkoutSortable &lhs,
                              const WorkoutSortable rhs) {
            return lhs.score < rhs.score;
        }
        Py_ssize_t getId() const {
            return id;
        }
};

#define CLEAN_EXIT PyErr_Clear(); Py_RETURN_NONE;

// Throwing nullptr = bailing out
static f64 *getCVector(PyObject *vec) {
    if (PyList_Size(vec) != CN_ATTR) [[unlikely]]
        return nullptr;
    f64 *res = new f64[CN_ATTR];
    for (Py_ssize_t i = 0; i < CN_ATTR; ++i) {
        PyObject *item = PyList_GetItem(vec, i);
        if (!PyFloat_Check(item)) [[unlikely]]
            return nullptr;
        res[i] = PyFloat_AsDouble(item);
        if (PyErr_Occurred()) [[unlikely]] {
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

static PyObject *nyn_recommender_test(PyObject *self,
                                      PyObject *args) {
    CLEAN_EXIT;
}

static PyObject *fast_unit_vector(PyObject *self, PyObject *args) {
    PyObject *v;
    PyArg_ParseTuple(args, "O", &v);
    f64 *vec = getCVector(v);
    if (vec == nullptr) [[unlikely]] {
        CLEAN_EXIT;
    }
    makeVectorUnitInPlace(vec, CN_ATTR);
    return getPythonVector(vec);
}

static PyObject *recommend(PyObject *self, PyObject *args) {
    PyObject *user; // user preferences unit vector
    PyObject *matches; // workout unit vector matches
    Py_ssize_t count; // top n to return
    PyArg_ParseTuple(args, "OOn", &user, &matches, &count);
    if (PyErr_Occurred()) [[unlikely]] {
        CLEAN_EXIT;
    }

    f64 *uv = getCVector(user);
    if (uv == nullptr) [[unlikely]] { CLEAN_EXIT; }
    std::deque<WorkoutSortable> pq;
    for (Py_ssize_t i = 0; i < PyList_Size(matches); ++i) {
        f64 *wv = getCVector(PyList_GetItem(matches, i));
        if (wv == nullptr) [[unlikely]] { CLEAN_EXIT; }
        pq.push_back(WorkoutSortable(i, wv, uv));
        std::make_heap(pq.begin(), pq.end());
        if (static_cast<Py_ssize_t>(pq.size()) > count) [[likely]]
            pq.pop_back();
    }

    PyObject *ret = PyList_New(count);
    Py_ssize_t i = 0;
    for (WorkoutSortable &e : pq)
        PyList_SetItem(ret, i++, PyLong_FromSsize_t(e.getId()));
    return ret;
}

static PyMethodDef NYNMethods[] = {
    {"test", nyn_recommender_test, METH_VARARGS, "Test the module."},
    {"gen_uv", fast_unit_vector, METH_VARARGS, "Generate unit vector."},
    {"recommend", recommend, METH_VARARGS, "Recommend videos."},
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