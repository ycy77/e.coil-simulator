---
entity_id: "protein.P0A6C5"
entity_type: "protein"
name: "argA"
source_database: "UniProt"
source_id: "P0A6C5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:16890}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argA b2818 JW2786"
---

# argA

`protein.P0A6C5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6C5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:16890}.

## Enriched Summary

Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGS) (NAGS)

## Biological Role

Catalyzes acetyl-CoA:L-glutamate N-acetyltransferase (reaction.R00259). Component of N-acetylglutamate synthase (complex.ecocyc.N-ACETYLTRANSFER-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGS) (NAGS)

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00259|reaction.R00259]] `KEGG` `database` - via EC:2.3.1.1
- `is_component_of` --> [[complex.ecocyc.N-ACETYLTRANSFER-CPLX|complex.ecocyc.N-ACETYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2818|gene.b2818]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6C5`
- `KEGG:ecj:JW2786;eco:b2818;ecoc:C3026_15475;`
- `GeneID:75172902;75203790;947289;`
- `GO:GO:0004042; GO:0004358; GO:0005737; GO:0006526`
- `EC:2.3.1.1`

## Notes

Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGS) (NAGS)
