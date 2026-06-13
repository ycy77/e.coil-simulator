---
entity_id: "protein.P0DMC9"
entity_type: "protein"
name: "rcsA"
source_database: "UniProt"
source_id: "P0DMC9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcsA b1951 JW1935"
---

# rcsA

`protein.P0DMC9`

## Static

- Type: `protein`
- Source: `UniProt:P0DMC9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. Binds, with RcsB, to the RcsAB box to regulate expression of genes involved in colanic acid capsule synthesis. {ECO:0000255|HAMAP-Rule:MF_00982, ECO:0000269|PubMed:10702265, ECO:0000269|PubMed:1999391}. The binding site length of rcsA comes from a single reference . RcsA was proteolyzed by ATP-stimulated HslVU protease in vivo and in vitro at 41°C, and this affected the activation of expression of a cpsB::lacZ gene fusion. This effect on cpsB::lacZ fusion gene expression was similar to that produced by Lon protease under the same temperature conditions . The amount of RcsA protein is limited both by its rapid degradation by Lon, an ATP-dependent protease, and by its low level of synthesis. RcsA is degraded in a Lon-dependent fashion. The rcsA transcription level is decreased in rpoB mutants . RcsA belongs to the LuxR/UhpA protein family. The rcsA gene is upregulated in response to ampicillin treatment .

## Biological Role

Component of RcsAB DNA-binding transcriptional dual regulator (complex.ecocyc.PC00084).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. Binds, with RcsB, to the RcsAB box to regulate expression of genes involved in colanic acid capsule synthesis. {ECO:0000255|HAMAP-Rule:MF_00982, ECO:0000269|PubMed:10702265, ECO:0000269|PubMed:1999391}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PC00084|complex.ecocyc.PC00084]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1951|gene.b1951]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DMC9`
- `KEGG:ecj:JW1935;eco:b1951;ecoc:C3026_11045;`
- `GeneID:946467;`
- `GO:GO:0003677; GO:0005667; GO:0006351; GO:0045892; GO:0045893; GO:1901913; GO:1902021`

## Notes

Transcriptional regulatory protein RcsA (Colanic acid capsular biosynthesis activation protein A)
