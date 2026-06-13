---
entity_id: "reaction.R04965"
entity_type: "reaction"
name: "(3R)-3-hydroxydodecanoyl-[acyl-carrier-protein] hydro-lyase"
source_database: "KEGG"
source_id: "R04965"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04965"
---

# (3R)-3-hydroxydodecanoyl-[acyl-carrier-protein] hydro-lyase

`reaction.R04965`

## Static

- Type: `reaction`
- Source: `KEGG:R04965`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(3R)-3-Hydroxydodecanoyl-[acyl-carrier protein] trans-Dodec-2-enoyl-[acp] + H2O

## Biological Role

Catalyzed by fabA (protein.P0A6Q3), fabZ (protein.P0A6Q6). Substrates: (3R)-3-Hydroxydodecanoyl-[acyl-carrier protein] (molecule.C05757). Products: H2O (molecule.C00001), trans-Dodec-2-enoyl-[acp] (molecule.C05758).

## Annotation

(3R)-3-Hydroxydodecanoyl-[acyl-carrier protein] <=> trans-Dodec-2-enoyl-[acp] + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6Q3|protein.P0A6Q3]] `KEGG` `database` - via EC:4.2.1.59
- `catalyzes` <-- [[protein.P0A6Q6|protein.P0A6Q6]] `KEGG` `database` - via EC:4.2.1.59
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05757 <=> C05758 + C00001
- `is_product_of` <-- [[molecule.C05758|molecule.C05758]] `KEGG` `database` - C05757 <=> C05758 + C00001
- `is_substrate_of` <-- [[molecule.C05757|molecule.C05757]] `KEGG` `database` - C05757 <=> C05758 + C00001

## External IDs

- `KEGG:R04965`

## Notes

EQUATION: C05757 <=> C05758 + C00001
