---
entity_id: "reaction.ecocyc.DGTPTRIPHYDRO-RXN"
entity_type: "reaction"
name: "DGTPTRIPHYDRO-RXN"
source_database: "EcoCyc"
source_id: "DGTPTRIPHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DGTPTRIPHYDRO-RXN

`reaction.ecocyc.DGTPTRIPHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DGTPTRIPHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide hydrolysis. EcoCyc reaction equation: WATER + DGTP -> DEOXYGUANOSINE + P3I; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of nucleotide hydrolysis.

## Biological Role

Catalyzed by dGTP triphosphohydrolase (complex.ecocyc.DGTPTRIPHYDRO-CPLX). Substrates: H2O (molecule.C00001), dGTP (molecule.C00286). Products: Deoxyguanosine (molecule.C00330), Triphosphate (molecule.C00536).

## Annotation

This reaction is part of nucleotide hydrolysis.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.DGTPTRIPHYDRO-CPLX|complex.ecocyc.DGTPTRIPHYDRO-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00330|molecule.C00330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DGTPTRIPHYDRO-RXN`

## Notes

WATER + DGTP -> DEOXYGUANOSINE + P3I; direction=PHYSIOL-LEFT-TO-RIGHT
