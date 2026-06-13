---
entity_id: "reaction.ecocyc.3.4.17.8-RXN"
entity_type: "reaction"
name: "3.4.17.8-RXN"
source_database: "EcoCyc"
source_id: "3.4.17.8-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.17.8-RXN

`reaction.ecocyc.3.4.17.8-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.17.8-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

C1 + WATER -> UDP-MURNAC-TETRAPEPTIDE + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: C1 + WATER -> UDP-MURNAC-TETRAPEPTIDE + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-alanyl-D-alanine carboxypeptidase DacA (complex.ecocyc.CPLX0-8252), D-alanyl-D-alanine carboxypeptidase DacC (complex.ecocyc.CPLX0-8254). Substrates: H2O (molecule.C00001), UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-6-carboxy-L-lysyl-D-alanyl-D-alanine (molecule.C04882). Products: D-Alanine (molecule.C00133), UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala (molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE).

## Annotation

C1 + WATER -> UDP-MURNAC-TETRAPEPTIDE + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8252|complex.ecocyc.CPLX0-8252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8254|complex.ecocyc.CPLX0-8254]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE|molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04882|molecule.C04882]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.6-AMINOPENICILLANATE|molecule.ecocyc.6-AMINOPENICILLANATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CEPHALOSPORIN-C|molecule.ecocyc.CEPHALOSPORIN-C]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9195|molecule.ecocyc.CPD-9195]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PENICILLIN-G|molecule.ecocyc.PENICILLIN-G]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.4.17.8-RXN`

## Notes

C1 + WATER -> UDP-MURNAC-TETRAPEPTIDE + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
