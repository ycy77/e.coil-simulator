---
entity_id: "reaction.R00139"
entity_type: "reaction"
name: "ATP:2'-deoxy-5-hydroxymethylcytidine-5'-diphosphate phosphotransferase"
source_database: "KEGG"
source_id: "R00139"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00139"
---

# ATP:2'-deoxy-5-hydroxymethylcytidine-5'-diphosphate phosphotransferase

`reaction.R00139`

## Static

- Type: `reaction`
- Source: `KEGG:R00139`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate + ATP 2'-Deoxy-5-hydroxymethylcytidine-5'-triphosphate + ADP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), 2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate (molecule.C11038). Products: ADP (molecule.C00008), 2'-Deoxy-5-hydroxymethylcytidine-5'-triphosphate (molecule.C11039).

## Annotation

2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate + ATP <=> 2'-Deoxy-5-hydroxymethylcytidine-5'-triphosphate + ADP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C11038 + C00002 <=> C11039 + C00008
- `is_product_of` <-- [[molecule.C11039|molecule.C11039]] `KEGG` `database` - C11038 + C00002 <=> C11039 + C00008
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C11038 + C00002 <=> C11039 + C00008
- `is_substrate_of` <-- [[molecule.C11038|molecule.C11038]] `KEGG` `database` - C11038 + C00002 <=> C11039 + C00008

## External IDs

- `KEGG:R00139`

## Notes

EQUATION: C11038 + C00002 <=> C11039 + C00008
