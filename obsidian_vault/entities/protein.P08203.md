---
entity_id: "protein.P08203"
entity_type: "protein"
name: "araD"
source_database: "UniProt"
source_id: "P08203"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araD b0061 JW0060"
---

# araD

`protein.P08203`

## Static

- Type: `protein`
- Source: `UniProt:P08203`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the degradation of L-arabinose (PubMed:13890280). Catalyzes the interconversion of L-ribulose 5-phosphate (LRu5P) and D-xylulose 5-phosphate (D-Xu5P) via a retroaldol/aldol mechanism (carbon-carbon bond cleavage analogous to a class II aldolase reaction). {ECO:0000255|HAMAP-Rule:MF_00989, ECO:0000269|PubMed:10769138, ECO:0000269|PubMed:10769139, ECO:0000269|PubMed:11732896, ECO:0000269|PubMed:13890280, ECO:0000269|PubMed:4879898, ECO:0000269|PubMed:9548961}. L-ribulose 5-phosphate 4-epimerase catalyzes the third step in the pathway for degradation of L-arabinose, the epimerization at the C4 carbon to form D-xylulose-5-phosphate, which enters the NONOXIPENT-PWY. The enzyme catalyzes epimerization via a carbon-carbon bond cleavage analogous to a class II aldolase reaction . The H97N and other mutants can catalyze an aldolase reaction . The binding site for Zn2+, the physiological metal cofactor, has been identified by sequence similarity and mutagenesis as well as in the crystal structure . Mutagenesis of the predicted phosphate-binding pocket results in a significant increase in Km, and Asp120 was identified as one of two key catalytic acid/base residues . The enzyme was crystallized , and crystal structures of the wild type and a mutant enzyme have been solved...

## Biological Role

Catalyzes L-ribulose-5-phosphate 4-epimerase (reaction.R05850). Component of L-ribulose-5-phosphate 4-epimerase AraD (complex.ecocyc.RIBULPEPIM-CPLX).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in the degradation of L-arabinose (PubMed:13890280). Catalyzes the interconversion of L-ribulose 5-phosphate (LRu5P) and D-xylulose 5-phosphate (D-Xu5P) via a retroaldol/aldol mechanism (carbon-carbon bond cleavage analogous to a class II aldolase reaction). {ECO:0000255|HAMAP-Rule:MF_00989, ECO:0000269|PubMed:10769138, ECO:0000269|PubMed:10769139, ECO:0000269|PubMed:11732896, ECO:0000269|PubMed:13890280, ECO:0000269|PubMed:4879898, ECO:0000269|PubMed:9548961}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05850|reaction.R05850]] `KEGG` `database` - via EC:5.1.3.4
- `is_component_of` --> [[complex.ecocyc.RIBULPEPIM-CPLX|complex.ecocyc.RIBULPEPIM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0061|gene.b0061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08203`
- `KEGG:ecj:JW0060;eco:b0061;`
- `GeneID:945294;`
- `GO:GO:0005829; GO:0008270; GO:0008742; GO:0016832; GO:0019323; GO:0019324; GO:0019569; GO:0032991; GO:0042802`
- `EC:5.1.3.4`

## Notes

L-ribulose-5-phosphate 4-epimerase AraD (EC 5.1.3.4) (Phosphoribulose isomerase)
