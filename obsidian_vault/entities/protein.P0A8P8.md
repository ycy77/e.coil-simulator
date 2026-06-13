---
entity_id: "protein.P0A8P8"
entity_type: "protein"
name: "xerD"
source_database: "UniProt"
source_id: "P0A8P8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xerD xprB b2894 JW2862"
---

# xerD

`protein.P0A8P8`

## Static

- Type: `protein`
- Source: `UniProt:P0A8P8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Site-specific tyrosine recombinase, which acts by catalyzing the cutting and rejoining of the recombining DNA molecules. Binds cooperatively to specific DNA consensus sequences that are separated from XerC binding sites by a short central region, forming the heterotetrameric XerC-XerD complex that recombines DNA substrates. The complex is essential to convert dimers of the bacterial chromosome into monomers to permit their segregation at cell division. It also contributes to the segregational stability of plasmids at ColE1 xer (or cer) and pSC101 (or psi) sites. In the complex XerD specifically exchanges the bottom DNA strands (By similarity). {ECO:0000250, ECO:0000269|PubMed:7744017, ECO:0000269|PubMed:9268326}. XerD is part of the Xer site-specific recombination system .

## Biological Role

Component of Xer site-specific recombination system (complex.ecocyc.CPLX0-3959).

## Annotation

FUNCTION: Site-specific tyrosine recombinase, which acts by catalyzing the cutting and rejoining of the recombining DNA molecules. Binds cooperatively to specific DNA consensus sequences that are separated from XerC binding sites by a short central region, forming the heterotetrameric XerC-XerD complex that recombines DNA substrates. The complex is essential to convert dimers of the bacterial chromosome into monomers to permit their segregation at cell division. It also contributes to the segregational stability of plasmids at ColE1 xer (or cer) and pSC101 (or psi) sites. In the complex XerD specifically exchanges the bottom DNA strands (By similarity). {ECO:0000250, ECO:0000269|PubMed:7744017, ECO:0000269|PubMed:9268326}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3959|complex.ecocyc.CPLX0-3959]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2894|gene.b2894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8P8`
- `KEGG:ecj:JW2862;eco:b2894;ecoc:C3026_15870;`
- `GeneID:89517705;93779108;947362;`
- `GO:GO:0003677; GO:0005737; GO:0006276; GO:0006310; GO:0006313; GO:0007059; GO:0009009; GO:0009037; GO:0009314; GO:0048476; GO:0051301; GO:0071139`

## Notes

Tyrosine recombinase XerD
