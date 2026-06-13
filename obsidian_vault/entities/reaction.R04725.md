---
entity_id: "reaction.R04725"
entity_type: "reaction"
name: "dodecanoyl-[acp]:NADP+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04725"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04725"
---

# dodecanoyl-[acp]:NADP+ trans-2-oxidoreductase

`reaction.R04725`

## Static

- Type: `reaction`
- Source: `KEGG:R04725`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-[acyl-carrier protein] + NADP+ trans-Dodec-2-enoyl-[acp] + NADPH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NADP+ (molecule.C00006), Dodecanoyl-[acyl-carrier protein] (molecule.C05223). Products: NADPH (molecule.C00005), H+ (molecule.C00080), trans-Dodec-2-enoyl-[acp] (molecule.C05758).

## Annotation

Dodecanoyl-[acyl-carrier protein] + NADP+ <=> trans-Dodec-2-enoyl-[acp] + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.10
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_product_of` <-- [[molecule.C05758|molecule.C05758]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C05223|molecule.C05223]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080

## External IDs

- `KEGG:R04725`

## Notes

EQUATION: C05223 + C00006 <=> C05758 + C00005 + C00080
