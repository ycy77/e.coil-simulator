---
entity_id: "reaction.ecocyc.TRANS-RXN0-279"
entity_type: "reaction"
name: "TRANS-RXN0-279"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-279"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-279

`reaction.ecocyc.TRANS-RXN0-279`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-279`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON -> C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON -> C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wzxE (protein.P0AAA7). Substrates: H+ (molecule.C00080), α-D-Fuc4NAc-(1→4)-β-D-ManNAcA-(1→4)-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC). Products: H+ (molecule.C00080), α-D-Fuc4NAc-(1→4)-β-D-ManNAcA-(1→4)-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC).

## Enriched Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Annotation

C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON -> C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAA7|protein.P0AAA7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC|molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC|molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-279`

## Notes

C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON -> C55-PP-GLCNAC-MANNACA-FUC4NAC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
