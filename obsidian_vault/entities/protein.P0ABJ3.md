---
entity_id: "protein.P0ABJ3"
entity_type: "protein"
name: "cyoC"
source_database: "UniProt"
source_id: "P0ABJ3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cyoC b0430 JW0420"
---

# cyoC

`protein.P0ABJ3`

## Static

- Type: `protein`
- Source: `UniProt:P0ABJ3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. CyoC is subunit III of the 4 subunit cytochrome bo complex. Subunit III is required for expression of a functional enzyme . The CyoC polypeptide contains five transmembrane helices .

## Biological Role

Component of cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0430|gene.b0430]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABJ3`
- `KEGG:ecj:JW0420;eco:b0430;ecoc:C3026_02100;`
- `GeneID:93777024;946897;`
- `GO:GO:0004129; GO:0005886; GO:0009055; GO:0009060; GO:0009319; GO:0009486; GO:0015078; GO:0015453; GO:0015990; GO:0019646`

## Notes

Cytochrome bo(3) ubiquinol oxidase subunit 3 (Cytochrome o ubiquinol oxidase subunit 3) (Cytochrome o subunit 3) (Oxidase bo(3) subunit 3) (Ubiquinol oxidase chain C) (Ubiquinol oxidase polypeptide III) (Ubiquinol oxidase subunit 3)
