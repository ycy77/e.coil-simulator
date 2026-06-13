---
entity_id: "reaction.R00137"
entity_type: "reaction"
name: "ATP:nicotinamide-nucleotide adenylyltransferase"
source_database: "KEGG"
source_id: "R00137"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00137"
---

# ATP:nicotinamide-nucleotide adenylyltransferase

`reaction.R00137`

## Static

- Type: `reaction`
- Source: `KEGG:R00137`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Nicotinamide D-ribonucleotide Diphosphate + NAD+

## Biological Role

Catalyzed by nadD (protein.P0A752), nadR (protein.P27278). Substrates: ATP (molecule.C00002), Nicotinamide D-ribonucleotide (molecule.C00455). Products: NAD+ (molecule.C00003), Diphosphate (molecule.C00013).

## Annotation

ATP + Nicotinamide D-ribonucleotide <=> Diphosphate + NAD+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A752|protein.P0A752]] `KEGG` `database` - via EC:2.7.7.18
- `catalyzes` <-- [[protein.P27278|protein.P27278]] `KEGG` `database` - via EC:2.7.7.1
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00002 + C00455 <=> C00013 + C00003
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00455 <=> C00013 + C00003
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00455 <=> C00013 + C00003
- `is_substrate_of` <-- [[molecule.C00455|molecule.C00455]] `KEGG` `database` - C00002 + C00455 <=> C00013 + C00003

## External IDs

- `KEGG:R00137`

## Notes

EQUATION: C00002 + C00455 <=> C00013 + C00003
