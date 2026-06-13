---
entity_id: "protein.P0AAG8"
entity_type: "protein"
name: "mglA"
source_database: "UniProt"
source_id: "P0AAG8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01717, ECO:0000305|PubMed:6294056}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01717, ECO:0000305|PubMed:6294056}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mglA b2149 JW2136"
---

# mglA

`protein.P0AAG8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAG8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01717, ECO:0000305|PubMed:6294056}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01717, ECO:0000305|PubMed:6294056}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:4910389, ECO:0000305|PubMed:6294056, ECO:0000305|PubMed:6807987}. MglA is the predicted ATP-binding component of a D-galactose / D-galactoside ABC transporter. mglA mutants are unable to accumulate labeled methyl-β-D-galactopyranoside . mglA+ plasmids direct the synthesis of a 50 kD protein in minicells . mglA contains an ABC-ABC domain

## Biological Role

Component of D-galactose / methyl-β-D-galactoside ABC transporter (complex.ecocyc.ABC-18-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:4910389, ECO:0000305|PubMed:6294056, ECO:0000305|PubMed:6807987}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-18-CPLX|complex.ecocyc.ABC-18-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2149|gene.b2149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAG8`
- `KEGG:ecj:JW2136;eco:b2149;`
- `GeneID:75172277;949036;`
- `GO:GO:0005354; GO:0005524; GO:0005886; GO:0006974; GO:0015592; GO:0015757; GO:0015765; GO:0016020; GO:0016887; GO:0055052`
- `EC:7.5.2.11`

## Notes

Galactose/methyl galactoside import ATP-binding protein MglA (EC 7.5.2.11)
