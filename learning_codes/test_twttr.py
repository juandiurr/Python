from twttr import shorten,vocales

def test_shorten():
    assert shorten("hola") == "hl"
    assert shorten("HOLA") == "HL"
    assert shorten("hl") == "hl"
def test_vocales():
    assert vocales("hola") == ['o','a']
    assert vocales("holaa") == ['o','a']
    assert vocales("aoaoaa") == ['a','o']
    assert vocales("putaperrasexo") == ['u','a','e','o']
    assert vocales("twtrr") == -1
    