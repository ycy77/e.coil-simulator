---
entity_id: "molecule.C01250"
entity_type: "small_molecule"
name: "N-Acetyl-L-glutamate 5-semialdehyde"
source_database: "KEGG"
source_id: "C01250"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-L-glutamate 5-semialdehyde"
  - "2-Acetamido-5-oxopentanoate"
---

# N-Acetyl-L-glutamate 5-semialdehyde

`molecule.C01250`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01250`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-L-glutamate 5-semialdehyde; 2-Acetamido-5-oxopentanoate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)

## Annotation

KEGG compound: N-Acetyl-L-glutamate 5-semialdehyde; 2-Acetamido-5-oxopentanoate

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03443|reaction.R03443]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN|reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01250`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
