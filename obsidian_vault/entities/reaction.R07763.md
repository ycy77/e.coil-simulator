---
entity_id: "reaction.R07763"
entity_type: "reaction"
name: "R07763"
source_database: "KEGG"
source_id: "R07763"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07763"
---

# R07763

`reaction.R07763`

## Static

- Type: `reaction`
- Source: `KEGG:R07763`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Oxostearoyl-[acp] + NADPH + H+ (3R)-3-Hydroxyoctadecanoyl-[acyl-carrier protein] + NADP+

## Biological Role

Catalyzed by fabG (protein.P0AEK2). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Oxostearoyl-[acp] (molecule.C16219). Products: NADP+ (molecule.C00006), (3R)-3-Hydroxyoctadecanoyl-[acyl-carrier protein] (molecule.C16220).

## Annotation

3-Oxostearoyl-[acp] + NADPH + H+ <=> (3R)-3-Hydroxyoctadecanoyl-[acyl-carrier protein] + NADP+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK2|protein.P0AEK2]] `KEGG` `database` - via EC:1.1.1.100
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C16219 + C00005 + C00080 <=> C16220 + C00006
- `is_product_of` <-- [[molecule.C16220|molecule.C16220]] `KEGG` `database` - C16219 + C00005 + C00080 <=> C16220 + C00006
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C16219 + C00005 + C00080 <=> C16220 + C00006
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C16219 + C00005 + C00080 <=> C16220 + C00006
- `is_substrate_of` <-- [[molecule.C16219|molecule.C16219]] `KEGG` `database` - C16219 + C00005 + C00080 <=> C16220 + C00006

## External IDs

- `KEGG:R07763`

## Notes

EQUATION: C16219 + C00005 + C00080 <=> C16220 + C00006
