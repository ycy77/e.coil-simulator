---
entity_id: "reaction.ecocyc.2.7.13.1-RXN"
entity_type: "reaction"
name: "2.7.13.1-RXN"
source_database: "EcoCyc"
source_id: "2.7.13.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.7.13.1-RXN

`reaction.ecocyc.2.7.13.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.13.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Protein-Histidines -> Protein-pi-phospho-L-histidines + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Protein-Histidines -> Protein-pi-phospho-L-histidines + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sensor histidine kinase CusS (complex.ecocyc.CPLX0-8288). Substrates: ATP (molecule.C00002), a [protein]-L-histidine (molecule.ecocyc.Protein-Histidines). Products: ADP (molecule.C00008), H+ (molecule.C00080), a [protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Protein-pi-phospho-L-histidines).

## Annotation

ATP + Protein-Histidines -> Protein-pi-phospho-L-histidines + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8288|complex.ecocyc.CPLX0-8288]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-pi-phospho-L-histidines|molecule.ecocyc.Protein-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Histidines|molecule.ecocyc.Protein-Histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.13.1-RXN`

## Notes

ATP + Protein-Histidines -> Protein-pi-phospho-L-histidines + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
