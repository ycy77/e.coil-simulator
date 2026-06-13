---
entity_id: "protein.P76298"
entity_type: "protein"
name: "flhA"
source_database: "UniProt"
source_id: "P76298"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flhA b1879 JW1868"
---

# flhA

`protein.P76298`

## Static

- Type: `protein`
- Source: `UniProt:P76298`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Required for formation of the rod structure of the flagellar apparatus. Together with FliI and FliH, may constitute the export apparatus of flagellin. FlhA is one of six integral membrane components of the flagellar export apparatus. FlhA has two regions: the hydrophobic N-terminal transmembrane region with eight membrane-spanning segments and the C-terminal cytoplasmic domain . The structures of the C-terminal domain of FlhA and a fragment of the domain have been determined by X-ray crystallography to a resolution of 2.9 and 3.2 Å, respectively . Temperature-sensitive mutations in the cytoplasmic region of FlhA can prevent flagellar export . FlhA is osmosensitive and is involved in the stress response at pH 6.5 or lower .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Required for formation of the rod structure of the flagellar apparatus. Together with FliI and FliH, may constitute the export apparatus of flagellin.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1879|gene.b1879]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76298`
- `KEGG:ecj:JW1868;eco:b1879;ecoc:C3026_10690;`
- `GeneID:946390;`
- `GO:GO:0005886; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044780; GO:0071973; GO:0120102`

## Notes

Flagellar biosynthesis protein FlhA
