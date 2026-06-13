---
entity_id: "protein.P69874"
entity_type: "protein"
name: "potA"
source_database: "UniProt"
source_id: "P69874"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:7592703}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:7592703}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potA b1126 JW1112"
---

# potA

`protein.P69874`

## Static

- Type: `protein`
- Source: `UniProt:P69874`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:7592703}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:7592703}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PotABCD involved in spermidine/putrescine import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:2249996, ECO:0000269|PubMed:8366082}. PotA is the ATP-binding subunit of a high affinity spermidine uptake system. PotA contains signature motifs conserved in ATP-binding cassette (ABC) proteins . PotA binds nucleotides with the following specificity: ATP>GTP=ADP>CTP=UTP . PotA associates with the membrane through its interaction with PotB and PotC; purified PotA has Mg2+ dependent ATPase activity which is inhibited by spermidine and spermine but not by putrescine; the C-terminal domain of PotA (residues 251-378) may contain a spermidine binding site which is involved in regulation of its ATPase activity . PotA is able to form dimers but each PotA subunit appears to function independently (no cooperativity for ATP during ATP hydrolysis)

## Biological Role

Component of spermidine preferential ABC transporter (complex.ecocyc.ABC-24-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PotABCD involved in spermidine/putrescine import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:2249996, ECO:0000269|PubMed:8366082}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1126|gene.b1126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69874`
- `KEGG:ecj:JW1112;eco:b1126;ecoc:C3026_06775;`
- `GeneID:75203712;946323;`
- `GO:GO:0000166; GO:0005524; GO:0005886; GO:0015417; GO:0015594; GO:0015847; GO:0016020; GO:0016887; GO:0043190; GO:1903711`
- `EC:7.6.2.11`

## Notes

Spermidine/putrescine import ATP-binding protein PotA (EC 7.6.2.11)
