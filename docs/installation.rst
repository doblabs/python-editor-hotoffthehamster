############
Installation
############

.. vim:tw=0:ts=3:sw=3:et:norl:nospell:ft=rst

.. |virtualenv| replace:: ``virtualenv``
.. _virtualenv: https://virtualenv.pypa.io/en/latest/

.. |workon| replace:: ``workon``
.. _workon: https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html?highlight=workon#workon

To install system-wide, run as superuser::

    $ pip3 install python-editor-hotoffthehamster

To install user-local, simply run::

    $ pip3 install -U python-editor-hotoffthehamster

To install within a |virtualenv|_, try::

    $ cd "$(mktemp -d)"

    $ python3 -m venv .venv

    $ . ./.venv/bin/activate

    (python-editor-hotoffthehamster) $ pip install python-editor-hotoffthehamster

To develop on the project, link to the source files instead::

    (python-editor-hotoffthehamster) $ deactivate
    $ git clone git@github.com:doblabs/python-editor-hotoffthehamster.git
    $ cd python-editor-hotoffthehamster
    $ python3 -m venv python-editor-hotoffthehamster
    $ . ./.venv/bin/activate
    (python-editor-hotoffthehamster) $ make develop

After creating the virtual environment, it's easy to start
developing from a fresh terminal::

    $ cd python-editor-hotoffthehamster
    $ . ./.venv/bin/activate
    (python-editor-hotoffthehamster) $ ...

