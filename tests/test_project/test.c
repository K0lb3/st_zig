#include "Python.h"

static PyModuleDef test_def = {
    PyModuleDef_HEAD_INIT,
    "test", // Module name
    "",
    -1,   // Optional size of the module state memory
    NULL, // Optional table of module-level functions
    NULL, // Optional slot definitions
    NULL, // Optional traversal function
    NULL, // Optional clear function
    NULL  // Optional module deallocation function
};

PyMODINIT_FUNC PyInit_test(void) { return PyModule_Create(&test_def); }
