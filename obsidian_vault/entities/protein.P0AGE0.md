---
entity_id: "protein.P0AGE0"
entity_type: "protein"
name: "ssb"
source_database: "UniProt"
source_id: "P0AGE0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ssb exrB lexC b4059 JW4020"
---

# ssb

`protein.P0AGE0`

## Static

- Type: `protein`
- Source: `UniProt:P0AGE0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Plays an important role in DNA replication, recombination and repair. Binds to ssDNA and to an array of partner proteins to recruit them to their sites of action during DNA metabolism. Acts as a sliding platform that migrates on DNA via reptation. SSB or its 10 C-terminal amino acids stimulates the ATPase activity of RadD (PubMed:27519413). {ECO:0000255|HAMAP-Rule:MF_00984, ECO:0000269|PubMed:18937104, ECO:0000269|PubMed:20360609, ECO:0000269|PubMed:21784244, ECO:0000269|PubMed:27519413}.

## Biological Role

Component of replisome (complex.ecocyc.CPLX0-13320), ssDNA-binding protein (complex.ecocyc.CPLX0-8165).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Plays an important role in DNA replication, recombination and repair. Binds to ssDNA and to an array of partner proteins to recruit them to their sites of action during DNA metabolism. Acts as a sliding platform that migrates on DNA via reptation. SSB or its 10 C-terminal amino acids stimulates the ATPase activity of RadD (PubMed:27519413). {ECO:0000255|HAMAP-Rule:MF_00984, ECO:0000269|PubMed:18937104, ECO:0000269|PubMed:20360609, ECO:0000269|PubMed:21784244, ECO:0000269|PubMed:27519413}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=7
- `is_component_of` --> [[complex.ecocyc.CPLX0-8165|complex.ecocyc.CPLX0-8165]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## Incoming Edges (1)

- `encodes` <-- [[gene.b4059|gene.b4059]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGE0`
- `KEGG:ecj:JW4020;eco:b4059;ecoc:C3026_21935;`
- `GeneID:86944601;948570;`
- `GO:GO:0000725; GO:0003697; GO:0005829; GO:0006260; GO:0006261; GO:0006298; GO:0008047; GO:0009295; GO:0009432; GO:0030894; GO:0042802; GO:0044777`

## Notes

Single-stranded DNA-binding protein (SSB) (Helix-destabilizing protein)
