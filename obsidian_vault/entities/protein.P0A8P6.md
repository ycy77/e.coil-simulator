---
entity_id: "protein.P0A8P6"
entity_type: "protein"
name: "xerC"
source_database: "UniProt"
source_id: "P0A8P6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm. Note=Associated with DNA."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xerC b3811 JW3784"
---

# xerC

`protein.P0A8P6`

## Static

- Type: `protein`
- Source: `UniProt:P0A8P6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm. Note=Associated with DNA.

## Enriched Summary

FUNCTION: Site-specific tyrosine recombinase, which acts by catalyzing the cutting and rejoining of the recombining DNA molecules. Binds cooperatively to specific DNA consensus sequences that are separated from XerD binding sites by a short central region, forming the heterotetrameric XerC-XerD complex that recombines DNA substrates. The complex is essential to convert dimers of the bacterial chromosome into monomers to permit their segregation at cell division. It also contributes to the segregational stability of plasmids at ColE1 xer (or cer) and pSC101 (or psi) sites. In the complex XerC specifically exchanges the top DNA strands (By similarity). {ECO:0000250, ECO:0000269|PubMed:10037776, ECO:0000269|PubMed:7744017, ECO:0000269|PubMed:9268326}. XerC is part of the Xer site-specific recombination system .

## Biological Role

Component of Xer site-specific recombination system (complex.ecocyc.CPLX0-3959).

## Annotation

FUNCTION: Site-specific tyrosine recombinase, which acts by catalyzing the cutting and rejoining of the recombining DNA molecules. Binds cooperatively to specific DNA consensus sequences that are separated from XerD binding sites by a short central region, forming the heterotetrameric XerC-XerD complex that recombines DNA substrates. The complex is essential to convert dimers of the bacterial chromosome into monomers to permit their segregation at cell division. It also contributes to the segregational stability of plasmids at ColE1 xer (or cer) and pSC101 (or psi) sites. In the complex XerC specifically exchanges the top DNA strands (By similarity). {ECO:0000250, ECO:0000269|PubMed:10037776, ECO:0000269|PubMed:7744017, ECO:0000269|PubMed:9268326}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3959|complex.ecocyc.CPLX0-3959]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3811|gene.b3811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8P6`
- `KEGG:ecj:JW3784;eco:b3811;ecoc:C3026_20630;`
- `GeneID:75059707;948355;`
- `GO:GO:0003677; GO:0005737; GO:0006276; GO:0006310; GO:0006313; GO:0007059; GO:0009009; GO:0009037; GO:0042150; GO:0048476; GO:0051301; GO:0071139`

## Notes

Tyrosine recombinase XerC
