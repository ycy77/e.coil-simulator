---
entity_id: "reaction.R09774"
entity_type: "reaction"
name: "4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:KDO2-lipid IVA 4-amino-4-deoxy-beta-L-arabinopyranosyltransferase"
source_database: "KEGG"
source_id: "R09774"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09774"
---

# 4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:KDO2-lipid IVA 4-amino-4-deoxy-beta-L-arabinopyranosyltransferase

`reaction.R09774`

## Static

- Type: `reaction`
- Source: `KEGG:R09774`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Undecaprenyl phosphate alpha-L-Ara4N + KDO2-lipid IVA alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[4-P-L-Ara4N]-lipid IVA + di-trans,poly-cis-Undecaprenyl phosphate

## Biological Role

Catalyzed by arnT (protein.P76473). Substrates: KDO2-lipid IVA (molecule.C06025), Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556).

## Annotation

Undecaprenyl phosphate alpha-L-Ara4N + KDO2-lipid IVA <=> alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[4-P-L-Ara4N]-lipid IVA + di-trans,poly-cis-Undecaprenyl phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P76473|protein.P76473]] `KEGG` `database` - via EC:2.4.2.43
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `KEGG` `database` - C16157 + C06025 <=> C19883 + C17556
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `KEGG` `database` - C16157 + C06025 <=> C19883 + C17556
- `is_substrate_of` <-- [[molecule.C16157|molecule.C16157]] `KEGG` `database` - C16157 + C06025 <=> C19883 + C17556

## External IDs

- `KEGG:R09774`

## Notes

EQUATION: C16157 + C06025 <=> C19883 + C17556
