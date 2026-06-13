---
entity_id: "protein.P10907"
entity_type: "protein"
name: "ugpC"
source_database: "UniProt"
source_id: "P10907"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01727, ECO:0000305}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01727, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ugpC b3450 JW3415"
---

# ugpC

`protein.P10907`

## Static

- Type: `protein`
- Source: `UniProt:P10907`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01727, ECO:0000305}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01727, ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304, PubMed:363686, PubMed:7042685, PubMed:8282692). Responsible for energy coupling to the transport system (Probable). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but it was shown later by Wuttge et al that UgpB does not bind G2P, questioning this transport activity (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304, ECO:0000269|PubMed:363686, ECO:0000269|PubMed:7042685, ECO:0000269|PubMed:8282692, ECO:0000305}. UgpC is the predicted ATP binding subunit of an sn-glycerol 3-phosphate ABC importer . UgpC contains signature motifs conserved in ABC domains

## Biological Role

Component of sn-glycerol 3-phosphate / glycerophosphodiester ABC transporter (complex.ecocyc.ABC-34-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304, PubMed:363686, PubMed:7042685, PubMed:8282692). Responsible for energy coupling to the transport system (Probable). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but it was shown later by Wuttge et al that UgpB does not bind G2P, questioning this transport activity (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304, ECO:0000269|PubMed:363686, ECO:0000269|PubMed:7042685, ECO:0000269|PubMed:8282692, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-34-CPLX|complex.ecocyc.ABC-34-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3450|gene.b3450]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10907`
- `KEGG:ecj:JW3415;eco:b3450;ecoc:C3026_18685;`
- `GeneID:947953;`
- `GO:GO:0001406; GO:0001407; GO:0005524; GO:0008643; GO:0015169; GO:0015430; GO:0015794; GO:0016020; GO:0016887; GO:0055052; GO:1902517`
- `EC:7.6.2.10`

## Notes

sn-glycerol-3-phosphate import ATP-binding protein UgpC (EC 7.6.2.10)
