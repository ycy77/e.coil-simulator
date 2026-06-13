---
entity_id: "reaction.ecocyc.TRANS-RXN0-446"
entity_type: "reaction"
name: "TRANS-RXN0-446"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-446"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-446

`reaction.ecocyc.TRANS-RXN0-446`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-446`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

N-acetyl-D-mannosamine + Hpr-pi-phospho-L-histidines -> N-ACETYL-D-MANNOSAMINE-6P + Hpr-Histidine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: N-acetyl-D-mannosamine + Hpr-pi-phospho-L-histidines -> N-ACETYL-D-MANNOSAMINE-6P + Hpr-Histidine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165). Substrates: N-Acetyl-D-mannosamine (molecule.C00645), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: N-Acetyl-D-mannosamine 6-phosphate (molecule.C04257), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

N-acetyl-D-mannosamine + Hpr-pi-phospho-L-histidines -> N-ACETYL-D-MANNOSAMINE-6P + Hpr-Histidine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04257|molecule.C04257]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00645|molecule.C00645]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-446`

## Notes

N-acetyl-D-mannosamine + Hpr-pi-phospho-L-histidines -> N-ACETYL-D-MANNOSAMINE-6P + Hpr-Histidine; direction=LEFT-TO-RIGHT
