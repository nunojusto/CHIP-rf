CHIP-rf
======

Introduction
------------

Python module for sending and receiving 433/315MHz LPD/SRD signals with generic low-cost GPIO RF modules on a CHIP Computer for Next Thing Co (NTC).
This was ported from rpi-rf module

Protocol and base logic ported from `rc-switch`_.

Supported hardware
------------------

Most generic 433/315MHz capable modules (cost: ~2€) connected via GPIO to a CHIP computer.

.. figure:: http://i.imgur.com/vG89UP9.jpg
   :alt: 433modules

Compatibility
-------------

Generic RF outlets and most 433/315MHz switches (cost: ~15€/3pcs).

.. figure:: http://i.imgur.com/WVRxvWe.jpg
   :alt: rfoutlet


Chipsets:

* SC5262 / SC5272
* HX2262 / HX2272
* PT2262 / PT2272
* EV1527 / RT1527 / FP1527 / HS1527

For a full list of compatible devices and chipsets see the `rc-switch Wiki`_

Dependencies
------------

::

    CHIP.GPIO
you can find information here `CHIP_IO`_

Installation (not working yet)
------------

On CHIP, install the *CHIP-rf* module via pip.

Python 3::

    # apt-get install python3-pip
    # pip3 install CHIP-rf

Wiring diagram (example)
------------------------

CHIP::

    TX:
       GND > PIN (GND)
       VCC > PIN (5V)
      DATA > PIN (CSID1)

    RX:
       VCC > PIN (5V)
      DATA > PIN (CSID0)
       GND > PIN (GND)

Usage
-----

See `scripts`_ (`chip-rf_send`_, `chip-rf_receive`_) which are also shipped as cmdline tools.

Open Source
-----------

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues

.. _rc-switch: https://github.com/sui77/rc-switch
.. _rc-switch Wiki: https://github.com/sui77/rc-switch/wiki
.. _rpi-rf: https://github.com/milaq/rpi-rf
.. _CHIP_IO: https://github.com/xtacocorex/CHIP_IO
.. _BSD Licence: http://www.linfo.org/bsdlicense.html
.. _GitHub: https://github.com/nunojusto/chip-rf
.. _GitHub issues: https://github.com/nunojusto/chip-rf/issues
.. _scripts: https://github.com/nunojusto/chip-rf/blob/master/scripts
.. _chip-rf_send: https://github.com/nunojusto/chip-rf/blob/master/scripts/chip-rf_send
.. _chip-rf_receive: https://github.com/nunojusto/chip-rf/blob/master/scripts/chip-rf_receive
