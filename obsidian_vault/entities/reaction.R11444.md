---
entity_id: "reaction.R11444"
entity_type: "reaction"
name: "L-leucyl-tRNA(Leu):[protein] N-terminal L-arginine leucyltransferase"
source_database: "KEGG"
source_id: "R11444"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11444"
---

# L-leucyl-tRNA(Leu):[protein] N-terminal L-arginine leucyltransferase

`reaction.R11444`

## Static

- Type: `reaction`
- Source: `KEGG:R11444`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Leucyl-tRNA + L-Arginyl-protein tRNA(Leu) + L-Leucyl-L-arginyl-protein

## Biological Role

Catalyzed by aat (protein.P0A8P1). Substrates: L-Leucyl-tRNA (molecule.C02047).

## Annotation

L-Leucyl-tRNA + L-Arginyl-protein <=> tRNA(Leu) + L-Leucyl-L-arginyl-protein

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P0A8P1|protein.P0A8P1]] `KEGG` `database` - via EC:2.3.2.6
- `is_substrate_of` <-- [[molecule.C02047|molecule.C02047]] `KEGG` `database` - C02047 + C16739 <=> C01645 + C21386

## External IDs

- `KEGG:R11444`

## Notes

EQUATION: C02047 + C16739 <=> C01645 + C21386
