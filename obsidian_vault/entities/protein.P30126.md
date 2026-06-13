---
entity_id: "protein.P30126"
entity_type: "protein"
name: "leuD"
source_database: "UniProt"
source_id: "P30126"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "leuD b0071 JW0070"
---

# leuD

`protein.P30126`

## Static

- Type: `protein`
- Source: `UniProt:P30126`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization between 2-isopropylmalate and 3-isopropylmalate, via the formation of 2-isopropylmaleate. Isopropylmalate (IPM) isomerase catalyzes the second step in leucine biosynthesis, converting 2-isopropylmalate to 3-isopropylmalate. LeuC and LeuD are both required for the activity of IPM isomerase . Based on the IPM isomerase in Salmonella typhimurium and cross-species complementation studies with the Salmonella and S. cerevisiae enzymes, E. coli IPM isomerase is likely to be a protein complex consisting of a 1:1 pairing of the of leuC and leuD gene products .

## Biological Role

Component of 3-isopropylmalate dehydratase (complex.ecocyc.3-ISOPROPYLMALISOM-CPLX).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization between 2-isopropylmalate and 3-isopropylmalate, via the formation of 2-isopropylmaleate.

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.3-ISOPROPYLMALISOM-CPLX|complex.ecocyc.3-ISOPROPYLMALISOM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0071|gene.b0071]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30126`
- `KEGG:ecj:JW0070;eco:b0071;`
- `GeneID:93777364;945642;`
- `GO:GO:0003861; GO:0005829; GO:0009098; GO:0009316`
- `EC:4.2.1.33`

## Notes

3-isopropylmalate dehydratase small subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase)
