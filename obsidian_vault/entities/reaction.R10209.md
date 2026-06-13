---
entity_id: "reaction.R10209"
entity_type: "reaction"
name: "tRNA-guanosine34:7-aminomethyl-7-carbaguanine tRNA-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R10209"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10209"
---

# tRNA-guanosine34:7-aminomethyl-7-carbaguanine tRNA-D-ribosyltransferase

`reaction.R10209`

## Static

- Type: `reaction`
- Source: `KEGG:R10209`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA guanine + 7-Aminomethyl-7-carbaguanine tRNA 7-aminomethyl-7-carbaguanine + Guanine

## Biological Role

Catalyzed by tgt (protein.P0A847). Substrates: 7-Aminomethyl-7-carbaguanine (molecule.C16675). Products: Guanine (molecule.C00242).

## Annotation

tRNA guanine + 7-Aminomethyl-7-carbaguanine <=> tRNA 7-aminomethyl-7-carbaguanine + Guanine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A847|protein.P0A847]] `KEGG` `database` - via EC:2.4.2.29
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `KEGG` `database` - C01977 + C16675 <=> C20446 + C00242
- `is_substrate_of` <-- [[molecule.C16675|molecule.C16675]] `KEGG` `database` - C01977 + C16675 <=> C20446 + C00242

## External IDs

- `KEGG:R10209`

## Notes

EQUATION: C01977 + C16675 <=> C20446 + C00242
