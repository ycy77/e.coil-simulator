---
entity_id: "protein.P15373"
entity_type: "protein"
name: "prlF"
source_database: "UniProt"
source_id: "P15373"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prlF sohA b3129 JW3098"
---

# prlF

`protein.P15373`

## Static

- Type: `protein`
- Source: `UniProt:P15373`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the YhaV toxin and neutralizes its ribonuclease activity. Also acts as a transcription factor. The YhaV/PrlF complex binds the prlF-yhaV operon, probably negatively regulating its expression. {ECO:0000269|PubMed:17706670}.; FUNCTION: Negatively regulates its own expression as well as relieving the export block imposed by high-level synthesis of the LamB-LacZ hybrid protein. Overexpression leads to increased doubling time and also suppresses a htrA (degP) null phenotype. {ECO:0000269|PubMed:17706670}. PrlF is the antitoxin component in the PrlF-YhaV antitoxin-toxin complex. Overproduction of PrlF yields a growth defect and increased export of a reporter protein . prlF mutants show activated CPLX0-2881 activity, and suppression of heat sensitivity in htrA mutants . prlF htrA double mutants are cold sensitive . Review:

## Biological Role

Component of YhaV-PrlF toxin-antitoxin complex (complex.ecocyc.CPLX0-7624).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the YhaV toxin and neutralizes its ribonuclease activity. Also acts as a transcription factor. The YhaV/PrlF complex binds the prlF-yhaV operon, probably negatively regulating its expression. {ECO:0000269|PubMed:17706670}.; FUNCTION: Negatively regulates its own expression as well as relieving the export block imposed by high-level synthesis of the LamB-LacZ hybrid protein. Overexpression leads to increased doubling time and also suppresses a htrA (degP) null phenotype. {ECO:0000269|PubMed:17706670}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7624|complex.ecocyc.CPLX0-7624]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3129|gene.b3129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15373`
- `KEGG:ecj:JW3098;eco:b3129;ecoc:C3026_17055;`
- `GeneID:75203755;947639;`
- `GO:GO:0001558; GO:0003677; GO:0003700; GO:0005737; GO:0006355; GO:0019899; GO:0040008; GO:0042802; GO:0044010; GO:0045892; GO:0097351; GO:0110001`

## Notes

Antitoxin PrlF (HtrA suppressor protein SohA)
