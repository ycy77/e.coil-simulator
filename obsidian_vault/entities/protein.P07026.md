---
entity_id: "protein.P07026"
entity_type: "protein"
name: "sdiA"
source_database: "UniProt"
source_id: "P07026"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdiA b1916 JW1901"
---

# sdiA

`protein.P07026`

## Static

- Type: `protein`
- Source: `UniProt:P07026`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Activates cell division by specifically increasing transcription from one of the two promoters that lie immediately upstream of the ftsQAZ gene cluster. Activates ydiV expression in response to extracellular autoinducer AI-1 (Vibrio fischeri autoinducer oxoC6). {ECO:0000269|PubMed:18560382, ECO:0000269|PubMed:1915297}. The transcription factor SdiA, for "Suppressor of the cell division inhibitor," is possibly positively autoregulated and controls the transcription of the genes involved in cell division and acid tolerance . SdiA has been shown to increase transcription from the P2 promoter of the ftsQAZ operon by facilitating RNA polymerase binding to the promoter region . SdiA activates the expression of ydiV, which is involved in the interaction between two quorum-sensing systems. An sdiA ydiV double mutant reduces cAMP levels, which inhibits quorum-sensing system 2 . Expression of sdiA itself is regulated by a mechanism similar to quorum sensing: exposure to conditioned medium results in a 50-80% decrease in sdiA expression . The transcriptional activity of SdiA is affected not only by quorum signaling but also by other environmental factors, such as oxidation . Overexpression of SdiA speeds up cell division and causes apparently concomitant morphological changes; in both exponential and stationary phases, cells appear rounder and shorter...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Activates cell division by specifically increasing transcription from one of the two promoters that lie immediately upstream of the ftsQAZ gene cluster. Activates ydiV expression in response to extracellular autoinducer AI-1 (Vibrio fischeri autoinducer oxoC6). {ECO:0000269|PubMed:18560382, ECO:0000269|PubMed:1915297}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (7)

- `activates` --> [[gene.b0093|gene.b0093]] `RegulonDB` `S` - regulator=SdiA; target=ftsQ; function=-+
- `activates` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=SdiA; target=rmf; function=+
- `activates` --> [[gene.b1707|gene.b1707]] `RegulonDB` `S` - regulator=SdiA; target=rflP; function=+
- `activates` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=SdiA; target=rsd; function=+
- `represses` --> [[gene.b0093|gene.b0093]] `RegulonDB` `S` - regulator=SdiA; target=ftsQ; function=-+
- `represses` --> [[gene.b0094|gene.b0094]] `RegulonDB` `S` - regulator=SdiA; target=ftsA; function=-
- `represses` --> [[gene.b0095|gene.b0095]] `RegulonDB` `S` - regulator=SdiA; target=ftsZ; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1916|gene.b1916]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07026`
- `KEGG:ecj:JW1901;eco:b1916;ecoc:C3026_10875;`
- `GeneID:946421;`
- `GO:GO:0003677; GO:0051301; GO:2000144`

## Notes

Regulatory protein SdiA
