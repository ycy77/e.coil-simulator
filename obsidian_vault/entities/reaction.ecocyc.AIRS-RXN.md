---
entity_id: "reaction.ecocyc.AIRS-RXN"
entity_type: "reaction"
name: "AIRS-RXN"
source_database: "EcoCyc"
source_id: "AIRS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AIRS-RXN

`reaction.ecocyc.AIRS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AIRS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step (the imidazole ring closure) in de novo purine biosynthesis EcoCyc reaction equation: ATP + 5-PHOSPHORIBOSYL-N-FORMYLGLYCINEAMIDINE -> PROTON + ADP + Pi + 5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fifth step (the imidazole ring closure) in de novo purine biosynthesis

## Biological Role

Catalyzed by phosphoribosylformylglycinamide cyclo-ligase (complex.ecocyc.AIRS-CPLX). Substrates: ATP (molecule.C00002), 2-(Formamido)-N1-(5'-phosphoribosyl)acetamidine (molecule.C04640). Products: ADP (molecule.C00008), H+ (molecule.C00080), Aminoimidazole ribotide (molecule.C03373), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Annotation

This is the fifth step (the imidazole ring closure) in de novo purine biosynthesis

## Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.AIRS-CPLX|complex.ecocyc.AIRS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03373|molecule.C03373]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04640|molecule.C04640]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03373|molecule.C03373]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AIRS-RXN`

## Notes

ATP + 5-PHOSPHORIBOSYL-N-FORMYLGLYCINEAMIDINE -> PROTON + ADP + Pi + 5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE; direction=PHYSIOL-LEFT-TO-RIGHT
