# tdd-ul-dl-configcommon-calc
## [TDD-UL-DL-ConfigCommon](https://github.com/KRIISHSHARMA/OAI-config)

``` bash
# subcarrierSpacing
# 0=kHz15, 1=kHz30, 2=kHz60, 3=kHz120
      referenceSubcarrierSpacing                                    = 1;
      # pattern1
      # dl_UL_TransmissionPeriodicity
      # 0=ms0p5, 1=ms0p625, 2=ms1, 3=ms1p25, 4=ms2, 5=ms2p5, 6=ms5, 7=ms10
      dl_UL_TransmissionPeriodicity                                 = 5; #thamizh change
      nrofDownlinkSlots                                             = 3; #thamizh change
      nrofDownlinkSymbols                                           = 6; #thamizh change
      nrofUplinkSlots                                               = 1; #thamizh change
      nrofUplinkSymbols                                             = 4; #thamizh change
      #luis config
      #dl_UL_TransmissionPeriodicity                                 = 6; #thamizh change
      #nrofDownlinkSlots                                             = 7; #thamizh change
      #nrofDownlinkSymbols                                           = 6; #thamizh change
      #nrofUplinkSlots                                               = 2; #thamizh change
      #nrofUplinkSymbols                                             = 4; #thamizh change

```
- [reference](https://www.telecomhall.net/t/identify-tdd-dl-ul-configuration-from-log/21325/2)
- [reference](https://techbarnwireless.blogspot.com/2019/03/frame-structure-and-slot-configuration.html)
- [reference](https://www.sharetechnote.com/html/5G/5G_tdd_UL_DL_configurationCommon.html)
- [reference](https://www.5gfundamental.com/2020/05/tdd-ul-dl-slot-configuration.html)
- [reference](https://www.linkedin.com/pulse/5g-nr-tdd-slot-configuration-andrew-kolomatski/)
- **referenceSubcarrierSpacing** : Reference SCS used to determine the time domain boundaries in the UL-DL pattern which must be common across all subcarrier specific carriers, i.e., independent of the actual subcarrier spacing using for data transmission. Only the values 15, 30 or 60 kHz (FR1), and 60 or 120 kHz (FR2) are applicable. The network configures a not larger than any SCS of configured BWPs for the serving cell. The network or SL-PreconfigGeneralconfigures a not larger than the SCS of (pre-)configured SL BWP.See TS 38.213 [13], clause 11.1.

- **dl-UL-TransmissionPeriodicity** : Periodicity of the DL-UL pattern, see TS 38.213 [13], clause 11.1.If the dl-UL-TransmissionPeriodicity-v1530 is signalled, UE shall ignore the dl-UL-TransmissionPeriodicity (without suffix).

![1679464309298](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/039b60c3-bbc8-41d6-867f-85ad6b00696a)
![tddpri](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/ad824c27-0524-4839-8250-3a7d28bdd782)

- **nrofDownlinkSlots** : Number of consecutive full DL slots at the beginning of each DL-UL pattern, see TS 38.213 [13], clause 11.1. In this release, the maximum value for this field is 80.

- **nrofDownlinkSymbols** : Number of consecutive DL symbols in the beginning of the slot following the last full DL slot (as derived from nrofDownlinkSlots). The value 0 indicates that there is no partial-downlink slot. (see TS 38.213 [13], clause 11.1).

- **nrofUplinkSlots** : Number of consecutive full UL slots at the end of each DL-UL pattern, see TS 38.213 [13], clause 11.1. In this release, the maximum value for this field is 80. 

- **nrofUplinkSymbols** : Number of consecutive UL symbols in the end of the slot preceding the first full UL slot (as derived from nrofUplinkSlots). The value 0 indicates that there is no partial-uplink slot. (see TS 38.213 [13], clause 11.1).

![IMG_20231217_195712](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/e67a6f9b-c136-44fc-a47b-38a319d8bafa)
![IMG_20231217_195647](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/71c3597e-2378-472a-93ec-5cb6c8cedc89)

