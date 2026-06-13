---
entity_id: "reaction.ecocyc.RXN-9789"
entity_type: "reaction"
name: "RXN-9789"
source_database: "EcoCyc"
source_id: "RXN-9789"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9789

`reaction.ecocyc.RXN-9789`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9789`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Thi-S + ATP + PROTON -> Adenylated-ThiS-Proteins + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Thi-S + ATP + PROTON -> Adenylated-ThiS-Proteins + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sulfur carrier protein ThiS adenylyltransferase (complex.ecocyc.CPLX0-8558). Substrates: ATP (molecule.C00002), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013).

## Enriched Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)

## Annotation

Thi-S + ATP + PROTON -> Adenylated-ThiS-Proteins + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8558|complex.ecocyc.CPLX0-8558]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9789`

## Notes

Thi-S + ATP + PROTON -> Adenylated-ThiS-Proteins + PPI; direction=LEFT-TO-RIGHT
