---
entity_id: "protein.P12008"
entity_type: "protein"
name: "aroC"
source_database: "UniProt"
source_id: "P12008"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroC b2329 JW2326"
---

# aroC

`protein.P12008`

## Static

- Type: `protein`
- Source: `UniProt:P12008`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the anti-1,4-elimination of the C-3 phosphate and the C-6 proR hydrogen from 5-enolpyruvylshikimate-3-phosphate (EPSP) to yield chorismate, which is the branch point compound that serves as the starting substrate for the three terminal pathways of aromatic amino acid biosynthesis. This reaction introduces a second double bond into the aromatic ring system. It uses NADPH to reduce FMN. {ECO:0000255|HAMAP-Rule:MF_00300, ECO:0000269|PubMed:10956653, ECO:0000269|PubMed:11034781, ECO:0000269|PubMed:2969724, ECO:0000269|PubMed:7848266, ECO:0000269|PubMed:7978236, ECO:0000269|PubMed:8703965}. Chorismate synthase (AroC) is involved in the 7th and last step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. This enzyme catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate into chorismate, which is the branch point compound that serves as the starting substrate for the three terminal pathways of aromatic amino acid biosynthesis. This reaction introduces a second double bond into the aromatic ring system. The enzymatic mechanism has been studied in detail . The enzyme catalyzes phosphate elimination by a 1,4-elimination mechanism that proceeds with anti-stereochemistry . The E. coli enzyme is unable to generate reduced flavin via the oxidation of reduced nicotinamide nucleotides...

## Biological Role

Component of chorismate synthase (complex.ecocyc.AROC-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the anti-1,4-elimination of the C-3 phosphate and the C-6 proR hydrogen from 5-enolpyruvylshikimate-3-phosphate (EPSP) to yield chorismate, which is the branch point compound that serves as the starting substrate for the three terminal pathways of aromatic amino acid biosynthesis. This reaction introduces a second double bond into the aromatic ring system. It uses NADPH to reduce FMN. {ECO:0000255|HAMAP-Rule:MF_00300, ECO:0000269|PubMed:10956653, ECO:0000269|PubMed:11034781, ECO:0000269|PubMed:2969724, ECO:0000269|PubMed:7848266, ECO:0000269|PubMed:7978236, ECO:0000269|PubMed:8703965}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.AROC-CPLX|complex.ecocyc.AROC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2329|gene.b2329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12008`
- `KEGG:ecj:JW2326;eco:b2329;ecoc:C3026_12975;`
- `GeneID:75172457;946814;`
- `GO:GO:0004107; GO:0005829; GO:0008652; GO:0009073; GO:0009423; GO:0010181; GO:0042802`
- `EC:4.2.3.5`

## Notes

Chorismate synthase (CS) (EC 4.2.3.5) (5-enolpyruvylshikimate-3-phosphate phospholyase) (EPSP phospholyase)
