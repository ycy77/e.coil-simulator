---
entity_id: "reaction.ecocyc.DEOXYADENPHOSPHOR-RXN"
entity_type: "reaction"
name: "DEOXYADENPHOSPHOR-RXN"
source_database: "EcoCyc"
source_id: "DEOXYADENPHOSPHOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEOXYADENPHOSPHOR-RXN

`reaction.ecocyc.DEOXYADENPHOSPHOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYADENPHOSPHOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEOXYADENOSINE + Pi -> ADENINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE EcoCyc reaction equation: DEOXYADENOSINE + Pi -> ADENINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX). Substrates: Deoxyadenosine (molecule.C00559), phosphate (molecule.ecocyc.Pi). Products: Adenine (molecule.C00147), 2-Deoxy-D-ribose 1-phosphate (molecule.C00672).

## Enriched Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Annotation

DEOXYADENOSINE + Pi -> ADENINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00672|molecule.C00672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEOXYADENPHOSPHOR-RXN`

## Notes

DEOXYADENOSINE + Pi -> ADENINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE
