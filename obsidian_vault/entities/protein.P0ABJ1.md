---
entity_id: "protein.P0ABJ1"
entity_type: "protein"
name: "cyoA"
source_database: "UniProt"
source_id: "P0ABJ1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:6365921}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:6365921}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cyoA b0432 JW0422"
---

# cyoA

`protein.P0ABJ1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABJ1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:6365921}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:6365921}.

## Enriched Summary

FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. CyoA is subunit II of the 4 subunit cytochrome bo complex. CyoA was initially suggested to contain one of two ubiquinone binding sites; current work suggests that the complex contains only one binding site located in subunit I (CyoB) . CyoA consists of two domains - an N terminal domain containing two transmembrane helices and a large C-terminal domain located in the periplasm . CyoA is a lipoprotein; during maturation, the protein is modified by attachment of fatty acids and protease cleavage at C25. The addition of [14C]palmitic acid to the growth medium results in covalent labeling of CyoA with the fatty acid. A C25A mutation blocks lipoprotein processing but the protein retains oxidase activity suggesting that posttranslational modification is not essential for assembly or activity of the cytochrome bo terminal oxidase complex . YIDC "YidC", the Sec translocon (SECE-G-Y-CPLX "SecYEG") and CPLX0-8089 "SecA" are required for efficient insertion of cyoA into proteoliposomes...

## Biological Role

Catalyzes ubiquinol:oxygen oxidoreductase (H+-transporting) (reaction.R11335). Component of cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11335|reaction.R11335]] `KEGG` `database` - via EC:7.1.1.3
- `is_component_of` --> [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0432|gene.b0432]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABJ1`
- `KEGG:ecj:JW0422;eco:b0432;ecoc:C3026_02110;`
- `GeneID:86862977;945080;`
- `GO:GO:0004129; GO:0005507; GO:0005886; GO:0009055; GO:0009060; GO:0009319; GO:0009486; GO:0015078; GO:0015453; GO:0015990; GO:0016682; GO:0019646; GO:0042773; GO:0098803`

## Notes

Cytochrome bo(3) ubiquinol oxidase subunit 2 (Cytochrome b562-o complex subunit II) (Cytochrome o ubiquinol oxidase subunit 2) (Cytochrome o subunit 2) (Oxidase bo(3) subunit 2) (Ubiquinol oxidase chain B) (Ubiquinol oxidase polypeptide II) (Ubiquinol oxidase subunit 2)
