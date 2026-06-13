---
entity_id: "protein.P0A6K1"
entity_type: "protein"
name: "dapF"
source_database: "UniProt"
source_id: "P0A6K1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dapF b3809 JW5592"
---

# dapF

`protein.P0A6K1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6K1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the succinylase branch of the L-lysine biosynthesis and in the biosynthesis of the pentapeptide incorporated in the peptidoglycan moiety (PubMed:3283102). Catalyzes the stereoinversion of LL-2,6-diaminopimelate (L,L-DAP) to meso-diaminopimelate (meso-DAP) (PubMed:3031013, PubMed:3042781, PubMed:6378903). {ECO:0000269|PubMed:3031013, ECO:0000269|PubMed:3042781, ECO:0000269|PubMed:3283102, ECO:0000269|PubMed:6378903}.

## Biological Role

Component of diaminopimelate epimerase (complex.ecocyc.CPLX0-7997).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the succinylase branch of the L-lysine biosynthesis and in the biosynthesis of the pentapeptide incorporated in the peptidoglycan moiety (PubMed:3283102). Catalyzes the stereoinversion of LL-2,6-diaminopimelate (L,L-DAP) to meso-diaminopimelate (meso-DAP) (PubMed:3031013, PubMed:3042781, PubMed:6378903). {ECO:0000269|PubMed:3031013, ECO:0000269|PubMed:3042781, ECO:0000269|PubMed:3283102, ECO:0000269|PubMed:6378903}.

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7997|complex.ecocyc.CPLX0-7997]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3809|gene.b3809]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6K1`
- `KEGG:ecj:JW5592;eco:b3809;ecoc:C3026_20620;`
- `GeneID:93778134;948364;`
- `GO:GO:0005829; GO:0008047; GO:0008837; GO:0009089; GO:0042803`
- `EC:5.1.1.7`

## Notes

Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase)
