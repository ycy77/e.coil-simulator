---
entity_id: "protein.P0A715"
entity_type: "protein"
name: "kdsA"
source_database: "UniProt"
source_id: "P0A715"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdsA b1215 JW1206"
---

# kdsA

`protein.P0A715`

## Static

- Type: `protein`
- Source: `UniProt:P0A715`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}.

## Enriched Summary

FUNCTION: Synthesis of KDO 8-P which is required for lipid A maturation and cellular growth. 3-deoxy-D-manno-octulosonate 8-phosphate (KDO-8-P) synthase is a key enzyme in lipopolysaccharide biosynthesis. It catalyzes the condensation of arabinose-5-phosphate and PEP by cleavage of the C-O bond in PEP, forming the eight-carbon skeleton of 3-deoxy-D-manno-octulosonate, which serves as a linker between the hydrophobic portion of lipopolysaccharide, lipid A, and the hydrophilic polysaccharide chain. The reaction mechanism has been studied extensively . Various crystal structures of KdsA have been solved . The enzyme appears to be a homotetramer , although initial biochemical data of the E. coli B enzyme seemed to favor a trimeric form . The crystal structures allowed confirmation of the observed stereochemical preferences and reaction mechanism of the enzyme and provide an explanation for the irreversible nature of the reaction . Two cysteine residues, C38 and C166, are important for catalytic activity . Two conserved histidine residues, H97 and H241, are important for catalytic activity, and a third residue, H202, is essential . The wild type E...

## Biological Role

Component of 3-deoxy-D-manno-octulosonate 8-phosphate synthase (complex.ecocyc.KDO-8PSYNTH-CPLX).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Synthesis of KDO 8-P which is required for lipid A maturation and cellular growth.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.KDO-8PSYNTH-CPLX|complex.ecocyc.KDO-8PSYNTH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1215|gene.b1215]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A715`
- `KEGG:ecj:JW1206;eco:b1215;ecoc:C3026_07135;`
- `GeneID:75171326;75203328;945785;`
- `GO:GO:0005829; GO:0008676; GO:0019294; GO:0032991; GO:0042802`
- `EC:2.5.1.55`

## Notes

2-dehydro-3-deoxyphosphooctonate aldolase (EC 2.5.1.55) (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase) (KDO-8-phosphate synthase) (KDO 8-P synthase) (KDOPS) (Phospho-2-dehydro-3-deoxyoctonate aldolase)
