---
entity_id: "reaction.ecocyc.FGAMSYN-RXN"
entity_type: "reaction"
name: "FGAMSYN-RXN"
source_database: "EcoCyc"
source_id: "FGAMSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FGAMSYN-RXN

`reaction.ecocyc.FGAMSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FGAMSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in de novo purine biosynthesis EcoCyc reaction equation: ATP + 5-P-RIBOSYL-N-FORMYLGLYCINEAMIDE + GLN + WATER -> PROTON + ADP + Pi + 5-PHOSPHORIBOSYL-N-FORMYLGLYCINEAMIDINE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fourth step in de novo purine biosynthesis

## Biological Role

Catalyzed by purL (protein.P15254). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), 5'-Phosphoribosyl-N-formylglycinamide (molecule.C04376). Products: ADP (molecule.C00008), L-Glutamate (molecule.C00025), H+ (molecule.C00080), 2-(Formamido)-N1-(5'-phosphoribosyl)acetamidine (molecule.C04640), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Annotation

This is the fourth step in de novo purine biosynthesis

## Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)
- `ecocyc.PWY-6122` 5-aminoimidazole ribonucleotide biosynthesis II (EcoCyc)
- `ecocyc.PWY-6277` superpathway of 5-aminoimidazole ribonucleotide biosynthesis (from PRPP) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P15254|protein.P15254]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04640|molecule.C04640]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04376|molecule.C04376]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FGAMSYN-RXN`

## Notes

ATP + 5-P-RIBOSYL-N-FORMYLGLYCINEAMIDE + GLN + WATER -> PROTON + ADP + Pi + 5-PHOSPHORIBOSYL-N-FORMYLGLYCINEAMIDINE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
