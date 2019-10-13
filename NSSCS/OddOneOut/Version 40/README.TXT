
Signal Generator Firmware C.03.40 Readme

PLEASE NOTE: We recommends that you install the latest version of firmware for your instrument. Older firmware installed in a newly manufactured instrument may disable functionality of the instrument. The firmware files are provided for customers who require a re-installation into older instruments.
To Install This Firmware

    Download and install the PSG/ESG Upgrade Assistant onto your PC.
    Download and install firmware C.03.40 onto your PC.
    Run the PSG/ESG Upgrade Assistant and install firmware for your signal generator.

For further information, refer to the "PSG/ESG Firmware Upgrade Guide" found in "Documents & Downloads" below.
Features

With the introduction of Option 201, We is providing a significant edge in signal generation for customers developing products for the CDMA marketplace. The ESG/Option 201 can be used to provide fully coded, multi-channel stimulus signals supporting both the IS-95 and IS-2000 CDMA standards. These signals can be used to test receiver performance (bit error rates, frame error rates) and low level protocol handling for CDMA products. Features include:

    Real-time generation of both cdmaOne and cdma2000 signals to emulate a base station
    Fully coded IS-95 signal package including pilot, sync, paging, and traffic channels
    Fully coded IS-2000 signals including fundamental and supplemental channels at rates up to 307.2 kbps
    Full control of paging message stream (overhead and signaling messages)
    Supports both convolutional and turbo coding
    User data insertion via user files or external data
    Variable chip rates
    Fully configurable sync channel base station parameters
    Radio Configurations, RC1-RC2 with one box and RC1-RC5 with two boxes
    Combining multiple ESGs can expand number of channels. The user can utilize 2 ESGs to provide multi-channel capability at Spread Rate 1 and Radio Configuration 1-5

Improvements and Defects Fixed

    SCPI filter IS2000SR3DS query returned incorrect value, Option UND. (All CDMA formats)
    Sweep pre-calculation was intermittently incorrect. (List/Sweep)
    FP polarity keys are blanked with UN3/4, Option UND. (ARB 3GPP)
    Changed ARB 3GPP scramble code default to 0, Option UND

Hardware Compatibility

This code should be used in any box with the following hardware options:

    All standard ESG shipments (analog and digital with standard options)
    H97 WCDMA Special option
    H61 Triggers special and H60 IDEN special options
    H99 when it is shipped with UND, UN5 or H97 options
    Any ESG with option 300

Restrictions

This code revision should NOT be used with:

    H98 WCDMA special option
    H65 EDGE special option
    H03 Single Channel CDMA option

update files are below
    IT-I11T.bin
    IT-I12T.bin
    IT-I13T.bin

