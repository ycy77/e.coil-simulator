---
entity_id: "reaction.ecocyc.RXN-25085"
entity_type: "reaction"
name: "RXN-25085"
source_database: "EcoCyc"
source_id: "RXN-25085"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25085

`reaction.ecocyc.RXN-25085`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25085`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + IscS-IscU-Fe-Complex -> L-ALPHA-ALANINE + IscS-S-IscU-Fe-Complex; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + IscS-IscU-Fe-Complex -> L-ALPHA-ALANINE + IscS-S-IscU-Fe-Complex; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: L-Cysteine (molecule.C00097). Products: L-Alanine (molecule.C00041).

## Enriched Pathways

- `ecocyc.PWY-8566` [2Fe-2S] iron-sulfur cluster biosynthesis (bacterial IscS system) (EcoCyc)

## Annotation

CYS + IscS-IscU-Fe-Complex -> L-ALPHA-ALANINE + IscS-S-IscU-Fe-Complex; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8566` [2Fe-2S] iron-sulfur cluster biosynthesis (bacterial IscS system) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25085`

## Notes

CYS + IscS-IscU-Fe-Complex -> L-ALPHA-ALANINE + IscS-S-IscU-Fe-Complex; direction=PHYSIOL-LEFT-TO-RIGHT
