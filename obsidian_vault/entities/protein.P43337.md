---
entity_id: "protein.P43337"
entity_type: "protein"
name: "nudL"
source_database: "UniProt"
source_id: "P43337"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudL yeaB b1813 JW1802"
---

# nudL

`protein.P43337`

## Static

- Type: `protein`
- Source: `UniProt:P43337`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably mediates the hydrolysis of some nucleoside diphosphate derivatives. {ECO:0000255|HAMAP-Rule:MF_01592}. NudL belongs to the Nudix family of hydrolases and was predicted to have CoA pyrophosphohydrolase activity . nudL (yeaB) was isolated as a multicopy suppressor of the repression of flhDC transcription in a pgsA mutant. The suppression may be due to the reduction of σS expression in cells that overexpress nudL . nudL (yeaB) was also isolated as a multicopy suppressor of the PLP auxotrophy of a pdxB deletion strain. NudL was found to be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 4-PHOSPHONOOXY-THREONINE, that lies downstream of PdxB. The pathway diverts 3-phosphohydroxypyruvate from serine biosynthesis. With a Kcat of 5.7x10-5, NudL is an inefficient catalyst of the conversion of 3-phosphohydroxypyruvate to hydroxypyruvate, but its activity appears to be sufficient for production of PLP . Review:

## Biological Role

Catalyzes RXN0-6562 (reaction.ecocyc.RXN0-6562).

## Annotation

FUNCTION: Probably mediates the hydrolysis of some nucleoside diphosphate derivatives. {ECO:0000255|HAMAP-Rule:MF_01592}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6562|reaction.ecocyc.RXN0-6562]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1813|gene.b1813]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P43337`
- `KEGG:ecj:JW1802;eco:b1813;ecoc:C3026_10325;`
- `GeneID:946330;`
- `GO:GO:0000287; GO:0009132; GO:0010945; GO:0016818; GO:0030145`
- `EC:3.6.1.-`

## Notes

Uncharacterized Nudix hydrolase NudL (EC 3.6.1.-)
