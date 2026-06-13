---
entity_id: "protein.P60757"
entity_type: "protein"
name: "hisG"
source_database: "UniProt"
source_id: "P60757"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisG b2019 JW2001"
---

# hisG

`protein.P60757`

## Static

- Type: `protein`
- Source: `UniProt:P60757`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the condensation of ATP and 5-phosphoribose 1-diphosphate to form N'-(5'-phosphoribosyl)-ATP (PR-ATP). Has a crucial role in the pathway because the rate of histidine biosynthesis seems to be controlled primarily by regulation of HisG enzymatic activity. {ECO:0000269|PubMed:4909873}.

## Biological Role

Component of ATP phosphoribosyltransferase (complex.ecocyc.CPLX0-7614).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of ATP and 5-phosphoribose 1-diphosphate to form N'-(5'-phosphoribosyl)-ATP (PR-ATP). Has a crucial role in the pathway because the rate of histidine biosynthesis seems to be controlled primarily by regulation of HisG enzymatic activity. {ECO:0000269|PubMed:4909873}.

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7614|complex.ecocyc.CPLX0-7614]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2019|gene.b2019]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60757`
- `KEGG:ecj:JW2001;eco:b2019;ecoc:C3026_11385;`
- `GeneID:86946973;93775154;946549;`
- `GO:GO:0000105; GO:0000287; GO:0003879; GO:0005524; GO:0005829`
- `EC:2.4.2.17`

## Notes

ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase) (EC 2.4.2.17)
