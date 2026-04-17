TaraLists
=========

.. image:: https://github.com/taradix/taralists/workflows/test/badge.svg
       :target: https://github.com/taradix/taralists/actions
.. image:: https://github.com/taradix/taralists/workflows/deploy/badge.svg
       :target: https://mail.taram.ca

Liste de diffusion à Taram.

Setup
-----

Configure taramail to relay mail for the lists domain to the taralists
postfix service:

.. code-block:: text

    taramail post_domain --relay-all-recipients lists.taram.ca
    taramail post_transport lists.taram.ca '[taralists-postfix]:25'
