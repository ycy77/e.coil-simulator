---
entity_id: "protein.P0AEZ1"
entity_type: "protein"
name: "metF"
source_database: "UniProt"
source_id: "P0AEZ1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metF b3941 JW3913"
---

# metF

`protein.P0AEZ1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEZ1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADH-dependent reduction of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate (PubMed:9922232). Is required to provide the methyl group necessary for methionine synthetase to convert homocysteine to methionine; the methyl group is given by 5-methyltetrahydrofolate. Can also use NADPH as the reductant, but much less effectively than NADH (PubMed:9922232). {ECO:0000269|PubMed:14275142, ECO:0000269|PubMed:9922232}. E. coli MetF is a flavoprotein capable of catalyzing the NADH-linked reduction of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate. The enzyme is a tetramer of four identical subunits with a beta8alpha8 barrel catalytic domain. Each of the four subunits of MetH contains a molecule of noncovalently bound flavin adenine dinucleotide (FAD) at the C-termini of the beta strands . Each of the four subunits of MetH contains a molecule of noncovalently bound flavin adenine dinucleotide (FAD). In the reaction, NADH transfers reducing equivalents to the FAD cofactor, which in turn transfers them to methyltetrahydrofolate. This reaction provides methyltetrahydrofolate to be used for methylation of homocysteine to form methionine . NADPH also serves as a reductant, but much less effectively than NADH...

## Biological Role

Component of 5,10-methylenetetrahydrofolate reductase (complex.ecocyc.METHYLENETHFREDUCT-CPLX).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the NADH-dependent reduction of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate (PubMed:9922232). Is required to provide the methyl group necessary for methionine synthetase to convert homocysteine to methionine; the methyl group is given by 5-methyltetrahydrofolate. Can also use NADPH as the reductant, but much less effectively than NADH (PubMed:9922232). {ECO:0000269|PubMed:14275142, ECO:0000269|PubMed:9922232}.

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.METHYLENETHFREDUCT-CPLX|complex.ecocyc.METHYLENETHFREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3941|gene.b3941]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEZ1`
- `KEGG:ecj:JW3913;eco:b3941;ecoc:C3026_21300;`
- `GeneID:93777951;948432;`
- `GO:GO:0004489; GO:0005829; GO:0009086; GO:0032991; GO:0035999; GO:0051087; GO:0071949; GO:0106312`
- `EC:1.5.1.54`

## Notes

5,10-methylenetetrahydrofolate reductase (MTHFR) (EC 1.5.1.54) (NADH-dependent 5,10-methylenetetrahydrofolate reductase)
