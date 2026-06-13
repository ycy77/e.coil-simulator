---
entity_id: "reaction.R11372"
entity_type: "reaction"
name: "(8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate lyase (cyclic pyranopterin phosphate-forming)"
source_database: "KEGG"
source_id: "R11372"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11372"
---

# (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate lyase (cyclic pyranopterin phosphate-forming)

`reaction.R11372`

## Static

- Type: `reaction`
- Source: `KEGG:R11372`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate + H2O Precursor Z + Diphosphate

## Biological Role

Catalyzed by moaC (protein.P0A738). Substrates: H2O (molecule.C00001), (8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate (molecule.C21310). Products: Diphosphate (molecule.C00013), Precursor Z (molecule.C18239).

## Annotation

(8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate + H2O <=> Precursor Z + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A738|protein.P0A738]] `KEGG` `database` - via EC:4.6.1.17
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C21310 + C00001 <=> C18239 + C00013
- `is_product_of` <-- [[molecule.C18239|molecule.C18239]] `KEGG` `database` - C21310 + C00001 <=> C18239 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C21310 + C00001 <=> C18239 + C00013
- `is_substrate_of` <-- [[molecule.C21310|molecule.C21310]] `KEGG` `database` - C21310 + C00001 <=> C18239 + C00013

## External IDs

- `KEGG:R11372`

## Notes

EQUATION: C21310 + C00001 <=> C18239 + C00013
