---
entity_id: "protein.P18811"
entity_type: "protein"
name: "malI"
source_database: "UniProt"
source_id: "P18811"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malI b1620 JW1612"
---

# malI

`protein.P18811`

## Static

- Type: `protein`
- Source: `UniProt:P18811`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor for the malX and malY genes. Also regulates its own expression. Binds maltose as an inducer. {ECO:0000269|PubMed:1856179}. "Maltose inhibitor," MalI, is a repressor that controls genes related to the maltose system. It is negatively autoregulated and coordinately represses transcription of a divergent operon that encodes a maltose-glucose PTS permease and a bifunctional protein that interacts directly with the MalT transcriptional activator . This transcription factor binds to two 12-bp-long direct repeat nucleotide sequences in tandem, overlapping the malXp and malIp simultaneously . MalI shows high similarity to GalR (28%), CytR (21%), and LacI (24%), and homology to a fragment of 30 amino acids from MalT. Additionally, the N-terminal region has a helix-turn-helix DNA-binding domain . The gene encoding this protein is homologous to transcriptional repressors of the LacI/GalR family. A negative correlation between cellular growth and the copy number of the proteins MalI has been reported .

## Annotation

FUNCTION: Repressor for the malX and malY genes. Also regulates its own expression. Binds maltose as an inducer. {ECO:0000269|PubMed:1856179}.

## Outgoing Edges (3)

- `represses` --> [[gene.b1620|gene.b1620]] `RegulonDB` `S` - regulator=MalI; target=malI; function=-
- `represses` --> [[gene.b1621|gene.b1621]] `RegulonDB` `S` - regulator=MalI; target=malX; function=-
- `represses` --> [[gene.b1622|gene.b1622]] `RegulonDB` `S` - regulator=MalI; target=malY; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1620|gene.b1620]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18811`
- `KEGG:ecj:JW1612;eco:b1620;ecoc:C3026_09315;`
- `GeneID:947104;`
- `GO:GO:0000976; GO:0001217; GO:0003700; GO:0006355; GO:0032993; GO:0045892`

## Notes

Maltose regulon regulatory protein MalI
