---
entity_id: "reaction.R10267"
entity_type: "reaction"
name: "(6S)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide hydro-lyase (ADP-hydrolysing; NADH-forming)"
source_database: "KEGG"
source_id: "R10267"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10267"
---

# (6S)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide hydro-lyase (ADP-hydrolysing; NADH-forming)

`reaction.R10267`

## Static

- Type: `reaction`
- Source: `KEGG:R10267`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP + (6S)-6beta-Hydroxy-1,4,5,6-tetrahydronicotinamide-adenine dinucleotide AMP + Orthophosphate + NADH

## Biological Role

Catalyzed by nnr (protein.P31806). Substrates: ADP (molecule.C00008). Products: NADH (molecule.C00004), Orthophosphate (molecule.C00009), AMP (molecule.C00020).

## Annotation

ADP + (6S)-6beta-Hydroxy-1,4,5,6-tetrahydronicotinamide-adenine dinucleotide <=> AMP + Orthophosphate + NADH

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31806|protein.P31806]] `KEGG` `database` - via EC:4.2.1.136
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00008 + C04856 <=> C00020 + C00009 + C00004
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00008 + C04856 <=> C00020 + C00009 + C00004
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00008 + C04856 <=> C00020 + C00009 + C00004
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00008 + C04856 <=> C00020 + C00009 + C00004

## External IDs

- `KEGG:R10267`

## Notes

EQUATION: C00008 + C04856 <=> C00020 + C00009 + C00004
