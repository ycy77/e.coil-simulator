---
entity_id: "reaction.R04710"
entity_type: "reaction"
name: "protein-glycine,dihydroflavodoxin:S-adenosyl-L-methionine oxidoreductase (S-adenosyl-L-methionine cleaving)"
source_database: "KEGG"
source_id: "R04710"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04710"
---

# protein-glycine,dihydroflavodoxin:S-adenosyl-L-methionine oxidoreductase (S-adenosyl-L-methionine cleaving)

`reaction.R04710`

## Static

- Type: `reaction`
- Source: `KEGG:R04710`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + Dihydroflavodoxin + Protein glycine 5'-Deoxyadenosine + L-Methionine + Flavodoxin semiquinone + Protein glycin-2-yl radical

## Biological Role

Catalyzed by pflA (protein.P0A9N4), nrdG (protein.P0A9N8), pflC (protein.P32675), ybiY (protein.P75794). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: L-Methionine (molecule.C00073).

## Annotation

S-Adenosyl-L-methionine + Dihydroflavodoxin + Protein glycine <=> 5'-Deoxyadenosine + L-Methionine + Flavodoxin semiquinone + Protein glycin-2-yl radical

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A9N4|protein.P0A9N4]] `KEGG` `database` - via EC:1.97.1.4
- `catalyzes` <-- [[protein.P0A9N8|protein.P0A9N8]] `KEGG` `database` - via EC:1.97.1.4
- `catalyzes` <-- [[protein.P32675|protein.P32675]] `KEGG` `database` - via EC:1.97.1.4
- `catalyzes` <-- [[protein.P75794|protein.P75794]] `KEGG` `database` - via EC:1.97.1.4
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C00019 + C05196 + C05197 <=> C05198 + C00073 + C05199 + C05312
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C05196 + C05197 <=> C05198 + C00073 + C05199 + C05312

## External IDs

- `KEGG:R04710`

## Notes

EQUATION: C00019 + C05196 + C05197 <=> C05198 + C00073 + C05199 + C05312
