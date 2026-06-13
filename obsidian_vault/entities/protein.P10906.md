---
entity_id: "protein.P10906"
entity_type: "protein"
name: "ugpE"
source_database: "UniProt"
source_id: "P10906"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ugpE b3451 JW3416"
---

# ugpE

`protein.P10906`

## Static

- Type: `protein`
- Source: `UniProt:P10906`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304). Probably responsible for the translocation of the substrate across the membrane (Probable). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but it was shown later by Wuttge et al that UgpB does not bind G2P, questioning this transport activity (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304, ECO:0000305}. ugpE encodes one of two predicted inner membrane subunits of an sn-glycerol 3-phosphate and glycerophosphodiester ABC importer.

## Biological Role

Component of sn-glycerol 3-phosphate / glycerophosphodiester ABC transporter (complex.ecocyc.ABC-34-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304). Probably responsible for the translocation of the substrate across the membrane (Probable). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but it was shown later by Wuttge et al that UgpB does not bind G2P, questioning this transport activity (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-34-CPLX|complex.ecocyc.ABC-34-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3451|gene.b3451]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10906`
- `KEGG:ecj:JW3416;eco:b3451;ecoc:C3026_18690;`
- `GeneID:947959;`
- `GO:GO:0005886; GO:0015169; GO:0015794; GO:0016020; GO:0055052; GO:1902517`

## Notes

sn-glycerol-3-phosphate transport system permease protein UgpE
