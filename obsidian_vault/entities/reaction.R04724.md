---
entity_id: "reaction.R04724"
entity_type: "reaction"
name: "dodecanoyl-[acp]:NAD+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04724"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04724"
---

# dodecanoyl-[acp]:NAD+ trans-2-oxidoreductase

`reaction.R04724`

## Static

- Type: `reaction`
- Source: `KEGG:R04724`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-[acyl-carrier protein] + NAD+ trans-Dodec-2-enoyl-[acp] + NADH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NAD+ (molecule.C00003), Dodecanoyl-[acyl-carrier protein] (molecule.C05223). Products: NADH (molecule.C00004), H+ (molecule.C00080), trans-Dodec-2-enoyl-[acp] (molecule.C05758).

## Annotation

Dodecanoyl-[acyl-carrier protein] + NAD+ <=> trans-Dodec-2-enoyl-[acp] + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.9
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_product_of` <-- [[molecule.C05758|molecule.C05758]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C05223|molecule.C05223]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080

## External IDs

- `KEGG:R04724`

## Notes

EQUATION: C05223 + C00003 <=> C05758 + C00004 + C00080
