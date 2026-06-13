---
entity_id: "protein.P46883"
entity_type: "protein"
name: "tynA"
source_database: "UniProt"
source_id: "P46883"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tynA maoA b1386 JW1381"
---

# tynA

`protein.P46883`

## Static

- Type: `protein`
- Source: `UniProt:P46883`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: The enzyme prefers aromatic over aliphatic amines.

## Biological Role

Catalyzes tyramine:oxygen oxidoreductase(deaminating)(flavin-containing) (reaction.R02382), phenethylamine:oxygen oxidoreductase (deaminating) (reaction.R02613), primary-amine oxidase (reaction.R03139). Component of copper-containing amine oxidase (complex.ecocyc.AMINEOXID-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: The enzyme prefers aromatic over aliphatic amines.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R02382|reaction.R02382]] `KEGG` `database` - via EC:1.4.3.21
- `catalyzes` --> [[reaction.R02613|reaction.R02613]] `KEGG` `database` - via EC:1.4.3.21
- `catalyzes` --> [[reaction.R03139|reaction.R03139]] `KEGG` `database` - via EC:1.4.3.21
- `is_component_of` --> [[complex.ecocyc.AMINEOXID-CPLX|complex.ecocyc.AMINEOXID-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1386|gene.b1386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46883`
- `KEGG:ecj:JW1381;eco:b1386;ecoc:C3026_08095;`
- `GeneID:945939;`
- `GO:GO:0005507; GO:0005509; GO:0006559; GO:0008131; GO:0009308; GO:0019607; GO:0042597; GO:0048038`
- `EC:1.4.3.21`

## Notes

Primary amine oxidase (EC 1.4.3.21) (2-phenylethylamine oxidase) (Copper amine oxidase) (Tyramine oxidase)
