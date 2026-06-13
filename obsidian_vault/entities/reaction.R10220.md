---
entity_id: "reaction.R10220"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:7-aminomethyl-7-deazaguanosine ribosyltransferase (ribosyl isomerizing; L-methionine, adenine releasing)"
source_database: "KEGG"
source_id: "R10220"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10220"
---

# S-adenosyl-L-methionine:7-aminomethyl-7-deazaguanosine ribosyltransferase (ribosyl isomerizing; L-methionine, adenine releasing)

`reaction.R10220`

## Static

- Type: `reaction`
- Source: `KEGG:R10220`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + tRNA 7-aminomethyl-7-carbaguanine L-Methionine + Adenine + Epoxyqueuosine in tRNA

## Biological Role

Catalyzed by queA (protein.P0A7F9). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: L-Methionine (molecule.C00073), Adenine (molecule.C00147).

## Annotation

S-Adenosyl-L-methionine + tRNA 7-aminomethyl-7-carbaguanine <=> L-Methionine + Adenine + Epoxyqueuosine in tRNA

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A7F9|protein.P0A7F9]] `KEGG` `database` - via EC:2.4.99.17
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C00019 + C20446 <=> C00073 + C00147 + C19647
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `KEGG` `database` - C00019 + C20446 <=> C00073 + C00147 + C19647
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C20446 <=> C00073 + C00147 + C19647

## External IDs

- `KEGG:R10220`

## Notes

EQUATION: C00019 + C20446 <=> C00073 + C00147 + C19647
