---
entity_id: "reaction.R10244"
entity_type: "reaction"
name: "purine-deoxynucleoside:phosphate ribosyltransferase"
source_database: "KEGG"
source_id: "R10244"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10244"
---

# purine-deoxynucleoside:phosphate ribosyltransferase

`reaction.R10244`

## Static

- Type: `reaction`
- Source: `KEGG:R10244`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Purine deoxyribonucleoside + Orthophosphate Purine + 2-Deoxy-D-ribose 1-phosphate

## Biological Role

Catalyzed by deoD (protein.P0ABP8), ppnP (protein.P0C037), yfiH (protein.P33644), xapA (protein.P45563). Substrates: Orthophosphate (molecule.C00009). Products: 2-Deoxy-D-ribose 1-phosphate (molecule.C00672).

## Annotation

Purine deoxyribonucleoside + Orthophosphate <=> Purine + 2-Deoxy-D-ribose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABP8|protein.P0ABP8]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` <-- [[protein.P0C037|protein.P0C037]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` <-- [[protein.P33644|protein.P33644]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` <-- [[protein.P45563|protein.P45563]] `KEGG` `database` - via EC:2.4.2.1
- `is_product_of` <-- [[molecule.C00672|molecule.C00672]] `KEGG` `database` - C20463 + C00009 <=> C15587 + C00672
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C20463 + C00009 <=> C15587 + C00672

## External IDs

- `KEGG:R10244`

## Notes

EQUATION: C20463 + C00009 <=> C15587 + C00672
