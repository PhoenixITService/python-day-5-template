import glob

def test_tuple_sort_output():
    py_files = glob.glob("*_tuple_sort.py")
    assert py_files, "No *_tuple_sort.py file found"

    with open(py_files[0], "r") as f:
        content = f.read()
        assert "data" in content, "'data' list not found in the file"

        namespace = {}
        exec(content, namespace)

        assert "data" in namespace, "'data' not defined properly"

        expected_output = ['D', 'B', 'A', 'E', 'C']

        matching_lists = [
            val for val in namespace.values()
            if isinstance(val, list) and val == expected_output
        ]

        assert matching_lists, f"No output matched the expected result: {expected_output}"
