---
entity_id: "reaction.ecocyc.2.7.1.148-RXN"
entity_type: "reaction"
name: "2.7.1.148-RXN"
source_database: "EcoCyc"
source_id: "2.7.1.148-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "CMK"
  - "4-diphosphocytidyl-2-C-methyl-D-erythritol kinase"
---

# 2.7.1.148-RXN

`reaction.ecocyc.2.7.1.148-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.1.148-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-CYTIDINE-5-DIPHOSPHO-2-C + ATP -> PROTON + 2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 4-CYTIDINE-5-DIPHOSPHO-2-C + ATP -> PROTON + 2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase (complex.ecocyc.CPLX0-3841). Substrates: ATP (molecule.C00002), 4-(Cytidine 5'-diphospho)-2-C-methyl-D-erythritol (molecule.C11435). Products: ADP (molecule.C00008), H+ (molecule.C00080), 2-Phospho-4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol (molecule.C11436).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

4-CYTIDINE-5-DIPHOSPHO-2-C + ATP -> PROTON + 2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3841|complex.ecocyc.CPLX0-3841]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11436|molecule.C11436]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11435|molecule.C11435]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.1.148-RXN`

## Notes

4-CYTIDINE-5-DIPHOSPHO-2-C + ATP -> PROTON + 2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET + ADP; direction=LEFT-TO-RIGHT
