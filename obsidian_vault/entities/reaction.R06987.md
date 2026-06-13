---
entity_id: "reaction.R06987"
entity_type: "reaction"
name: "propanoyl-CoA:formate C-propanoyltransferase"
source_database: "KEGG"
source_id: "R06987"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06987"
---

# propanoyl-CoA:formate C-propanoyltransferase

`reaction.R06987`

## Static

- Type: `reaction`
- Source: `KEGG:R06987`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxobutanoate + CoA Propanoyl-CoA + Formate

## Biological Role

Catalyzed by pflB (protein.P09373), tdcE (protein.P42632). Substrates: CoA (molecule.C00010), 2-Oxobutanoate (molecule.C00109). Products: Formate (molecule.C00058), Propanoyl-CoA (molecule.C00100).

## Annotation

2-Oxobutanoate + CoA <=> Propanoyl-CoA + Formate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P09373|protein.P09373]] `KEGG` `database` - via EC:2.3.1.54
- `catalyzes` <-- [[protein.P42632|protein.P42632]] `KEGG` `database` - via EC:2.3.1.54
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058
- `is_product_of` <-- [[molecule.C00100|molecule.C00100]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058
- `is_substrate_of` <-- [[molecule.C00109|molecule.C00109]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058

## External IDs

- `KEGG:R06987`

## Notes

EQUATION: C00109 + C00010 <=> C00100 + C00058
