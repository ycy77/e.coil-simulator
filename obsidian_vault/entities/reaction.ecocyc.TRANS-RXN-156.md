---
entity_id: "reaction.ecocyc.TRANS-RXN-156"
entity_type: "reaction"
name: "D-mannitol PTS permease"
source_database: "EcoCyc"
source_id: "TRANS-RXN-156"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-mannitol PTS permease

`reaction.ecocyc.TRANS-RXN-156`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-156`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + MANNITOL -> MANNITOL-1P + Hpr-Histidine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + MANNITOL -> MANNITOL-1P + Hpr-Histidine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannitol-specific PTS enzyme II CmtBA (complex.ecocyc.CPLX-156), mannitol-specific PTS enzyme II (complex.ecocyc.CPLX-166), sorbitol-specific PTS enzyme II (complex.ecocyc.CPLX-169). Substrates: Mannitol (molecule.C00392), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: D-Mannitol 1-phosphate (molecule.C00644), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + MANNITOL -> MANNITOL-1P + Hpr-Histidine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX-156|complex.ecocyc.CPLX-156]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-166|complex.ecocyc.CPLX-166]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-169|complex.ecocyc.CPLX-169]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00644|molecule.C00644]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00392|molecule.C00392]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00794|molecule.C00794]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-156`

## Notes

Hpr-pi-phospho-L-histidines + MANNITOL -> MANNITOL-1P + Hpr-Histidine; direction=LEFT-TO-RIGHT
