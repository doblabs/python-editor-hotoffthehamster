import sys

import editor


def test_editor(capfd):
    cont = editor.edit(contents="ABC!", use_tty="use_tty" in sys.argv)
    sys.stdout.write(cont.decode())
    out, err = capfd.readouterr()
    # I see two Warnings locally, and too many Warnings on GHA CI.
    # - Though it might be my local EDITOR setting vs. CI's.
    assert (
        err
        == (
            "Vim: Warning: Output is not to a terminal\n"
            "Vim: Warning: Input is not from a terminal\n"
        )
        or err == "Too many errors from stdin\n"
    )
