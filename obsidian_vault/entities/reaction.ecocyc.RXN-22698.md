---
entity_id: "reaction.ecocyc.RXN-22698"
entity_type: "reaction"
name: "RXN-22698"
source_database: "EcoCyc"
source_id: "RXN-22698"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22698

`reaction.ecocyc.RXN-22698`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22698`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + MOCS3-Cysteine -> L-ALPHA-ALANINE + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + MOCS3-Cysteine -> L-ALPHA-ALANINE + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: L-Cysteine (molecule.C00097), a [molybdopterin synthase sulfurtransferase]-L-cysteine (molecule.ecocyc.MOCS3-Cysteine). Products: L-Alanine (molecule.C00041), a [molybdopterin synthase sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.MOCS3-Cysteine-Persulfide).

## Enriched Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Annotation

CYS + MOCS3-Cysteine -> L-ALPHA-ALANINE + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MOCS3-Cysteine-Persulfide|molecule.ecocyc.MOCS3-Cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MOCS3-Cysteine|molecule.ecocyc.MOCS3-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22698`

## Notes

CYS + MOCS3-Cysteine -> L-ALPHA-ALANINE + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
