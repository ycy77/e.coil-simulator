---
entity_id: "protein.P0ABK2"
entity_type: "protein"
name: "cydB"
source_database: "UniProt"
source_id: "P0ABK2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}. Note=The displayed topology is based on (PubMed:15013751) not the large scale studies (PubMed:15919996). {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cydB cyd-2 b0734 JW0723"
---

# cydB

`protein.P0ABK2`

## Static

- Type: `protein`
- Source: `UniProt:P0ABK2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:16079137}. Note=The displayed topology is based on (PubMed:15013751) not the large scale studies (PubMed:15919996). {ECO:0000269|PubMed:15013751, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: A terminal oxidase that produces a proton motive force by the vectorial transfer of protons across the inner membrane. It is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at low aeration. Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:6307994}. cydB encodes subunit II of the cytochrome bd-I complex. Subunit II has eight predicted transmembrane helices; the N and C-termini are located in the cytoplasm ; in the bd-I complex, the subunit forms two four-helix bundles with an additional peripheral helix . Subunit I (encoded by cydA) and subunit II are both required for binding of the heme b595 and heme d components of cytochrome bd-I . In the cryo-EM structure of the bd-I complex reported by , CydB binds a structural ubiquinone-8 cofactor that may have a role in CydAB dimer assembly (see also ).

## Biological Role

Component of cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: A terminal oxidase that produces a proton motive force by the vectorial transfer of protons across the inner membrane. It is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at low aeration. Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:6307994}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0734|gene.b0734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABK2`
- `KEGG:ecj:JW0723;eco:b0734;ecoc:C3026_03680;`
- `GeneID:93776751;945347;`
- `GO:GO:0005886; GO:0006119; GO:0009055; GO:0016020; GO:0016682; GO:0019646; GO:0046872; GO:0070069`
- `EC:7.1.1.7`

## Notes

Cytochrome bd-I ubiquinol oxidase subunit 2 (EC 7.1.1.7) (Cytochrome bd-I oxidase subunit II) (Cytochrome d ubiquinol oxidase subunit II)
