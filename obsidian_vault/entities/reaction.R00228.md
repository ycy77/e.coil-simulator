---
entity_id: "reaction.R00228"
entity_type: "reaction"
name: "acetaldehyde:NAD+ oxidoreductase (CoA-acetylating)"
source_database: "KEGG"
source_id: "R00228"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00228"
---

# acetaldehyde:NAD+ oxidoreductase (CoA-acetylating)

`reaction.R00228`

## Static

- Type: `reaction`
- Source: `KEGG:R00228`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetaldehyde + CoA + NAD+ Acetyl-CoA + NADH + H+

## Biological Role

Catalyzed by adhE (protein.P0A9Q7), mhpF (protein.P77580). Substrates: NAD+ (molecule.C00003), CoA (molecule.C00010), Acetaldehyde (molecule.C00084). Products: NADH (molecule.C00004), Acetyl-CoA (molecule.C00024), H+ (molecule.C00080).

## Annotation

Acetaldehyde + CoA + NAD+ <=> Acetyl-CoA + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `KEGG` `database` - via EC:1.2.1.10
- `catalyzes` <-- [[protein.P77580|protein.P77580]] `KEGG` `database` - via EC:1.2.1.10
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080

## External IDs

- `KEGG:R00228`

## Notes

EQUATION: C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
