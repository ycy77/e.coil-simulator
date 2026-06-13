---
entity_id: "reaction.R00125"
entity_type: "reaction"
name: "P1,P4-bis(5'-adenosyl)-tetraphosphate nucleotidebisphosphohydrolase"
source_database: "KEGG"
source_id: "R00125"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00125"
---

# P1,P4-bis(5'-adenosyl)-tetraphosphate nucleotidebisphosphohydrolase

`reaction.R00125`

## Static

- Type: `reaction`
- Source: `KEGG:R00125`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

P1,P4-Bis(5'-adenosyl)tetraphosphate + H2O 2 ADP

## Biological Role

Catalyzed by apaH (protein.P05637). Substrates: H2O (molecule.C00001), P1,P4-Bis(5'-adenosyl)tetraphosphate (molecule.C01260). Products: ADP (molecule.C00008).

## Annotation

P1,P4-Bis(5'-adenosyl)tetraphosphate + H2O <=> 2 ADP

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P05637|protein.P05637]] `KEGG` `database` - via EC:3.6.1.41
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C01260 + C00001 <=> 2 C00008
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01260 + C00001 <=> 2 C00008
- `is_substrate_of` <-- [[molecule.C01260|molecule.C01260]] `KEGG` `database` - C01260 + C00001 <=> 2 C00008

## External IDs

- `KEGG:R00125`

## Notes

EQUATION: C01260 + C00001 <=> 2 C00008
