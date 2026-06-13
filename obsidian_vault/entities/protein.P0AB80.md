---
entity_id: "protein.P0AB80"
entity_type: "protein"
name: "ilvE"
source_database: "UniProt"
source_id: "P0AB80"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvE b3770 JW5606"
---

# ilvE

`protein.P0AB80`

## Static

- Type: `protein`
- Source: `UniProt:P0AB80`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts on leucine, isoleucine and valine.

## Biological Role

Component of branched-chain-amino-acid aminotransferase (complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Acts on leucine, isoleucine and valine.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX|complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3770|gene.b3770]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB80`
- `KEGG:ecj:JW5606;eco:b3770;ecoc:C3026_20420;`
- `GeneID:75174003;75204761;948278;`
- `GO:GO:0004084; GO:0005829; GO:0006532; GO:0009097; GO:0009098; GO:0009099; GO:0042802; GO:0052654; GO:0052655; GO:0052656`
- `EC:2.6.1.42`

## Notes

Branched-chain-amino-acid aminotransferase (BCAT) (EC 2.6.1.42) (Transaminase B)
