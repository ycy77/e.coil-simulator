---
entity_id: "reaction.ecocyc.GLCNACPTRANS-RXN"
entity_type: "reaction"
name: "GLCNACPTRANS-RXN"
source_database: "EcoCyc"
source_id: "GLCNACPTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLCNACPTRANS-RXN

`reaction.ecocyc.GLCNACPTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLCNACPTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes N-acetyl-glucosaminyl-pyrophosphorylundecaprenol (lipid I), the first lipid-linked intermediate in enterobacterial common antigen (ECA) synthesis. EcoCyc reaction equation: CPD-9646 + UDP-N-ACETYL-D-GLUCOSAMINE -> ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + UMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes N-acetyl-glucosaminyl-pyrophosphorylundecaprenol (lipid I), the first lipid-linked intermediate in enterobacterial common antigen (ECA) synthesis.

## Biological Role

Catalyzed by UDP-N-acetylglucosamine—undecaprenyl-phosphate N-acetylglucosaminephosphotransferase (complex.ecocyc.CPLX0-8011). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556). Products: UMP (molecule.C00105), α-D-GlcNAc-PP-Und (molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE).

## Enriched Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Annotation

This reaction synthesizes N-acetyl-glucosaminyl-pyrophosphorylundecaprenol (lipid I), the first lipid-linked intermediate in enterobacterial common antigen (ECA) synthesis.

## Pathways

- `ecocyc.ECASYN-PWY` enterobacterial common antigen biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.ecocyc.CPD0-1088|molecule.ecocyc.CPD0-1088]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8011|complex.ecocyc.CPLX0-8011]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE|molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-5242|molecule.ecocyc.CPD-5242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLCNACPTRANS-RXN`

## Notes

CPD-9646 + UDP-N-ACETYL-D-GLUCOSAMINE -> ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + UMP; direction=PHYSIOL-LEFT-TO-RIGHT
