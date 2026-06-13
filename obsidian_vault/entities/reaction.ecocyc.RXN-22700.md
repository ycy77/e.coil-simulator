---
entity_id: "reaction.ecocyc.RXN-22700"
entity_type: "reaction"
name: "RXN-22700"
source_database: "EcoCyc"
source_id: "RXN-22700"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22700

`reaction.ecocyc.RXN-22700`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22700`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + TusA-L-cysteine -> L-ALPHA-ALANINE + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + TusA-L-cysteine -> L-ALPHA-ALANINE + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: L-Cysteine (molecule.C00097), a [TusA]-L-cysteine (molecule.ecocyc.TusA-L-cysteine). Products: L-Alanine (molecule.C00041), a [TusA sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.TusA-Persulfides).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

CYS + TusA-L-cysteine -> L-ALPHA-ALANINE + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TusA-Persulfides|molecule.ecocyc.TusA-Persulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TusA-L-cysteine|molecule.ecocyc.TusA-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22700`

## Notes

CYS + TusA-L-cysteine -> L-ALPHA-ALANINE + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT
