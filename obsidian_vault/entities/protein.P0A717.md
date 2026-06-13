---
entity_id: "protein.P0A717"
entity_type: "protein"
name: "prs"
source_database: "UniProt"
source_id: "P0A717"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00583}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prs prsA b1207 JW1198"
---

# prs

`protein.P0A717`

## Static

- Type: `protein`
- Source: `UniProt:P0A717`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00583}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the central metabolite phospho-alpha-D-ribosyl-1-pyrophosphate (PRPP) via the transfer of pyrophosphoryl group from ATP to 1-hydroxyl of ribose-5-phosphate (Rib-5-P). {ECO:0000255|HAMAP-Rule:MF_00583, ECO:0000269|PubMed:10954724, ECO:0000269|PubMed:2542328, ECO:0000269|PubMed:3009477, ECO:0000269|PubMed:6290219, ECO:0000269|PubMed:7657655, ECO:0000269|PubMed:8679571, ECO:0000269|PubMed:9125530}.

## Biological Role

Component of ribose-phosphate diphosphokinase (complex.ecocyc.CPLX0-8299).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the central metabolite phospho-alpha-D-ribosyl-1-pyrophosphate (PRPP) via the transfer of pyrophosphoryl group from ATP to 1-hydroxyl of ribose-5-phosphate (Rib-5-P). {ECO:0000255|HAMAP-Rule:MF_00583, ECO:0000269|PubMed:10954724, ECO:0000269|PubMed:2542328, ECO:0000269|PubMed:3009477, ECO:0000269|PubMed:6290219, ECO:0000269|PubMed:7657655, ECO:0000269|PubMed:8679571, ECO:0000269|PubMed:9125530}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8299|complex.ecocyc.CPLX0-8299]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1207|gene.b1207]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A717`
- `KEGG:ecj:JW1198;eco:b1207;ecoc:C3026_07095;`
- `GeneID:86859980;93775272;945772;`
- `GO:GO:0000287; GO:0002189; GO:0004749; GO:0005524; GO:0005737; GO:0005829; GO:0006015; GO:0006164; GO:0009156; GO:0016301; GO:0034214; GO:0042301; GO:0042802; GO:0043531`
- `EC:2.7.6.1`

## Notes

Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase) (PRPPase)
