---
entity_id: "reaction.R12067"
entity_type: "reaction"
name: "5-methoxy-2-methyl-3-(all-trans-polyprenyl)benzene-1,4-diol,acceptor:oxygen oxidoreductase (5-hydroxylating)"
source_database: "KEGG"
source_id: "R12067"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12067"
---

# 5-methoxy-2-methyl-3-(all-trans-polyprenyl)benzene-1,4-diol,acceptor:oxygen oxidoreductase (5-hydroxylating)

`reaction.R12067`

## Static

- Type: `reaction`
- Source: `KEGG:R12067`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Methoxy-2-methyl-3-(all-trans-polyprenyl)benzene-1,4-diol + Reduced acceptor + Oxygen 3-Demethylubiquinol + Acceptor + H2O

## Biological Role

Catalyzed by ubiF (protein.P75728). Substrates: Oxygen (molecule.C00007), 5-Methoxy-2-methyl-3-(all-trans-polyprenyl)benzene-1,4-diol (molecule.C19859). Products: H2O (molecule.C00001), 3-Demethylubiquinol (molecule.C21860).

## Annotation

5-Methoxy-2-methyl-3-(all-trans-polyprenyl)benzene-1,4-diol + Reduced acceptor + Oxygen <=> 3-Demethylubiquinol + Acceptor + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75728|protein.P75728]] `KEGG` `database` - via EC:1.14.99.60
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C19859 + C00030 + C00007 <=> C21860 + C00028 + C00001
- `is_product_of` <-- [[molecule.C21860|molecule.C21860]] `KEGG` `database` - C19859 + C00030 + C00007 <=> C21860 + C00028 + C00001
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C19859 + C00030 + C00007 <=> C21860 + C00028 + C00001
- `is_substrate_of` <-- [[molecule.C19859|molecule.C19859]] `KEGG` `database` - C19859 + C00030 + C00007 <=> C21860 + C00028 + C00001

## External IDs

- `KEGG:R12067`

## Notes

EQUATION: C19859 + C00030 + C00007 <=> C21860 + C00028 + C00001
