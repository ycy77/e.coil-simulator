---
entity_id: "reaction.ecocyc.TRANS-RXN-153"
entity_type: "reaction"
name: "TRANS-RXN-153"
source_database: "EcoCyc"
source_id: "TRANS-RXN-153"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-153

`reaction.ecocyc.TRANS-RXN-153`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-153`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

HYDROQUINONE-O-BETA-D-GLUCOPYRANOSIDE + Hpr-pi-phospho-L-histidines -> CPD-1162 + Hpr-Histidine; direction= EcoCyc reaction equation: HYDROQUINONE-O-BETA-D-GLUCOPYRANOSIDE + Hpr-pi-phospho-L-histidines -> CPD-1162 + Hpr-Histidine; direction=.

## Biological Role

Catalyzed by β-glucoside specific PTS enzyme II (complex.ecocyc.CPLX-153), β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase (complex.ecocyc.CPLX-154). Substrates: Arbutin (molecule.C06186), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: Arbutin 6-phosphate (molecule.C06187), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

HYDROQUINONE-O-BETA-D-GLUCOPYRANOSIDE + Hpr-pi-phospho-L-histidines -> CPD-1162 + Hpr-Histidine; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX-153|complex.ecocyc.CPLX-153]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-154|complex.ecocyc.CPLX-154]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06187|molecule.C06187]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06186|molecule.C06186]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-153`

## Notes

HYDROQUINONE-O-BETA-D-GLUCOPYRANOSIDE + Hpr-pi-phospho-L-histidines -> CPD-1162 + Hpr-Histidine; direction=
