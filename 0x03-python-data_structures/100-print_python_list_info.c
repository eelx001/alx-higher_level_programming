#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
VIEW HEADER-> https://github.com/python/cpython/blob/master/Include/listobject.h
VIEW MANUAL-> https://docs.python.org/3.4/c-api/list.html
VIEW HEADER-> https://docs.python.org/3.4/c-api/structures.html
VIEW MANUAL-> https://github.com/python/cpython/blob/master/Include/object.h
* print_python_list_info - Prints some basic info about pytohn list.
* @p: Python object.
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
