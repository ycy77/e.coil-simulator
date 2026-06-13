---
entity_id: "protein.P07650"
entity_type: "protein"
name: "deoA"
source_database: "UniProt"
source_id: "P07650"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "deoA tpp ttg b4382 JW4345"
---

# deoA

`protein.P07650`

## Static

- Type: `protein`
- Source: `UniProt:P07650`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The enzymes which catalyze the reversible phosphorolysis of pyrimidine nucleosides are involved in the degradation of these compounds and in their utilization as carbon and energy sources, or in the rescue of pyrimidine bases for nucleotide synthesis. DeoA is a thymidine phosphorylase which is part of the pathway that utilizes pyrimidine deoxyribonucleoside as a carbon and energy source. Thymidine phosphorylase catalyzes the phosphorolysis of thymidine and other pyrimidine 2-deoxyribosides. This enzyme is highly specific for deoxyribose 1-phosphate . The crystal structure of DeoA has been determined at 2.8 and 2.6 Å resolution . The enzyme is an S-shaped dimer with identical subunits that are related by a crystallographic 2-fold axis . Mutants lacking deoA readily incorporates exogenous thymidine into deoxyribonucleic acid, but not ribonucleic acid or other macromolecules . Thymidine phosphorylase mutants fail to grow on deoxycytodine, deoxyuridine and thymidine . More recently, a ΔdeoA mutant was found to be required for thymine-starvation induced chromosome fragmentation (TiCF) and may encode a critical anti-fragmentation factor. Conversely, fast removal of thymidine by DeoA can "snap-starve" replication forks for dTTP resulting in replication forks freezing in place and not undergoing disintegration, possibly blocking TiCF...

## Biological Role

Catalyzes 5'-deoxy-5-fluorouridine:phosphate deoxy-alpha-D-ribosyltransferase (reaction.R08222), 5-fluorodeoxyuridine:phosphate deoxy-alpha-D-ribosyltransferase (reaction.R08230). Component of thymidine phosphorylase / uracil phosphorylase (complex.ecocyc.DEOA-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: The enzymes which catalyze the reversible phosphorolysis of pyrimidine nucleosides are involved in the degradation of these compounds and in their utilization as carbon and energy sources, or in the rescue of pyrimidine bases for nucleotide synthesis.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R08222|reaction.R08222]] `KEGG` `database` - via EC:2.4.2.4
- `catalyzes` --> [[reaction.R08230|reaction.R08230]] `KEGG` `database` - via EC:2.4.2.4
- `is_component_of` --> [[complex.ecocyc.DEOA-CPLX|complex.ecocyc.DEOA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4382|gene.b4382]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07650`
- `KEGG:ecj:JW4345;eco:b4382;ecoc:C3026_23680;`
- `GeneID:948901;`
- `GO:GO:0004645; GO:0005829; GO:0006206; GO:0006213; GO:0006974; GO:0009032; GO:0016020; GO:0046104`
- `EC:2.4.2.4`

## Notes

Thymidine phosphorylase (EC 2.4.2.4) (TdRPase)
