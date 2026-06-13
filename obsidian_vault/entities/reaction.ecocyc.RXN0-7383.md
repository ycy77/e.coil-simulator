---
entity_id: "reaction.ecocyc.RXN0-7383"
entity_type: "reaction"
name: "RXN0-7383"
source_database: "EcoCyc"
source_id: "RXN0-7383"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7383

`reaction.ecocyc.RXN0-7383`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7383`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction represents Wzy-dependent block-wise polymerization of enterobacterial common antigen (ECA). The mechanism of Wzy-mediated chain elongation remains poorly understood. Two alternative models predominate (see and references within). EcoCyc reaction equation: CPD-24126 + C55-PP-GLCNAC-MANNACA-FUC4NAC -> CPD-24126 + UNDECAPRENYL-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents Wzy-dependent block-wise polymerization of enterobacterial common antigen (ECA). The mechanism of Wzy-mediated chain elongation remains poorly understood. Two alternative models predominate (see and references within).

## Biological Role

Catalyzed by wzyE (protein.P27835). Substrates: α-D-Fuc4NAc-(1→4)-β-D-ManNAcA-(1→4)-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC), enterobacterial common antigen (molecule.ecocyc.CPD-24126). Products: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), enterobacterial common antigen (molecule.ecocyc.CPD-24126).

## Annotation

This reaction represents Wzy-dependent block-wise polymerization of enterobacterial common antigen (ECA). The mechanism of Wzy-mediated chain elongation remains poorly understood. Two alternative models predominate (see and references within).

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27835|protein.P27835]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24126|molecule.ecocyc.CPD-24126]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC|molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24126|molecule.ecocyc.CPD-24126]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7383`

## Notes

CPD-24126 + C55-PP-GLCNAC-MANNACA-FUC4NAC -> CPD-24126 + UNDECAPRENYL-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
