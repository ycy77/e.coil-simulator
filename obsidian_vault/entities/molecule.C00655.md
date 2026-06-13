---
entity_id: "molecule.C00655"
entity_type: "small_molecule"
name: "Xanthosine 5'-phosphate"
source_database: "KEGG"
source_id: "C00655"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Xanthosine 5'-phosphate"
  - "Xanthylic acid"
  - "XMP"
  - "(9-D-Ribosylxanthine)-5'-phosphate"
---

# Xanthosine 5'-phosphate

`molecule.C00655`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00655`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Xanthosine 5'-phosphate; Xanthylic acid; XMP; (9-D-Ribosylxanthine)-5'-phosphate EcoCyc common name: XMP.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Xanthosine 5'-phosphate; Xanthylic acid; XMP; (9-D-Ribosylxanthine)-5'-phosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1603|reaction.ecocyc.RXN0-1603]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02142|reaction.R02142]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119
- `is_substrate_of` --> [[reaction.ecocyc.GMP-SYN-GLUT-RXN|reaction.ecocyc.GMP-SYN-GLUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GMP-SYN-NH3-RXN|reaction.ecocyc.GMP-SYN-NH3-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00655`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
