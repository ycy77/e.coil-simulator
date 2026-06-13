---
entity_id: "protein.P02943"
entity_type: "protein"
name: "lamB"
source_database: "UniProt"
source_id: "P02943"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01301, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:1988451, ECO:0000269|PubMed:4201774, ECO:0000269|Ref.9}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01301, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lamB malB b4036 JW3996"
---

# lamB

`protein.P02943`

## Static

- Type: `protein`
- Source: `UniProt:P02943`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01301, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:1988451, ECO:0000269|PubMed:4201774, ECO:0000269|Ref.9}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01301, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Involved in the transport of maltose and maltodextrins (PubMed:11742115, PubMed:2832377, PubMed:3301537, PubMed:7824948, PubMed:8805519, PubMed:9299337). Indispensable for translocation of maltodextrins (alpha 1-4 linked polyglucosyls) containing more than three glucosyl moieties. A hydrophobic path ('greasy slide') of aromatic residues serves to guide and select the sugars for transport through the channel (PubMed:11742115, PubMed:7824948, PubMed:8805519, PubMed:9299337). Also acts as a receptor for several bacteriophages including lambda (PubMed:4201774). Binds maltosaccharides; when LamB binds starch in soft agar, it inhibits motility (PubMed:2832377). {ECO:0000269|PubMed:11742115, ECO:0000269|PubMed:2832377, ECO:0000269|PubMed:3301537, ECO:0000269|PubMed:4201774, ECO:0000269|PubMed:7824948, ECO:0000269|PubMed:8805519, ECO:0000269|PubMed:9299337}.

## Biological Role

Component of maltose outer membrane channel / phage lambda receptor protein (complex.ecocyc.CPLX0-7655).

## Annotation

FUNCTION: Involved in the transport of maltose and maltodextrins (PubMed:11742115, PubMed:2832377, PubMed:3301537, PubMed:7824948, PubMed:8805519, PubMed:9299337). Indispensable for translocation of maltodextrins (alpha 1-4 linked polyglucosyls) containing more than three glucosyl moieties. A hydrophobic path ('greasy slide') of aromatic residues serves to guide and select the sugars for transport through the channel (PubMed:11742115, PubMed:7824948, PubMed:8805519, PubMed:9299337). Also acts as a receptor for several bacteriophages including lambda (PubMed:4201774). Binds maltosaccharides; when LamB binds starch in soft agar, it inhibits motility (PubMed:2832377). {ECO:0000269|PubMed:11742115, ECO:0000269|PubMed:2832377, ECO:0000269|PubMed:3301537, ECO:0000269|PubMed:4201774, ECO:0000269|PubMed:7824948, ECO:0000269|PubMed:8805519, ECO:0000269|PubMed:9299337}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7655|complex.ecocyc.CPLX0-7655]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b4036|gene.b4036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02943`
- `KEGG:ecj:JW3996;eco:b4036;ecoc:C3026_21810;`
- `GeneID:948548;`
- `GO:GO:0001618; GO:0005363; GO:0006811; GO:0006974; GO:0009279; GO:0015144; GO:0015288; GO:0015481; GO:0015774; GO:0042956; GO:0042958; GO:0046930; GO:0106234; GO:1904981`

## Notes

Maltoporin (Maltose outer membrane channel) (Maltose-inducible porin) (Phage lambda receptor protein)
