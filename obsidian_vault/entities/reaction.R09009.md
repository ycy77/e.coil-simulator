---
entity_id: "reaction.R09009"
entity_type: "reaction"
name: "UDP-L-arabinopyranose furanomutase"
source_database: "KEGG"
source_id: "R09009"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09009"
---

# UDP-L-arabinopyranose furanomutase

`reaction.R09009`

## Static

- Type: `reaction`
- Source: `KEGG:R09009`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-L-arabinose UDP-L-arabinofuranose

## Biological Role

Catalyzed by glf (protein.P37747). Substrates: UDP-L-arabinose (molecule.C00935). Products: UDP-L-arabinofuranose (molecule.C18094).

## Annotation

UDP-L-arabinose <=> UDP-L-arabinofuranose

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37747|protein.P37747]] `KEGG` `database` - via EC:5.4.99.9
- `is_product_of` <-- [[molecule.C18094|molecule.C18094]] `KEGG` `database` - C00935 <=> C18094
- `is_substrate_of` <-- [[molecule.C00935|molecule.C00935]] `KEGG` `database` - C00935 <=> C18094

## External IDs

- `KEGG:R09009`

## Notes

EQUATION: C00935 <=> C18094
