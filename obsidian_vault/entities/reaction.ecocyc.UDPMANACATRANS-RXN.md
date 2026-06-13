---
entity_id: "reaction.ecocyc.UDPMANACATRANS-RXN"
entity_type: "reaction"
name: "UDPMANACATRANS-RXN"
source_database: "EcoCyc"
source_id: "UDPMANACATRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPMANACATRANS-RXN

`reaction.ecocyc.UDPMANACATRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPMANACATRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes lipid II, the second lipid-linked intermediate in enterobacterial common antigen (ECA) synthesis. EcoCyc reaction equation: ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + UDP-MANNACA -> PROTON + C55-PP-GLCNAC-MANNACA + UDP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes lipid II, the second lipid-linked intermediate in enterobacterial common antigen (ECA) synthesis.

## Biological Role

Catalyzed by wecG (protein.P27836). Substrates: α-D-GlcNAc-PP-Und (molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE), UDP-N-acetyl-α-D-mannosaminuronate (molecule.ecocyc.UDP-MANNACA). Products: UDP (molecule.C00015), H+ (molecule.C00080), β-D-ManNAcA-(1→4)-α-D-GlcNAc-PP-Und (molecule.ecocyc.C55-PP-GLCNAC-MANNACA).

## Enriched Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Annotation

This reaction synthesizes lipid II, the second lipid-linked intermediate in enterobacterial common antigen (ECA) synthesis.

## Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27836|protein.P27836]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.C55-PP-GLCNAC-MANNACA|molecule.ecocyc.C55-PP-GLCNAC-MANNACA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE|molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.UDP-MANNACA|molecule.ecocyc.UDP-MANNACA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UDPMANACATRANS-RXN`

## Notes

ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + UDP-MANNACA -> PROTON + C55-PP-GLCNAC-MANNACA + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
