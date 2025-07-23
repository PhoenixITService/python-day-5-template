import glob
import subprocess
import sys

def test_set_elements():
    py_files = glob.glob("*_set_elements.py")
    assert py_files, "No *_set_elements.py file found"

    # Run the first matching file and capture output
    result = subprocess.run(
        [sys.executable, py_files[0]],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, f"Script exited with error:\n{result.stderr}"

    output = result.stdout.strip()

    expected_output = "Elements in exactly 2 sets: {1, 4, 6, 9}"
    assert output == expected_output, f"Unexpected output:\nExpected: {expected_output}\nGot: {output}"