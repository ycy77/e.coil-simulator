---
entity_id: "reaction.R00749"
entity_type: "reaction"
name: "ethanolamine ammonia-lyase (acetaldehyde-forming)"
source_database: "KEGG"
source_id: "R00749"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00749"
---

# ethanolamine ammonia-lyase (acetaldehyde-forming)

`reaction.R00749`

## Static

- Type: `reaction`
- Source: `KEGG:R00749`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ethanolamine Acetaldehyde + Ammonia

## Biological Role

Catalyzed by eutB (protein.P0AEJ6), eutC (protein.P19636). Substrates: Ethanolamine (molecule.C00189). Products: Ammonia (molecule.C00014), Acetaldehyde (molecule.C00084).

## Annotation

Ethanolamine <=> Acetaldehyde + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEJ6|protein.P0AEJ6]] `KEGG` `database` - via EC:4.3.1.7
- `catalyzes` <-- [[protein.P19636|protein.P19636]] `KEGG` `database` - via EC:4.3.1.7
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00189 <=> C00084 + C00014
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C00189 <=> C00084 + C00014
- `is_substrate_of` <-- [[molecule.C00189|molecule.C00189]] `KEGG` `database` - C00189 <=> C00084 + C00014

## External IDs

- `KEGG:R00749`

## Notes

EQUATION: C00189 <=> C00084 + C00014
