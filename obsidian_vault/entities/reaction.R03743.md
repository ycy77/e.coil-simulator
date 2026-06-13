---
entity_id: "reaction.R03743"
entity_type: "reaction"
name: "beta-lactamhydrolase"
source_database: "KEGG"
source_id: "R03743"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03743"
---

# beta-lactamhydrolase

`reaction.R03743`

## Static

- Type: `reaction`
- Source: `KEGG:R03743`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

beta-Lactam + H2O Substituted beta-amino acid

## Biological Role

Catalyzed by ampC (protein.P00811). Substrates: H2O (molecule.C00001).

## Annotation

beta-Lactam + H2O <=> Substituted beta-amino acid

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P00811|protein.P00811]] `KEGG` `database` - via EC:3.5.2.6
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01866 + C00001 <=> C03806

## External IDs

- `KEGG:R03743`

## Notes

EQUATION: C01866 + C00001 <=> C03806
