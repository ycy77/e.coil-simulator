---
entity_id: "reaction.R07765"
entity_type: "reaction"
name: "octadecanoyl-[acp]:NAD+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R07765"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07765"
---

# octadecanoyl-[acp]:NAD+ trans-2-oxidoreductase

`reaction.R07765`

## Static

- Type: `reaction`
- Source: `KEGG:R07765`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(2E)-Octadecenoyl-[acp] + NADH + H+ Octadecanoyl-[acyl-carrier protein] + NAD+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), (2E)-Octadecenoyl-[acp] (molecule.C16221). Products: NAD+ (molecule.C00003), Octadecanoyl-[acyl-carrier protein] (molecule.C04088).

## Annotation

(2E)-Octadecenoyl-[acp] + NADH + H+ <=> Octadecanoyl-[acyl-carrier protein] + NAD+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.9
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C16221 + C00004 + C00080 <=> C04088 + C00003
- `is_product_of` <-- [[molecule.C04088|molecule.C04088]] `KEGG` `database` - C16221 + C00004 + C00080 <=> C04088 + C00003
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C16221 + C00004 + C00080 <=> C04088 + C00003
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C16221 + C00004 + C00080 <=> C04088 + C00003
- `is_substrate_of` <-- [[molecule.C16221|molecule.C16221]] `KEGG` `database` - C16221 + C00004 + C00080 <=> C04088 + C00003

## External IDs

- `KEGG:R07765`

## Notes

EQUATION: C16221 + C00004 + C00080 <=> C04088 + C00003
