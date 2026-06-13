---
entity_id: "protein.P0ABY7"
entity_type: "protein"
name: "flhC"
source_database: "UniProt"
source_id: "P0ABY7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flhC flaI b1891 JW1880"
---

# flhC

`protein.P0ABY7`

## Static

- Type: `protein`
- Source: `UniProt:P0ABY7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Functions in complex with FlhD as a master transcriptional regulator that regulates transcription of several flagellar and non-flagellar operons by binding to their promoter region. Activates expression of class 2 flagellar genes, including fliA, which is a flagellum-specific sigma factor that turns on the class 3 genes. Also regulates genes whose products function in a variety of physiological pathways. {ECO:0000269|PubMed:11169100, ECO:0000269|PubMed:15941987, ECO:0000269|PubMed:7961507}.

## Biological Role

Component of FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Functions in complex with FlhD as a master transcriptional regulator that regulates transcription of several flagellar and non-flagellar operons by binding to their promoter region. Activates expression of class 2 flagellar genes, including fliA, which is a flagellum-specific sigma factor that turns on the class 3 genes. Also regulates genes whose products function in a variety of physiological pathways. {ECO:0000269|PubMed:11169100, ECO:0000269|PubMed:15941987, ECO:0000269|PubMed:7961507}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1891|gene.b1891]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABY7`
- `KEGG:ecj:JW1880;eco:b1891;ecoc:C3026_10750;`
- `GeneID:93776196;947280;`
- `GO:GO:0000166; GO:0003677; GO:0005667; GO:0005737; GO:0006351; GO:0008270; GO:0044781; GO:0045893; GO:1902210`

## Notes

Flagellar transcriptional regulator FlhC
