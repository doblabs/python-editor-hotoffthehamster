import sys

import editor


def test_editor(capfd):
    cont = editor.edit(contents="ABC!", use_tty="use_tty" in sys.argv)
    sys.stdout.write(cont.decode())
    out, err = capfd.readouterr()
    assert err == (
        "Vim: Warning: Output is not to a terminal\n"
        "Vim: Warning: Input is not from a terminal\n"
    )
