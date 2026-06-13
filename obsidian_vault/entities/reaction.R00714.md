---
entity_id: "reaction.R00714"
entity_type: "reaction"
name: "succinate-semialdehyde:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R00714"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00714"
---

# succinate-semialdehyde:NADP+ oxidoreductase

`reaction.R00714`

## Static

- Type: `reaction`
- Source: `KEGG:R00714`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Succinate semialdehyde + NADP+ + H2O Succinate + NADPH + H+

## Biological Role

Catalyzed by gabD (protein.P25526), sad (protein.P76149). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), Succinate semialdehyde (molecule.C00232). Products: NADPH (molecule.C00005), Succinate (molecule.C00042), H+ (molecule.C00080).

## Annotation

Succinate semialdehyde + NADP+ + H2O <=> Succinate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P25526|protein.P25526]] `KEGG` `database` - via EC:1.2.1.16
- `catalyzes` <-- [[protein.P76149|protein.P76149]] `KEGG` `database` - via EC:1.2.1.16
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00232|molecule.C00232]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080

## External IDs

- `KEGG:R00714`

## Notes

EQUATION: C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
