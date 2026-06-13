---
entity_id: "reaction.ecocyc.DEOXYINOPHOSPHOR-RXN"
entity_type: "reaction"
name: "DEOXYINOPHOSPHOR-RXN"
source_database: "EcoCyc"
source_id: "DEOXYINOPHOSPHOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEOXYINOPHOSPHOR-RXN

`reaction.ecocyc.DEOXYINOPHOSPHOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYINOPHOSPHOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEOXYINOSINE + Pi -> HYPOXANTHINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE EcoCyc reaction equation: DEOXYINOSINE + Pi -> HYPOXANTHINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX). Substrates: Deoxyinosine (molecule.C05512), phosphate (molecule.ecocyc.Pi). Products: Hypoxanthine (molecule.C00262), 2-Deoxy-D-ribose 1-phosphate (molecule.C00672).

## Enriched Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Annotation

DEOXYINOSINE + Pi -> HYPOXANTHINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00672|molecule.C00672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05512|molecule.C05512]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEOXYINOPHOSPHOR-RXN`

## Notes

DEOXYINOSINE + Pi -> HYPOXANTHINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE
