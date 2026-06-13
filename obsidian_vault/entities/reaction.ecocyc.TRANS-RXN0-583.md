---
entity_id: "reaction.ecocyc.TRANS-RXN0-583"
entity_type: "reaction"
name: "TRANS-RXN0-583"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-583"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-583

`reaction.ecocyc.TRANS-RXN0-583`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-583`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-3582 + Hpr-pi-phospho-L-histidines -> Hpr-Histidine + CPD-16619; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3582 + Hpr-pi-phospho-L-histidines -> Hpr-Histidine + CPD-16619; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glucose-specific PTS enzyme II (complex.ecocyc.CPLX-157). Substrates: methyl α-D-glucoside (molecule.ecocyc.CPD-3582), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: methyl α-D-glucoside 6-phosphate (molecule.ecocyc.CPD-16619), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

CPD-3582 + Hpr-pi-phospho-L-histidines -> Hpr-Histidine + CPD-16619; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-157|complex.ecocyc.CPLX-157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-16619|molecule.ecocyc.CPD-16619]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3582|molecule.ecocyc.CPD-3582]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-583`

## Notes

CPD-3582 + Hpr-pi-phospho-L-histidines -> Hpr-Histidine + CPD-16619; direction=LEFT-TO-RIGHT
