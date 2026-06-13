---
entity_id: "reaction.ecocyc.PRPPAMIDOTRANS-RXN"
entity_type: "reaction"
name: "PRPPAMIDOTRANS-RXN"
source_database: "EcoCyc"
source_id: "PRPPAMIDOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PRPPAMIDOTRANS-RXN

`reaction.ecocyc.PRPPAMIDOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRPPAMIDOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in de novo purine biosynthesis. It is an important site for control of purine nucleotide synthesis EcoCyc reaction equation: 5-P-BETA-D-RIBOSYL-AMINE + PPI + GLT -> PRPP + GLN + WATER; direction=RIGHT-TO-LEFT. This is the first step in de novo purine biosynthesis. It is an important site for control of purine nucleotide synthesis

## Biological Role

Catalyzed by amidophosphoribosyltransferase (complex.ecocyc.PRPPAMIDOTRANS-CPLX). Substrates: Diphosphate (molecule.C00013), L-Glutamate (molecule.C00025), 5-Phosphoribosylamine (molecule.C03090). Products: H2O (molecule.C00001), L-Glutamine (molecule.C00064), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119).

## Enriched Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Annotation

This is the first step in de novo purine biosynthesis. It is an important site for control of purine nucleotide synthesis

## Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `catalyzes` <-- [[complex.ecocyc.PRPPAMIDOTRANS-CPLX|complex.ecocyc.PRPPAMIDOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03090|molecule.C03090]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7388|molecule.ecocyc.CPD-7388]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1224|molecule.ecocyc.CPD0-1224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1627|molecule.ecocyc.CPD0-1627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2690|molecule.ecocyc.CPD0-2690]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2692|molecule.ecocyc.CPD0-2692]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PRPPAMIDOTRANS-RXN`

## Notes

5-P-BETA-D-RIBOSYL-AMINE + PPI + GLT -> PRPP + GLN + WATER; direction=RIGHT-TO-LEFT
