
Signal Generator Firmware C.03.30 Readme

PLEASE NOTE: We recommends that you install the latest version of firmware for your instrument. Older firmware installed in a newly manufactured instrument may disable functionality of the instrument. The firmware files are provided for customers who require a re-installation into older instruments.
To Install This Firmware

    Download and install the PSG/ESG Upgrade Assistant onto your PC.
    Download and install firmware C.03.30 onto your PC.
    Run the PSG/ESG Upgrade Assistant and install firmware for your signal generator.

For further information, refer to the "Signal Generator Firmware Upgrade Guide" found below in "Documents & Downloads".
Features

    Conforms with 3PP Version 3.1 (1999-12). In addition, this new feature set coexists with the earlier ARIB (1.0-1.2) feature set, so users have access to either set.
    Supports the new 3.84 Mcps chip rate. In addition, it is possible to vary this rate by +/-10%, in order simulate clock drift between systems.
    Offers new channel types and configurations: - Downlink physical channels include PCCPCH, PSCH, SSCH, DPCH, CPICH, PICH, and OCNS. These channels are simulated with the slot structures defined by the 3GPP standard. Refer to the Technical Specifications (5965-3096E ) for a complete description. In addition to user control of individual channel configurations, test models 1, 2, and 3 defined by the 3GPP standard can be set up at the press of a button. This option also offers multicarrier capability on the downlink, and up to five Dedicated Physical Data Channels (DPDCH) plus a Dedicated Physical Control Channel (DPCCH) on the uplink.
    Provides individual channel rates based on a 7.5 ksps base for the downlink, and a 15 ksps for an uplink. The number of bits per timeslot is changed to reflect new data rates and channel configurations.
    Offers the ability to modify predefined setups, or to define and store custom user states using the built in table editor. - Choose spread code, symbol rate, scramble code, power, symbol rate, tDCPH offset, data pattern, TFCI, FBI, TPC pattern, number of pilot symbols, and pilot power offsets.

Improvements and Defects Fixed

    Improved chip rate to 3.84 Mcps in W-CDMA (3GPP 3.1 12-99) Component Test (Option UND Rev. A or better)
    Improved Arb clock phase noise between 1 and 10 kHz (Option UND Rev. D or better)

Hardware Compatibility

This code should be used in any box with the following hardware options:

    All standard ESG shipments (analog and digital with standard options)
    H97 WCDMA Special option
    H61 Triggers special and H60 IDEN special options
    H99 when it is shipped with UND, UN5 or H97 options

Restrictions

This code revision should NOT be used with:

    H98 WCDMA special option
    H65 EDGE special option
    H03 Single Channel CDMA option
    Any ESG with option 300

Update files are below
    SV5_130.bin
    SV5_134.bin
    
	

