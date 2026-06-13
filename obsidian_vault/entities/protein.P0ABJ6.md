---
entity_id: "protein.P0ABJ6"
entity_type: "protein"
name: "cyoD"
source_database: "UniProt"
source_id: "P0ABJ6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cyoD b0429 JW0419"
---

# cyoD

`protein.P0ABJ6`

## Static

- Type: `protein`
- Source: `UniProt:P0ABJ6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. CyoD is subunit IV of the cytochrome bo3 complex. Subunit IV is required for a functional complex but its exact contribution remains uncertain The CyoD polypeptide contains three transmembrane helices . Deletion and cross-linking studies have suggested that subunit IV interacts with subunits I and III , which is confirmed by the crystal structure of the entire cytochrome bo terminal oxidase complex . cyoD belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

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

- `encodes` <-- [[gene.b0429|gene.b0429]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABJ6`
- `KEGG:ecj:JW0419;eco:b0429;ecoc:C3026_02095;`
- `GeneID:93777025;944918;`
- `GO:GO:0005886; GO:0009055; GO:0009060; GO:0009319; GO:0009486; GO:0015078; GO:0015453; GO:0015990; GO:0019646`

## Notes

Cytochrome bo(3) ubiquinol oxidase subunit 4 (Cytochrome o ubiquinol oxidase subunit 4) (Cytochrome o subunit 4) (Oxidase bo(3) subunit 4) (Ubiquinol oxidase chain D) (Ubiquinol oxidase polypeptide IV) (Ubiquinol oxidase subunit 4)
