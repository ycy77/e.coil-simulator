---
entity_id: "reaction.ecocyc.INOSINEKIN-RXN"
entity_type: "reaction"
name: "INOSINEKIN-RXN"
source_database: "EcoCyc"
source_id: "INOSINEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# INOSINEKIN-RXN

`reaction.ecocyc.INOSINEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:INOSINEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide metabolism. EcoCyc reaction equation: INOSINE + ATP -> PROTON + IMP + ADP; direction=LEFT-TO-RIGHT. This reaction is part of nucleotide metabolism.

## Biological Role

Catalyzed by inosine/guanosine kinase (complex.ecocyc.CPLX0-322). Substrates: ATP (molecule.C00002), Inosine (molecule.C00294). Products: ADP (molecule.C00008), H+ (molecule.C00080), IMP (molecule.C00130).

## Enriched Pathways

- `ecocyc.PWY-6611` adenine and adenosine salvage V (EcoCyc)

## Annotation

This reaction is part of nucleotide metabolism.

## Pathways

- `ecocyc.PWY-6611` adenine and adenosine salvage V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-322|complex.ecocyc.CPLX0-322]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:INOSINEKIN-RXN`

## Notes

INOSINE + ATP -> PROTON + IMP + ADP; direction=LEFT-TO-RIGHT
