---
entity_id: "protein.P0A9Q9"
entity_type: "protein"
name: "asd"
source_database: "UniProt"
source_id: "P0A9Q9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "asd hom b3433 JW3396"
---

# asd

`protein.P0A9Q9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9Q9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate-semialdehyde (L-ASA) by the reductive dephosphorylation of L-aspartyl-4-phosphate. {ECO:0000269|PubMed:11368768, ECO:0000269|PubMed:6102909}.

## Biological Role

Component of aspartate-semialdehyde dehydrogenase (complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate-semialdehyde (L-ASA) by the reductive dephosphorylation of L-aspartyl-4-phosphate. {ECO:0000269|PubMed:11368768, ECO:0000269|PubMed:6102909}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX|complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3433|gene.b3433]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9Q9`
- `KEGG:ecj:JW3396;eco:b3433;ecoc:C3026_18610;`
- `GeneID:75173592;75202278;947939;`
- `GO:GO:0004073; GO:0005829; GO:0006974; GO:0009088; GO:0009089; GO:0009090; GO:0009097; GO:0019877; GO:0046983; GO:0050661; GO:0051287; GO:0071266`
- `EC:1.2.1.11`

## Notes

Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase)
