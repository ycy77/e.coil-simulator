---
entity_id: "reaction.ecocyc.RXN-22149"
entity_type: "reaction"
name: "RXN-22149"
source_database: "EcoCyc"
source_id: "RXN-22149"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22149

`reaction.ecocyc.RXN-22149`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22149`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

C55-PP-GLCNAC-MANNACA-FUC4NAC -> CPD-24126 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: C55-PP-GLCNAC-MANNACA-FUC4NAC -> CPD-24126 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wzyE (protein.P27835). Substrates: α-D-Fuc4NAc-(1→4)-β-D-ManNAcA-(1→4)-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC). Products: H+ (molecule.C00080), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), enterobacterial common antigen (molecule.ecocyc.CPD-24126).

## Enriched Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Annotation

C55-PP-GLCNAC-MANNACA-FUC4NAC -> CPD-24126 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27835|protein.P27835]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24126|molecule.ecocyc.CPD-24126]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC|molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22149`

## Notes

C55-PP-GLCNAC-MANNACA-FUC4NAC -> CPD-24126 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
