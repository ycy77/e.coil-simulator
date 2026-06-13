---
entity_id: "protein.P0A9D4"
entity_type: "protein"
name: "cysE"
source_database: "UniProt"
source_id: "P0A9D4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "placeholder"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysE b3607 JW3582"
---

# cysE

`protein.P0A9D4`

## Static

- Type: `protein`
- Source: `UniProt:P0A9D4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Serine acetyltransferase (SAT) (EC 2.3.1.30)

## Biological Role

Catalyzes acetyl-CoA:L-serine O-acetyltransferase (reaction.R00586). Component of serine acetyltransferase (complex.ecocyc.CPLX0-237), cysteine synthase complex (complex.ecocyc.CYSSYNMULTI-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Serine acetyltransferase (SAT) (EC 2.3.1.30)

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00586|reaction.R00586]] `KEGG` `database` - via EC:2.3.1.30
- `is_component_of` --> [[complex.ecocyc.CPLX0-237|complex.ecocyc.CPLX0-237]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CYSSYNMULTI-CPLX|complex.ecocyc.CYSSYNMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3607|gene.b3607]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9D4`
- `KEGG:ecj:JW3582;eco:b3607;ecoc:C3026_19560;`
- `GeneID:93778321;948126;`
- `GO:GO:0005829; GO:0006535; GO:0009001; GO:0009333; GO:0010165`
- `EC:2.3.1.30`

## Notes

Serine acetyltransferase (SAT) (EC 2.3.1.30)
