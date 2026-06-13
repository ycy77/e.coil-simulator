---
entity_id: "reaction.ecocyc.RXN0-17"
entity_type: "reaction"
name: "transport of N-acetyl-D-muramate"
source_database: "EcoCyc"
source_id: "RXN0-17"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# transport of N-acetyl-D-muramate

`reaction.ecocyc.RXN0-17`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-17`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + NACMUR -> CPD0-881 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + NACMUR -> CPD0-881 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by N-acetylmuramic acid-specific PTS enzyme II (complex.ecocyc.CPLX0-7). Substrates: N-Acetylmuramate (molecule.C02713), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: N-Acetylmuramic acid 6-phosphate (molecule.C16698), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + NACMUR -> CPD0-881 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7|complex.ecocyc.CPLX0-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C16698|molecule.C16698]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02713|molecule.C02713]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-17`

## Notes

Hpr-pi-phospho-L-histidines + NACMUR -> CPD0-881 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
