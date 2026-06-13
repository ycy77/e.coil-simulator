---
entity_id: "reaction.R00472"
entity_type: "reaction"
name: "acetyl-CoA:glyoxylate C-acetyltransferase (thioester-hydrolysing, carboxymethyl-forming);"
source_database: "KEGG"
source_id: "R00472"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00472"
---

# acetyl-CoA:glyoxylate C-acetyltransferase (thioester-hydrolysing, carboxymethyl-forming);

`reaction.R00472`

## Static

- Type: `reaction`
- Source: `KEGG:R00472`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Malate + CoA Acetyl-CoA + H2O + Glyoxylate

## Biological Role

Catalyzed by aceB (protein.P08997), glcB (protein.P37330). Substrates: CoA (molecule.C00010), (S)-Malate (molecule.C00149). Products: H2O (molecule.C00001), Acetyl-CoA (molecule.C00024), Glyoxylate (molecule.C00048).

## Annotation

(S)-Malate + CoA <=> Acetyl-CoA + H2O + Glyoxylate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P08997|protein.P08997]] `KEGG` `database` - via EC:2.3.3.9
- `catalyzes` <-- [[protein.P37330|protein.P37330]] `KEGG` `database` - via EC:2.3.3.9
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048

## External IDs

- `KEGG:R00472`

## Notes

EQUATION: C00149 + C00010 <=> C00024 + C00001 + C00048
