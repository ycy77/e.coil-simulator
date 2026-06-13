---
entity_id: "reaction.R04405"
entity_type: "reaction"
name: "5-methyltetrahydropteroyltri-L-glutamate:L-homocysteine S-methyltransferase"
source_database: "KEGG"
source_id: "R04405"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04405"
---

# 5-methyltetrahydropteroyltri-L-glutamate:L-homocysteine S-methyltransferase

`reaction.R04405`

## Static

- Type: `reaction`
- Source: `KEGG:R04405`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Methyltetrahydropteroyltri-L-glutamate + L-Homocysteine Tetrahydropteroyltri-L-glutamate + L-Methionine

## Biological Role

Catalyzed by metE (protein.P25665). Substrates: L-Homocysteine (molecule.C00155). Products: L-Methionine (molecule.C00073).

## Annotation

5-Methyltetrahydropteroyltri-L-glutamate + L-Homocysteine <=> Tetrahydropteroyltri-L-glutamate + L-Methionine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P25665|protein.P25665]] `KEGG` `database` - via EC:2.1.1.14
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C04489 + C00155 <=> C04144 + C00073
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `KEGG` `database` - C04489 + C00155 <=> C04144 + C00073

## External IDs

- `KEGG:R04405`

## Notes

EQUATION: C04489 + C00155 <=> C04144 + C00073
