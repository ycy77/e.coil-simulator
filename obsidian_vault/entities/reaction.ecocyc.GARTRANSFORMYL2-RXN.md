---
entity_id: "reaction.ecocyc.GARTRANSFORMYL2-RXN"
entity_type: "reaction"
name: "GARTRANSFORMYL2-RXN"
source_database: "EcoCyc"
source_id: "GARTRANSFORMYL2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GARTRANSFORMYL2-RXN

`reaction.ecocyc.GARTRANSFORMYL2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GARTRANSFORMYL2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction provides an alternative route to the production of 5'-phosphoribosyl-N-formylglycinamide (FGAR), an intermediate in purine biosynthesis, using formate and ATP instead of formyl folate. EcoCyc reaction equation: 5-PHOSPHO-RIBOSYL-GLYCINEAMIDE + FORMATE + ATP -> PROTON + Pi + 5-P-RIBOSYL-N-FORMYLGLYCINEAMIDE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction provides an alternative route to the production of 5'-phosphoribosyl-N-formylglycinamide (FGAR), an intermediate in purine biosynthesis, using formate and ATP instead of formyl folate.

## Biological Role

Catalyzed by purT (protein.P33221). Substrates: ATP (molecule.C00002), Formate (molecule.C00058), 5'-Phosphoribosylglycinamide (molecule.C03838). Products: ADP (molecule.C00008), H+ (molecule.C00080), 5'-Phosphoribosyl-N-formylglycinamide (molecule.C04376), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Annotation

This reaction provides an alternative route to the production of 5'-phosphoribosyl-N-formylglycinamide (FGAR), an intermediate in purine biosynthesis, using formate and ATP instead of formyl folate.

## Pathways

- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P33221|protein.P33221]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04376|molecule.C04376]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03838|molecule.C03838]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GARTRANSFORMYL2-RXN`

## Notes

5-PHOSPHO-RIBOSYL-GLYCINEAMIDE + FORMATE + ATP -> PROTON + Pi + 5-P-RIBOSYL-N-FORMYLGLYCINEAMIDE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
