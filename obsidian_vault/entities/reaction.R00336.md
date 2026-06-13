---
entity_id: "reaction.R00336"
entity_type: "reaction"
name: "guanosine-3',5'-bis(diphosphate) 3'-diphosphohydrolase"
source_database: "KEGG"
source_id: "R00336"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00336"
---

# guanosine-3',5'-bis(diphosphate) 3'-diphosphohydrolase

`reaction.R00336`

## Static

- Type: `reaction`
- Source: `KEGG:R00336`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Guanosine 3',5'-bis(diphosphate) + H2O GDP + Diphosphate

## Biological Role

Catalyzed by spoT (protein.P0AG24). Substrates: H2O (molecule.C00001), Guanosine 3',5'-bis(diphosphate) (molecule.C01228). Products: Diphosphate (molecule.C00013), GDP (molecule.C00035).

## Annotation

Guanosine 3',5'-bis(diphosphate) + H2O <=> GDP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AG24|protein.P0AG24]] `KEGG` `database` - via EC:3.1.7.2
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C01228 + C00001 <=> C00035 + C00013
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C01228 + C00001 <=> C00035 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01228 + C00001 <=> C00035 + C00013
- `is_substrate_of` <-- [[molecule.C01228|molecule.C01228]] `KEGG` `database` - C01228 + C00001 <=> C00035 + C00013

## External IDs

- `KEGG:R00336`

## Notes

EQUATION: C01228 + C00001 <=> C00035 + C00013
