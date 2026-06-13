---
entity_id: "reaction.ecocyc.DURIDKI-RXN"
entity_type: "reaction"
name: "DURIDKI-RXN"
source_database: "EcoCyc"
source_id: "DURIDKI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DURIDKI-RXN

`reaction.ecocyc.DURIDKI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DURIDKI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. EcoCyc reaction equation: DEOXYURIDINE + ATP -> PROTON + DUMP + ADP; direction=LEFT-TO-RIGHT. This reaction is part of the pyrimidine salvage pathway.

## Biological Role

Catalyzed by thymidine kinase / deoxyuridine kinase (complex.ecocyc.CPLX0-8261). Substrates: ATP (molecule.C00002), Deoxyuridine (molecule.C00526). Products: ADP (molecule.C00008), H+ (molecule.C00080), dUMP (molecule.C00365).

## Enriched Pathways

- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway.

## Pathways

- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8261|complex.ecocyc.CPLX0-8261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00365|molecule.C00365]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DURIDKI-RXN`

## Notes

DEOXYURIDINE + ATP -> PROTON + DUMP + ADP; direction=LEFT-TO-RIGHT
