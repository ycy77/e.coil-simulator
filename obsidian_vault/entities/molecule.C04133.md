---
entity_id: "molecule.C04133"
entity_type: "small_molecule"
name: "N-Acetyl-L-glutamate 5-phosphate"
source_database: "KEGG"
source_id: "C04133"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-L-glutamate 5-phosphate"
  - "N-Acetyl-L-glutamyl 5-phosphate"
---

# N-Acetyl-L-glutamate 5-phosphate

`molecule.C04133`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04133`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-L-glutamate 5-phosphate; N-Acetyl-L-glutamyl 5-phosphate EcoCyc common name: N-acetylglutamyl-phosphate.

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)

## Annotation

KEGG compound: N-Acetyl-L-glutamate 5-phosphate; N-Acetyl-L-glutamyl 5-phosphate

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R03443|reaction.R03443]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.ACETYLGLUTKIN-RXN|reaction.ecocyc.ACETYLGLUTKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN|reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04133`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
