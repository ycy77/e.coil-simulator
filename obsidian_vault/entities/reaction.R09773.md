---
entity_id: "reaction.R09773"
entity_type: "reaction"
name: "4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:lipid IVA 4-amino-4-deoxy-beta-L-arabinopyranosyltransferase"
source_database: "KEGG"
source_id: "R09773"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09773"
---

# 4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:lipid IVA 4-amino-4-deoxy-beta-L-arabinopyranosyltransferase

`reaction.R09773`

## Static

- Type: `reaction`
- Source: `KEGG:R09773`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Undecaprenyl phosphate alpha-L-Ara4N + 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate Lipid IIA + di-trans,poly-cis-Undecaprenyl phosphate

## Biological Role

Catalyzed by arnT (protein.P76473). Substrates: 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate (molecule.C04919), Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), Lipid IIA (molecule.C19884).

## Annotation

Undecaprenyl phosphate alpha-L-Ara4N + 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate <=> Lipid IIA + di-trans,poly-cis-Undecaprenyl phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76473|protein.P76473]] `KEGG` `database` - via EC:2.4.2.43
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `KEGG` `database` - C16157 + C04919 <=> C19884 + C17556
- `is_product_of` <-- [[molecule.C19884|molecule.C19884]] `KEGG` `database` - C16157 + C04919 <=> C19884 + C17556
- `is_substrate_of` <-- [[molecule.C04919|molecule.C04919]] `KEGG` `database` - C16157 + C04919 <=> C19884 + C17556
- `is_substrate_of` <-- [[molecule.C16157|molecule.C16157]] `KEGG` `database` - C16157 + C04919 <=> C19884 + C17556

## External IDs

- `KEGG:R09773`

## Notes

EQUATION: C16157 + C04919 <=> C19884 + C17556
