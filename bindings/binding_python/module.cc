// Copyright (c) 2015 Vijos Dev Team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <Python.h>

#include "bindings/binding_python/error.h"
#include "bindings/binding_python/container.h"
#include "bindings/binding_python/target.h"
#include "bindings/binding_python/policy.h"

using namespace winc::python;

#if PY_MAJOR_VERSION >= 3
namespace {

struct PyModuleDef winc_module = {
  PyModuleDef_HEAD_INIT,
  "winc",
  NULL,
  -1
};

}
#endif

#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC PyInit_winc() {
#else
PyMODINIT_FUNC initwinc() {
#endif
  InitErrorClass();
  InitContainerType();
  InitTargetType();
  InitPolicyType();

#if PY_MAJOR_VERSION >= 3
  PyObject *module = PyModule_Create(&winc_module);
#else
  PyObject *module = Py_InitModule("winc", NULL);
#endif
  Py_INCREF(g_error_class);
  PyModule_AddObject(module, "Error", g_error_class);
  Py_INCREF(g_container_type);
  PyModule_AddObject(module, "Container", g_container_type);
  Py_INCREF(g_target_type);
  PyModule_AddObject(module, "Target", g_target_type);
  Py_INCREF(g_policy_type);
  PyModule_AddObject(module, "Policy", g_policy_type);

#if PY_MAJOR_VERSION >= 3
  return module;
#endif
}
