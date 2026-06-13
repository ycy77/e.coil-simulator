---
entity_id: "reaction.R00203"
entity_type: "reaction"
name: "pyruvaldehyde:NAD+ oxidoreductase;"
source_database: "KEGG"
source_id: "R00203"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00203"
---

# pyruvaldehyde:NAD+ oxidoreductase;

`reaction.R00203`

## Static

- Type: `reaction`
- Source: `KEGG:R00203`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Methylglyoxal + NAD+ + H2O Pyruvate + NADH + H+

## Biological Role

Catalyzed by aldA (protein.P25553). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Methylglyoxal (molecule.C00546). Products: NADH (molecule.C00004), Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

Methylglyoxal + NAD+ + H2O <=> Pyruvate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P25553|protein.P25553]] `KEGG` `database` - via EC:1.2.1.22
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00546|molecule.C00546]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080

## External IDs

- `KEGG:R00203`

## Notes

EQUATION: C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
