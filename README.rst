Product Unit of Measure Extension
=================================

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3


Very small module, that fixes display of few product quantity fields to correspond to
your ``Decimal Accuracy`` setting ``Product Unit of Measure``.

Especially useful when you work exclusively with whole units and pieces.


Configure Product Unit of Measure
---------------------------------

Switch to the developer mode, open the `Settings` app, and navigate to
`Technical` -> `Database structure` -> `Decimal Accuracy`. Select
``Product Unit of Measure`` and choose your desired numbers of digits, 0 for full units.


Currently handled fields
------------------------

* sold and purchased quantities on products and templates
* inventoried and available for stock quants


Bug Tracker
-----------

You found another quantity, that should be displayed according to
``Product Unit of Measure`` digits?

Please file an issue on `GitHub Issues <https://github.com/ayudoo/product_unit_of_measure_extension>`_.
Thank You!


Credits
-------

Authors
^^^^^^^

* Michael Jurke
* Ayudoo Ltd <support@ayudoo.bg>
