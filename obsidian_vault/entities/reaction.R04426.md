---
entity_id: "reaction.R04426"
entity_type: "reaction"
name: "(2R,3S)-3-isopropylmalate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R04426"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04426"
---

# (2R,3S)-3-isopropylmalate:NAD+ oxidoreductase

`reaction.R04426`

## Static

- Type: `reaction`
- Source: `KEGG:R04426`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(2R,3S)-3-Isopropylmalate + NAD+ (2S)-2-Isopropyl-3-oxosuccinate + NADH + H+

## Biological Role

Catalyzed by leuB (protein.P30125). Substrates: NAD+ (molecule.C00003), (2R,3S)-3-Isopropylmalate (molecule.C04411). Products: NADH (molecule.C00004), H+ (molecule.C00080), (2S)-2-Isopropyl-3-oxosuccinate (molecule.C04236).

## Annotation

(2R,3S)-3-Isopropylmalate + NAD+ <=> (2S)-2-Isopropyl-3-oxosuccinate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P30125|protein.P30125]] `KEGG` `database` - via EC:1.1.1.85
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_product_of` <-- [[molecule.C04236|molecule.C04236]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C04411|molecule.C04411]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080

## External IDs

- `KEGG:R04426`

## Notes

EQUATION: C04411 + C00003 <=> C04236 + C00004 + C00080
