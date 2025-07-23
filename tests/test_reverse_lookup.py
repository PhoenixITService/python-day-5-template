import glob
import builtins

def test_score_found(monkeypatch, capsys):
    py_files = glob.glob("*_reverse_lookup.py")
    assert py_files, "No *_reverse_lookup.py file found"

    monkeypatch.setattr(builtins, "input", lambda _: "88")

    with open(py_files[0], "r") as f:
        code = f.read()
        exec(code, {})

    captured = capsys.readouterr()
    assert captured.out.strip() == "Zoya", "Expected output 'Zoya' not found"

def test_score_not_found(monkeypatch, capsys):
    py_files = glob.glob("*_reverse_lookup.py")
    assert py_files, "No *_reverse_lookup.py file found"

    monkeypatch.setattr(builtins, "input", lambda _: "99")

    with open(py_files[0], "r") as f:
        code = f.read()
        exec(code, {})

    captured = capsys.readouterr()
    assert captured.out.strip() == "Not found", "Expected output 'Not found' not found"