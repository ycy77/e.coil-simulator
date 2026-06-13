---
entity_id: "protein.P0ABJ9"
entity_type: "protein"
name: "cydA"
source_database: "UniProt"
source_id: "P0ABJ9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cydA cyd-1 b0733 JW0722"
---

# cydA

`protein.P0ABJ9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABJ9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: A terminal oxidase that produces a proton motive force by the vectorial transfer of protons across the inner membrane. It is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at low aeration. Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:2656671, ECO:0000269|PubMed:6307994, ECO:0000269|PubMed:7577938}. cydA encodes subunit I of the cytochrome bd-I complex; it contains all three heme cofactors (heme b558, heme b595 and heme d) and is the site of ubiquinol oxidation and oxygen reduction . CydA contains the heme b558 component of cytochrome bd-I and is the site of ubiquinol oxidation . Purified, reconstituted CydA can be reduced by ubiquinol but it does not reduce molecular oxygen . The CydA protein has nine transmembrane helices, the N-terminus is located in the periplasm and the C-terminus in the cytoplasm ; in the bd-I complex, the subunit forms two four-helix bundles with an additional peripheral helix (see also ). A dynamic periplasmic loop (the Q-loop) located between transmembrane regions VI and VII is implicated in ubiquinol binding (further )...

## Biological Role

Component of cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: A terminal oxidase that produces a proton motive force by the vectorial transfer of protons across the inner membrane. It is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at low aeration. Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:2656671, ECO:0000269|PubMed:6307994, ECO:0000269|PubMed:7577938}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0733|gene.b0733]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABJ9`
- `KEGG:ecj:JW0722;eco:b0733;ecoc:C3026_03675;`
- `GeneID:93776752;945341;`
- `GO:GO:0005886; GO:0006119; GO:0009055; GO:0016020; GO:0016679; GO:0016682; GO:0019646; GO:0020037; GO:0046872; GO:0070069`
- `EC:7.1.1.7`

## Notes

Cytochrome bd-I ubiquinol oxidase subunit 1 (EC 7.1.1.7) (Cytochrome bd-I oxidase subunit I) (Cytochrome d ubiquinol oxidase subunit I)
