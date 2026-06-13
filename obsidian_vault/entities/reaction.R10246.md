---
entity_id: "reaction.R10246"
entity_type: "reaction"
name: "L-tyrosine 4-methylphenol-lyase (2-iminoacetate-forming)"
source_database: "KEGG"
source_id: "R10246"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10246"
---

# L-tyrosine 4-methylphenol-lyase (2-iminoacetate-forming)

`reaction.R10246`

## Static

- Type: `reaction`
- Source: `KEGG:R10246`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Tyrosine + S-Adenosyl-L-methionine + Reduced acceptor Iminoglycine + 4-Cresol + 5'-Deoxyadenosine + L-Methionine + Acceptor

## Biological Role

Catalyzed by thiH (protein.P30140). Substrates: S-Adenosyl-L-methionine (molecule.C00019), L-Tyrosine (molecule.C00082). Products: L-Methionine (molecule.C00073), 4-Cresol (molecule.C01468), Iminoglycine (molecule.C15809).

## Annotation

L-Tyrosine + S-Adenosyl-L-methionine + Reduced acceptor <=> Iminoglycine + 4-Cresol + 5'-Deoxyadenosine + L-Methionine + Acceptor

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P30140|protein.P30140]] `KEGG` `database` - via EC:4.1.99.19
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_product_of` <-- [[molecule.C01468|molecule.C01468]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_product_of` <-- [[molecule.C15809|molecule.C15809]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028

## External IDs

- `KEGG:R10246`

## Notes

EQUATION: C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
