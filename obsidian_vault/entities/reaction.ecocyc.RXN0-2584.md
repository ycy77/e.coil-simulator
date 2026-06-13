---
entity_id: "reaction.ecocyc.RXN0-2584"
entity_type: "reaction"
name: "RXN0-2584"
source_database: "EcoCyc"
source_id: "RXN0-2584"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2584

`reaction.ecocyc.RXN0-2584`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2584`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Uracil can be generated in DNA as a result of misincorporation by DNA polymerase, spontaneous deamination of cytosine, and deamination of cytosine induced by bisulfite or nitrous acid. Removal of these uracils is accomplished by the Base-Excision Repair (BER) mechanism which hydrolyzes the N-glycosylic bond between the deoxyribose and the base leaving an AP (apurinic or apyrimidinic) site. EcoCyc reaction equation: DNA-with-Uracils + WATER -> DNA-containing-abasic-Sites + URACIL; direction=PHYSIOL-LEFT-TO-RIGHT. Uracil can be generated in DNA as a result of misincorporation by DNA polymerase, spontaneous deamination of cytosine, and deamination of cytosine induced by bisulfite or nitrous acid. Removal of these uracils is accomplished by the Base-Excision Repair (BER) mechanism which hydrolyzes the N-glycosylic bond between the deoxyribose and the base leaving an AP (apurinic or apyrimidinic) site.

## Biological Role

Catalyzed by ATP-dependent helicase/uracil glycosylase Lhr (complex.ecocyc.CPLX0-8581), ung (protein.P12295). Substrates: H2O (molecule.C00001). Products: Uracil (molecule.C00106).

## Annotation

Uracil can be generated in DNA as a result of misincorporation by DNA polymerase, spontaneous deamination of cytosine, and deamination of cytosine induced by bisulfite or nitrous acid. Removal of these uracils is accomplished by the Base-Excision Repair (BER) mechanism which hydrolyzes the N-glycosylic bond between the deoxyribose and the base leaving an AP (apurinic or apyrimidinic) site.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8581|complex.ecocyc.CPLX0-8581]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P12295|protein.P12295]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2584`

## Notes

DNA-with-Uracils + WATER -> DNA-containing-abasic-Sites + URACIL; direction=PHYSIOL-LEFT-TO-RIGHT
