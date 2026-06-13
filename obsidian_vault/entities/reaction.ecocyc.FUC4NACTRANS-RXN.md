---
entity_id: "reaction.ecocyc.FUC4NACTRANS-RXN"
entity_type: "reaction"
name: "FUC4NACTRANS-RXN"
source_database: "EcoCyc"
source_id: "FUC4NACTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FUC4NACTRANS-RXN

`reaction.ecocyc.FUC4NACTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FUC4NACTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes lipid III, the third lipid-linked intermediate in enterobacterial common antigen (ECA) biosynthesis. Lipid III is then utilized for synthesis of ECA heteropolysaccharide chains. EcoCyc reaction equation: C55-PP-GLCNAC-MANNACA + TDP-FUC4NAC -> PROTON + C55-PP-GLCNAC-MANNACA-FUC4NAC + TDP; direction=LEFT-TO-RIGHT. This reaction synthesizes lipid III, the third lipid-linked intermediate in enterobacterial common antigen (ECA) biosynthesis. Lipid III is then utilized for synthesis of ECA heteropolysaccharide chains.

## Biological Role

Catalyzed by wecF (protein.P56258). Substrates: dTDP-4-acetamido-4,6-dideoxy-D-glucose (molecule.C06018), β-D-ManNAcA-(1→4)-α-D-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA). Products: H+ (molecule.C00080), dTDP (molecule.C00363), α-D-Fuc4NAc-(1→4)-β-D-ManNAcA-(1→4)-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC).

## Enriched Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Annotation

This reaction synthesizes lipid III, the third lipid-linked intermediate in enterobacterial common antigen (ECA) biosynthesis. Lipid III is then utilized for synthesis of ECA heteropolysaccharide chains.

## Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P56258|protein.P56258]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00363|molecule.C00363]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC|molecule.ecocyc.C55-PP-GLCNAC-MANNACA-FUC4NAC]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06018|molecule.C06018]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA|molecule.ecocyc.C55-PP-GLCNAC-MANNACA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FUC4NACTRANS-RXN`

## Notes

C55-PP-GLCNAC-MANNACA + TDP-FUC4NAC -> PROTON + C55-PP-GLCNAC-MANNACA-FUC4NAC + TDP; direction=LEFT-TO-RIGHT
