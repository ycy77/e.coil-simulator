---
entity_id: "reaction.ecocyc.THYM-PHOSPH-RXN"
entity_type: "reaction"
name: "THYM-PHOSPH-RXN"
source_database: "EcoCyc"
source_id: "THYM-PHOSPH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THYM-PHOSPH-RXN

`reaction.ecocyc.THYM-PHOSPH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THYM-PHOSPH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. EcoCyc reaction equation: THYMIDINE + Pi -> DEOXY-D-RIBOSE-1-PHOSPHATE + THYMINE; direction=REVERSIBLE. This reaction is part of the pyrimidine salvage pathway.

## Biological Role

Catalyzed by nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619), thymidine phosphorylase / uracil phosphorylase (complex.ecocyc.DEOA-CPLX). Substrates: Thymidine (molecule.C00214), phosphate (molecule.ecocyc.Pi). Products: Thymine (molecule.C00178), 2-Deoxy-D-ribose 1-phosphate (molecule.C00672).

## Enriched Pathways

- `ecocyc.PWY-7181` pyrimidine deoxyribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway.

## Pathways

- `ecocyc.PWY-7181` pyrimidine deoxyribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.DEOA-CPLX|complex.ecocyc.DEOA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00672|molecule.C00672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DEOXY-RIBOSE-1P|molecule.ecocyc.DEOXY-RIBOSE-1P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THYM-PHOSPH-RXN`

## Notes

THYMIDINE + Pi -> DEOXY-D-RIBOSE-1-PHOSPHATE + THYMINE; direction=REVERSIBLE
