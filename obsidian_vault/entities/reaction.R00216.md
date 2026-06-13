---
entity_id: "reaction.R00216"
entity_type: "reaction"
name: "(S)-malate:NADP+ oxidoreductase(oxaloacetate-decarboxylating)"
source_database: "KEGG"
source_id: "R00216"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00216"
---

# (S)-malate:NADP+ oxidoreductase(oxaloacetate-decarboxylating)

`reaction.R00216`

## Static

- Type: `reaction`
- Source: `KEGG:R00216`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Malate + NADP+ Pyruvate + CO2 + NADPH + H+

## Biological Role

Catalyzed by maeB (protein.P76558). Substrates: NADP+ (molecule.C00006), (S)-Malate (molecule.C00149). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

(S)-Malate + NADP+ <=> Pyruvate + CO2 + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76558|protein.P76558]] `KEGG` `database` - via EC:1.1.1.40
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080

## External IDs

- `KEGG:R00216`

## Notes

EQUATION: C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
