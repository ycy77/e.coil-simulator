---
entity_id: "protein.P37353"
entity_type: "protein"
name: "menE"
source_database: "UniProt"
source_id: "P37353"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menE b2260 JW2255"
---

# menE

`protein.P37353`

## Static

- Type: `protein`
- Source: `UniProt:P37353`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts 2-succinylbenzoate (OSB) to 2-succinylbenzoyl-CoA (OSB-CoA). {ECO:0000255|HAMAP-Rule:MF_00731, ECO:0000269|PubMed:8626063}. O-succinylbenzoate-CoA ligase (MenE) catalyzes the formation of an intermediate in menaquinone biosynthesis, o-succinylbenzoyl-CoA . Inhibition of the enzymatic activity by diethylpyrocarbonate suggested that a histidine residue located near the active site is essential for catalysis; mutagenesis of the His341 residue located in the predicted ATP binding region leads to loss of 65% of enzymatic activity . Mutagenesis of the conserved R195 residue results in reduced catalytic activity due to an increase in KM for O-succinylbenzoate . A crystal structure of the R195K mutant in a complex with the inhibitor OSB-AMS has been solved . Menaquinone biosynthesis provides an attractive antibacterial drug target. Inhibitors of MenE activity have been identified and tested . A menE mutant lacks o-succinylbenzoate-CoA ligase activity . Deletion of menC, menD or menE leads to loss of the ability to reduce selenate . Review:

## Biological Role

Component of o-succinylbenzoate—CoA ligase (complex.ecocyc.MENE-CPLX).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Converts 2-succinylbenzoate (OSB) to 2-succinylbenzoyl-CoA (OSB-CoA). {ECO:0000255|HAMAP-Rule:MF_00731, ECO:0000269|PubMed:8626063}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MENE-CPLX|complex.ecocyc.MENE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2260|gene.b2260]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37353`
- `KEGG:ecj:JW2255;eco:b2260;ecoc:C3026_12625;`
- `GeneID:946741;`
- `GO:GO:0005524; GO:0008756; GO:0009234; GO:0032991; GO:0042802`
- `EC:6.2.1.26`

## Notes

2-succinylbenzoate--CoA ligase (EC 6.2.1.26) (o-succinylbenzoyl-CoA synthetase) (OSB-CoA synthetase)
