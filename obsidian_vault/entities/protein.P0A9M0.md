---
entity_id: "protein.P0A9M0"
entity_type: "protein"
name: "lon"
source_database: "UniProt"
source_id: "P0A9M0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lon capR deg lopA muc b0439 JW0429"
---

# lon

`protein.P0A9M0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9M0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: ATP-dependent serine protease that mediates the selective degradation of mutant and abnormal proteins as well as certain short-lived regulatory proteins, including some antitoxins. Required for cellular homeostasis and for survival from DNA damage and developmental changes induced by stress. Degrades polypeptides processively to yield small peptide fragments that are 5 to 10 amino acids long. Binds to DNA in a double-stranded, site-specific manner. Endogenous substrates include the regulatory proteins RcsA and SulA, the transcriptional activator SoxS, UmuD and at least type II antitoxins CcdA, HipB and MazE (PubMed:16460757, PubMed:22720069, PubMed:24375411, PubMed:8022284). Its overproduction specifically inhibits translation through at least two different pathways, one of them being the YoeB-YefM toxin-antitoxin system (PubMed:15009896). {ECO:0000269|PubMed:12135363, ECO:0000269|PubMed:15009896, ECO:0000269|PubMed:16460757, ECO:0000269|PubMed:16584195, ECO:0000269|PubMed:19721064, ECO:0000269|PubMed:22720069, ECO:0000269|PubMed:24375411, ECO:0000269|PubMed:8022284}.

## Biological Role

Component of Lon protease (complex.ecocyc.CPLX0-2881).

## Annotation

FUNCTION: ATP-dependent serine protease that mediates the selective degradation of mutant and abnormal proteins as well as certain short-lived regulatory proteins, including some antitoxins. Required for cellular homeostasis and for survival from DNA damage and developmental changes induced by stress. Degrades polypeptides processively to yield small peptide fragments that are 5 to 10 amino acids long. Binds to DNA in a double-stranded, site-specific manner. Endogenous substrates include the regulatory proteins RcsA and SulA, the transcriptional activator SoxS, UmuD and at least type II antitoxins CcdA, HipB and MazE (PubMed:16460757, PubMed:22720069, PubMed:24375411, PubMed:8022284). Its overproduction specifically inhibits translation through at least two different pathways, one of them being the YoeB-YefM toxin-antitoxin system (PubMed:15009896). {ECO:0000269|PubMed:12135363, ECO:0000269|PubMed:15009896, ECO:0000269|PubMed:16460757, ECO:0000269|PubMed:16584195, ECO:0000269|PubMed:19721064, ECO:0000269|PubMed:22720069, ECO:0000269|PubMed:24375411, ECO:0000269|PubMed:8022284}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2881|complex.ecocyc.CPLX0-2881]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0439|gene.b0439]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9M0`
- `KEGG:ecj:JW0429;eco:b0439;ecoc:C3026_02150;`
- `GeneID:86862984;93777015;945085;`
- `GO:GO:0003677; GO:0004176; GO:0004252; GO:0005524; GO:0005737; GO:0005829; GO:0006508; GO:0006515; GO:0008233; GO:0009408; GO:0010165; GO:0016887; GO:0034605; GO:0043565`
- `EC:3.4.21.53`

## Notes

Lon protease (EC 3.4.21.53) (ATP-dependent protease La)
