---
entity_id: "reaction.R03443"
entity_type: "reaction"
name: "N-acetyl-L-glutamate-5-semialdehyde:NADP+ 5-oxidoreductase (phosphrylating)"
source_database: "KEGG"
source_id: "R03443"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03443"
---

# N-acetyl-L-glutamate-5-semialdehyde:NADP+ 5-oxidoreductase (phosphrylating)

`reaction.R03443`

## Static

- Type: `reaction`
- Source: `KEGG:R03443`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Acetyl-L-glutamate 5-semialdehyde + Orthophosphate + NADP+ N-Acetyl-L-glutamate 5-phosphate + NADPH + H+

## Biological Role

Catalyzed by argC (protein.P11446). Substrates: NADP+ (molecule.C00006), Orthophosphate (molecule.C00009), N-Acetyl-L-glutamate 5-semialdehyde (molecule.C01250). Products: NADPH (molecule.C00005), H+ (molecule.C00080), N-Acetyl-L-glutamate 5-phosphate (molecule.C04133).

## Annotation

N-Acetyl-L-glutamate 5-semialdehyde + Orthophosphate + NADP+ <=> N-Acetyl-L-glutamate 5-phosphate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P11446|protein.P11446]] `KEGG` `database` - via EC:1.2.1.38
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_product_of` <-- [[molecule.C04133|molecule.C04133]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C01250|molecule.C01250]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080

## External IDs

- `KEGG:R03443`

## Notes

EQUATION: C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
