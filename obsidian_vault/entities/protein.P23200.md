---
entity_id: "protein.P23200"
entity_type: "protein"
name: "mglC"
source_database: "UniProt"
source_id: "P23200"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mglC b2148 JW2135"
---

# mglC

`protein.P23200`

## Static

- Type: `protein`
- Source: `UniProt:P23200`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:6807987}. MglC is the predicted integral membrane component of a D-galactose / D-galactoside ABC transporter. mglC mutants are unable to accumulate labeled methyl-β-D-galactopyranoside .

## Biological Role

Component of D-galactose / methyl-β-D-galactoside ABC transporter (complex.ecocyc.ABC-18-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:6807987}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-18-CPLX|complex.ecocyc.ABC-18-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2148|gene.b2148]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23200`
- `KEGG:ecj:JW2135;eco:b2148;ecoc:C3026_12035;`
- `GeneID:93775034;949039;`
- `GO:GO:0005354; GO:0005886; GO:0006974; GO:0015592; GO:0015757; GO:0015765; GO:0016020; GO:0055052`

## Notes

Galactose/methyl galactoside import permease protein MglC
