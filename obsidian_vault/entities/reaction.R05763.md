---
entity_id: "reaction.R05763"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:(E)-prop-1-ene-1,2,3-tricarboxylate 2'-O-methyltransferase"
source_database: "KEGG"
source_id: "R05763"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05763"
---

# S-adenosyl-L-methionine:(E)-prop-1-ene-1,2,3-tricarboxylate 2'-O-methyltransferase

`reaction.R05763`

## Static

- Type: `reaction`
- Source: `KEGG:R05763`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + trans-Aconitate S-Adenosyl-L-homocysteine + (E)-3-(Methoxycarbonyl)pent-2-enedioate

## Biological Role

Catalyzed by tam (protein.P76145). Substrates: S-Adenosyl-L-methionine (molecule.C00019), trans-Aconitate (molecule.C02341). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + trans-Aconitate <=> S-Adenosyl-L-homocysteine + (E)-3-(Methoxycarbonyl)pent-2-enedioate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P76145|protein.P76145]] `KEGG` `database` - via EC:2.1.1.144
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C02341 <=> C00021 + C11514
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C02341 <=> C00021 + C11514
- `is_substrate_of` <-- [[molecule.C02341|molecule.C02341]] `KEGG` `database` - C00019 + C02341 <=> C00021 + C11514

## External IDs

- `KEGG:R05763`

## Notes

EQUATION: C00019 + C02341 <=> C00021 + C11514
