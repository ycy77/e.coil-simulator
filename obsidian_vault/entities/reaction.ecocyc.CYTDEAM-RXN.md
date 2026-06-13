---
entity_id: "reaction.ecocyc.CYTDEAM-RXN"
entity_type: "reaction"
name: "CYTDEAM-RXN"
source_database: "EcoCyc"
source_id: "CYTDEAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYTDEAM-RXN

`reaction.ecocyc.CYTDEAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYTDEAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. EcoCyc reaction equation: PROTON + WATER + CYTOSINE -> AMMONIUM + URACIL; direction=LEFT-TO-RIGHT. This reaction is part of the pyrimidine salvage pathway.

## Biological Role

Catalyzed by cytosine/isoguanine deaminase (complex.ecocyc.CPLX0-7932). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Cytosine (molecule.C00380). Products: Uracil (molecule.C00106), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-7194` pyrimidine nucleobases salvage II (EcoCyc)
- `ecocyc.PWY-7195` pyrimidine ribonucleosides salvage III (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway.

## Pathways

- `ecocyc.PWY-7194` pyrimidine nucleobases salvage II (EcoCyc)
- `ecocyc.PWY-7195` pyrimidine ribonucleosides salvage III (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7932|complex.ecocyc.CPLX0-7932]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2458|molecule.ecocyc.CPD0-2458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CYTDEAM-RXN`

## Notes

PROTON + WATER + CYTOSINE -> AMMONIUM + URACIL; direction=LEFT-TO-RIGHT
