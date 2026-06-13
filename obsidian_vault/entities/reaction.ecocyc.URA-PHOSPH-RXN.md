---
entity_id: "reaction.ecocyc.URA-PHOSPH-RXN"
entity_type: "reaction"
name: "URA-PHOSPH-RXN"
source_database: "EcoCyc"
source_id: "URA-PHOSPH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URA-PHOSPH-RXN

`reaction.ecocyc.URA-PHOSPH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URA-PHOSPH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEOXYURIDINE + Pi -> DEOXY-D-RIBOSE-1-PHOSPHATE + URACIL; direction=REVERSIBLE EcoCyc reaction equation: DEOXYURIDINE + Pi -> DEOXY-D-RIBOSE-1-PHOSPHATE + URACIL; direction=REVERSIBLE.

## Biological Role

Catalyzed by thymidine phosphorylase / uracil phosphorylase (complex.ecocyc.DEOA-CPLX). Substrates: Deoxyuridine (molecule.C00526), phosphate (molecule.ecocyc.Pi). Products: Uracil (molecule.C00106), 2-Deoxy-D-ribose 1-phosphate (molecule.C00672).

## Enriched Pathways

- `ecocyc.PWY-7181` pyrimidine deoxyribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Annotation

DEOXYURIDINE + Pi -> DEOXY-D-RIBOSE-1-PHOSPHATE + URACIL; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7181` pyrimidine deoxyribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DEOA-CPLX|complex.ecocyc.DEOA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00672|molecule.C00672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:URA-PHOSPH-RXN`

## Notes

DEOXYURIDINE + Pi -> DEOXY-D-RIBOSE-1-PHOSPHATE + URACIL; direction=REVERSIBLE
