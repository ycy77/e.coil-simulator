---
entity_id: "reaction.R11528"
entity_type: "reaction"
name: "L-cysteine:sulfur-acceptor sulfurtransferase"
source_database: "KEGG"
source_id: "R11528"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11528"
---

# L-cysteine:sulfur-acceptor sulfurtransferase

`reaction.R11528`

## Static

- Type: `reaction`
- Source: `KEGG:R11528`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine + [Protein]-L-cysteine L-Alanine + [Protein]-S-sulfanyl-L-cysteine

## Biological Role

Catalyzed by iscS (protein.P0A6B7), sufS (protein.P77444). Substrates: L-Cysteine (molecule.C00097). Products: L-Alanine (molecule.C00041).

## Annotation

L-Cysteine + [Protein]-L-cysteine <=> L-Alanine + [Protein]-S-sulfanyl-L-cysteine

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A6B7|protein.P0A6B7]] `KEGG` `database` - via EC:2.8.1.7
- `catalyzes` <-- [[protein.P77444|protein.P77444]] `KEGG` `database` - via EC:2.8.1.7
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `KEGG` `database` - C00097 + C02743 <=> C00041 + C21440
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `KEGG` `database` - C00097 + C02743 <=> C00041 + C21440

## External IDs

- `KEGG:R11528`

## Notes

EQUATION: C00097 + C02743 <=> C00041 + C21440
