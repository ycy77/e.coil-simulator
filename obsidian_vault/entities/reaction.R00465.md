---
entity_id: "reaction.R00465"
entity_type: "reaction"
name: "glycolate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R00465"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00465"
---

# glycolate:NADP+ oxidoreductase

`reaction.R00465`

## Static

- Type: `reaction`
- Source: `KEGG:R00465`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycolate + NADP+ Glyoxylate + NADPH + H+

## Biological Role

Catalyzed by ghrB (protein.P37666), ghrA (protein.P75913). Substrates: NADP+ (molecule.C00006), Glycolate (molecule.C00160). Products: NADPH (molecule.C00005), Glyoxylate (molecule.C00048), H+ (molecule.C00080).

## Annotation

Glycolate + NADP+ <=> Glyoxylate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P37666|protein.P37666]] `KEGG` `database` - via EC:1.1.1.79
- `catalyzes` <-- [[protein.P75913|protein.P75913]] `KEGG` `database` - via EC:1.1.1.79
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080

## External IDs

- `KEGG:R00465`

## Notes

EQUATION: C00160 + C00006 <=> C00048 + C00005 + C00080
