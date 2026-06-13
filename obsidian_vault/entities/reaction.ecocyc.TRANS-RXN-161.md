---
entity_id: "reaction.ecocyc.TRANS-RXN-161"
entity_type: "reaction"
name: "TRANS-RXN-161"
source_database: "EcoCyc"
source_id: "TRANS-RXN-161"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-161

`reaction.ecocyc.TRANS-RXN-161`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-161`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + GALACTITOL -> GALACTITOL-1-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + GALACTITOL -> GALACTITOL-1-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by galactitol-specific PTS enzyme II (complex.ecocyc.CPLX0-231). Substrates: Galactitol (molecule.C01697), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: Galactitol 1-phosphate (molecule.C06311), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Enriched Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Annotation

Hpr-pi-phospho-L-histidines + GALACTITOL -> GALACTITOL-1-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-231|complex.ecocyc.CPLX0-231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06311|molecule.C06311]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01697|molecule.C01697]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-161`

## Notes

Hpr-pi-phospho-L-histidines + GALACTITOL -> GALACTITOL-1-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
