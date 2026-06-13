---
entity_id: "reaction.R04159"
entity_type: "reaction"
name: "(5-L-glutamyl)-peptide:amino-acid 5-glutamyltransferase"
source_database: "KEGG"
source_id: "R04159"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04159"
---

# (5-L-glutamyl)-peptide:amino-acid 5-glutamyltransferase

`reaction.R04159`

## Static

- Type: `reaction`
- Source: `KEGG:R04159`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(5-L-Glutamyl)-peptide + Amino acid Peptide + 5-L-Glutamyl amino acid

## Biological Role

Catalyzed by ggt (protein.P18956). Products: Peptide (molecule.C00012).

## Annotation

(5-L-Glutamyl)-peptide + Amino acid <=> Peptide + 5-L-Glutamyl amino acid

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P18956|protein.P18956]] `KEGG` `database` - via EC:2.3.2.2
- `is_product_of` <-- [[molecule.C00012|molecule.C00012]] `KEGG` `database` - C03193 + C00045 <=> C00012 + C03363

## External IDs

- `KEGG:R04159`

## Notes

EQUATION: C03193 + C00045 <=> C00012 + C03363
