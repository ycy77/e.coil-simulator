---
entity_id: "reaction.ecocyc.GLYRIBONUCSYN-RXN"
entity_type: "reaction"
name: "GLYRIBONUCSYN-RXN"
source_database: "EcoCyc"
source_id: "GLYRIBONUCSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYRIBONUCSYN-RXN

`reaction.ecocyc.GLYRIBONUCSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYRIBONUCSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in de novo purine biosynthesis EcoCyc reaction equation: ATP + 5-P-BETA-D-RIBOSYL-AMINE + GLY -> PROTON + ADP + Pi + 5-PHOSPHO-RIBOSYL-GLYCINEAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in de novo purine biosynthesis

## Biological Role

Catalyzed by purD (protein.P15640). Substrates: ATP (molecule.C00002), Glycine (molecule.C00037), 5-Phosphoribosylamine (molecule.C03090). Products: ADP (molecule.C00008), H+ (molecule.C00080), 5'-Phosphoribosylglycinamide (molecule.C03838), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Annotation

This is the second step in de novo purine biosynthesis

## Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P15640|protein.P15640]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03838|molecule.C03838]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03090|molecule.C03090]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00099|molecule.C00099]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03090|molecule.C03090]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1465|molecule.ecocyc.CPD0-1465]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYRIBONUCSYN-RXN`

## Notes

ATP + 5-P-BETA-D-RIBOSYL-AMINE + GLY -> PROTON + ADP + Pi + 5-PHOSPHO-RIBOSYL-GLYCINEAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT
