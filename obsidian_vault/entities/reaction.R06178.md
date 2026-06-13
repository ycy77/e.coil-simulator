---
entity_id: "reaction.R06178"
entity_type: "reaction"
name: "[poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase"
source_database: "KEGG"
source_id: "R06178"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06178"
---

# [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase

`reaction.R06178`

## Static

- Type: `reaction`
- Source: `KEGG:R06178`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-gamma-D-glutamyl-L-lysyl-D-alanyl-D-alanine + [GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-g-D-Glu-L-Lys-D-Ala-D-Ala)]n-diphosphoundecaprenol di-trans,poly-cis-Undecaprenyl diphosphate + [GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-g-D-Glu-L-Lys-D-Ala-D-Ala)]n-diphosphoundecaprenol

## Biological Role

Catalyzed by mrcA (protein.P02918), mrcB (protein.P02919), ftsW (protein.P0ABG4), mrdB (protein.P0ABG7), mtgA (protein.P46022), pbpC (protein.P76577). Substrates: Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-gamma-D-glutamyl-L-lysyl-D-alanyl-D-alanine (molecule.C05893). Products: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574).

## Annotation

Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-gamma-D-glutamyl-L-lysyl-D-alanyl-D-alanine + [GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-g-D-Glu-L-Lys-D-Ala-D-Ala)]n-diphosphoundecaprenol <=> di-trans,poly-cis-Undecaprenyl diphosphate + [GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-g-D-Glu-L-Lys-D-Ala-D-Ala)]n-diphosphoundecaprenol

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P02918|protein.P02918]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P02919|protein.P02919]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P0ABG4|protein.P0ABG4]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P0ABG7|protein.P0ABG7]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P46022|protein.P46022]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` <-- [[protein.P76577|protein.P76577]] `KEGG` `database` - via EC:2.4.99.28
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `KEGG` `database` - C05893 + C11826 <=> C04574 + C11826
- `is_substrate_of` <-- [[molecule.C05893|molecule.C05893]] `KEGG` `database` - C05893 + C11826 <=> C04574 + C11826

## External IDs

- `KEGG:R06178`

## Notes

EQUATION: C05893 + C11826 <=> C04574 + C11826
