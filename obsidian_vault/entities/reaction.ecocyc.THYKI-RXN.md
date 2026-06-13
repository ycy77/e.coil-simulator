---
entity_id: "reaction.ecocyc.THYKI-RXN"
entity_type: "reaction"
name: "THYKI-RXN"
source_database: "EcoCyc"
source_id: "THYKI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THYKI-RXN

`reaction.ecocyc.THYKI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THYKI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. EcoCyc reaction equation: THYMIDINE + ATP -> PROTON + TMP + ADP; direction=LEFT-TO-RIGHT. This reaction is part of the pyrimidine salvage pathway.

## Biological Role

Catalyzed by thymidine kinase / deoxyuridine kinase (complex.ecocyc.CPLX0-8261). Substrates: ATP (molecule.C00002), Thymidine (molecule.C00214). Products: ADP (molecule.C00008), H+ (molecule.C00080), dTMP (molecule.C00364).

## Enriched Pathways

- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway.

## Pathways

- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (20)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00206|molecule.C00206]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00361|molecule.C00361]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00705|molecule.C00705]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C11038|molecule.C11038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C11039|molecule.C11039]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1343|molecule.ecocyc.CPD0-1343]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1344|molecule.ecocyc.CPD0-1344]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8261|complex.ecocyc.CPLX0-8261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00364|molecule.C00364]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THYKI-RXN`

## Notes

THYMIDINE + ATP -> PROTON + TMP + ADP; direction=LEFT-TO-RIGHT
