---
entity_id: "reaction.R10268"
entity_type: "reaction"
name: "(6S)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide-phosphate hydro-lyase (ADP-hydrolysing; NADPH-forming)"
source_database: "KEGG"
source_id: "R10268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10268"
---

# (6S)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide-phosphate hydro-lyase (ADP-hydrolysing; NADPH-forming)

`reaction.R10268`

## Static

- Type: `reaction`
- Source: `KEGG:R10268`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP + (6S)-6beta-Hydroxy-1,4,5,6-tetrahydronicotinamide-adenine dinucleotide phosphate AMP + Orthophosphate + NADPH

## Biological Role

Catalyzed by nnr (protein.P31806). Substrates: ADP (molecule.C00008). Products: NADPH (molecule.C00005), Orthophosphate (molecule.C00009), AMP (molecule.C00020).

## Annotation

ADP + (6S)-6beta-Hydroxy-1,4,5,6-tetrahydronicotinamide-adenine dinucleotide phosphate <=> AMP + Orthophosphate + NADPH

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31806|protein.P31806]] `KEGG` `database` - via EC:4.2.1.136
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00008 + C04899 <=> C00020 + C00009 + C00005
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00008 + C04899 <=> C00020 + C00009 + C00005
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00008 + C04899 <=> C00020 + C00009 + C00005
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00008 + C04899 <=> C00020 + C00009 + C00005

## External IDs

- `KEGG:R10268`

## Notes

EQUATION: C00008 + C04899 <=> C00020 + C00009 + C00005
