---
entity_id: "protein.P41409"
entity_type: "protein"
name: "rihA"
source_database: "UniProt"
source_id: "P41409"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rihA ybeK b0651 JW0646"
---

# rihA

`protein.P41409`

## Static

- Type: `protein`
- Source: `UniProt:P41409`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes with equal efficiency cytidine or uridine to ribose and cytosine or uracil, respectively.

## Biological Role

Component of pyrimidine-specific ribonucleoside hydrolase RihA (complex.ecocyc.CPLX0-8280).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Hydrolyzes with equal efficiency cytidine or uridine to ribose and cytosine or uracil, respectively.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8280|complex.ecocyc.CPLX0-8280]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0651|gene.b0651]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41409`
- `KEGG:ecj:JW0646;eco:b0651;ecoc:C3026_03255;`
- `GeneID:945503;`
- `GO:GO:0005509; GO:0005829; GO:0006152; GO:0006206; GO:0008477; GO:0015949; GO:0032991; GO:0042802; GO:0045437; GO:0046133; GO:0050263; GO:0051289`
- `EC:3.2.-.-`

## Notes

Pyrimidine-specific ribonucleoside hydrolase RihA (EC 3.2.-.-) (Cytidine/uridine-specific hydrolase)
