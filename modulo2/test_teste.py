def run_teste(inputs):
    script = open("funcoes.py", encoding="utf-8").read()
    answers = iter(inputs.splitlines())

    def input(prompt=""):
        return next(answers)

    exec(script, {"input": input, "__name__": "__main__"}) 


def test_numero_par_elevado(capsys):
    run_teste("4\n3")
    captured = capsys.readouterr()
    assert "O número é par." in captured.out
    assert "3 elevado a 3 é 27" in captured.out


def test_numero_impar_elevado(capsys):
    run_teste("5\n2")
    captured = capsys.readouterr()
    assert "O número é impar." in captured.out
    assert "2 elevado a 2 é 4" in captured.out