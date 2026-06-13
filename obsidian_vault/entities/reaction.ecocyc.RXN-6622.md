---
entity_id: "reaction.ecocyc.RXN-6622"
entity_type: "reaction"
name: "RXN-6622"
source_database: "EcoCyc"
source_id: "RXN-6622"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-6622

`reaction.ecocyc.RXN-6622`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-6622`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS-GLY + WATER -> CYS + GLY; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS-GLY + WATER -> CYS + GLY; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by peptidase D (complex.ecocyc.CPLX0-3001), aminopeptidase A/I and DNA-binding transcriptional repressor PepA (complex.ecocyc.CPLX0-3061), aminopeptidase B (complex.ecocyc.CPLX0-8122), pepN (protein.P04825). Substrates: H2O (molecule.C00001), Cys-Gly (molecule.C01419). Products: Glycine (molecule.C00037), L-Cysteine (molecule.C00097).

## Annotation

CYS-GLY + WATER -> CYS + GLY; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3001|complex.ecocyc.CPLX0-3001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3061|complex.ecocyc.CPLX0-3061]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8122|complex.ecocyc.CPLX0-8122]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P04825|protein.P04825]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01419|molecule.C01419]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-6622`

## Notes

CYS-GLY + WATER -> CYS + GLY; direction=PHYSIOL-LEFT-TO-RIGHT
