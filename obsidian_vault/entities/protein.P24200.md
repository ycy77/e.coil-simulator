---
entity_id: "protein.P24200"
entity_type: "protein"
name: "mcrA"
source_database: "UniProt"
source_id: "P24200"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mcrA rglA b1159 JW1145"
---

# mcrA

`protein.P24200`

## Static

- Type: `protein`
- Source: `UniProt:P24200`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Restriction of 5-methyl and 5-hydroxymethylcytosines at the specific DNA sequence 5'-C(me)CGG-3'. The McrA protein is a type IV site-specific deoxyribonuclease and is one of three restriction systems defending the cell against foreign DNA, such as bacteriophages. It specifically recognizes 5-methylcytosine residues in DNA , but the precise recognition sequence has not yet been identified. McrA was initially identified as a cellular activity that degraded T-even phage DNA containing nonglucosylated DNA . The rglA and mcrA phenotypes are separable; see the discussion in and references therein. Structural modelling of McrA has identified similarity to the ββαMe superfamily of endonucleases . Linker insertion scanning mutagenesis has been used to study the functional domain architecture . mcrA is part of the defective lambdoid prophage element e14 . After induction of the SOS response by UV irradiation, the prophage is abortively excised from the E. coli chromosome, leading to decreased levels of McrA restriction within a cell population . Restriction of methylated DNA is responsible for difficulties with cloning methylcytosine-containing DNA from various sources in E. coli . RglA = "restricts glucoseless DNA" McrA = "modified cytosine restriction"

## Biological Role

Catalyzes RXN0-2942 (reaction.ecocyc.RXN0-2942).

## Annotation

FUNCTION: Restriction of 5-methyl and 5-hydroxymethylcytosines at the specific DNA sequence 5'-C(me)CGG-3'.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2942|reaction.ecocyc.RXN0-2942]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1159|gene.b1159]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24200`
- `KEGG:ecj:JW1145;eco:b1159;`
- `GeneID:945727;`
- `GO:GO:0004519; GO:0008270; GO:0008327; GO:0009307; GO:0016787`
- `EC:3.1.21.-`

## Notes

Type IV methyl-directed restriction enzyme EcoKMcrA (EcoKMcrA) (EC 3.1.21.-) (5-methylcytosine-specific restriction enzyme A)
