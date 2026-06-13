---
entity_id: "protein.P39380"
entity_type: "protein"
name: "kptA"
source_database: "UniProt"
source_id: "P39380"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kptA yjiI b4331 JW5784"
---

# kptA

`protein.P39380`

## Static

- Type: `protein`
- Source: `UniProt:P39380`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Removes the 2'-phosphate from RNA via an intermediate in which the phosphate is ADP-ribosylated by NAD followed by a presumed transesterification to release the RNA and generate ADP-ribose 1''-2''-cyclic phosphate (APPR>P). May function as an ADP-ribosylase. {ECO:0000269|PubMed:9915792}. KptA exhibits tRNA 2'-phosphotransferase activity. However, 2' phopsphorylated RNA is a splicing intermediate; thus, this substrate is not likely to have physiological relevance in E. coli . KptA has similarity to Saccharomyces cerevisiae Tpt1, a tRNA splicing enzyme. Unlike Tpt1, KptA accumulates the ADP-ribosylated RNA reaction intermediate . Comparative genomics suggests that KptA may play a role in NAD metabolism .

## Annotation

FUNCTION: Removes the 2'-phosphate from RNA via an intermediate in which the phosphate is ADP-ribosylated by NAD followed by a presumed transesterification to release the RNA and generate ADP-ribose 1''-2''-cyclic phosphate (APPR>P). May function as an ADP-ribosylase. {ECO:0000269|PubMed:9915792}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4331|gene.b4331]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39380`
- `KEGG:ecj:JW5784;eco:b4331;ecoc:C3026_23410;`
- `GeneID:948858;`
- `GO:GO:0000215; GO:0003950; GO:0006388; GO:0008033; GO:0016772`
- `EC:2.7.1.-`

## Notes

RNA 2'-phosphotransferase (EC 2.7.1.-)
