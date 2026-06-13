---
entity_id: "protein.P0AG80"
entity_type: "protein"
name: "ugpB"
source_database: "UniProt"
source_id: "P0AG80"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:32882062}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ugpB b3453 JW3418"
---

# ugpB

`protein.P0AG80`

## Static

- Type: `protein`
- Source: `UniProt:P0AG80`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:32882062}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). Binds G3P and glycerophosphocholine, but not glycerol-2-phosphate (PubMed:23013274). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but as it was shown later by Wuttge et al that UgpB does not bind G2P, this transport activity is questioned (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304}.; FUNCTION: In the absence of G3P, UgpB can serve as a potent molecular chaperone that exhibits anti-aggregation activity against bile salt-induced protein aggregation (PubMed:32882062). The substrate G3P, which is known to accumulate in the later compartments of the digestive system, triggers a functional switch between UgpB's activity as a molecular chaperone and its activity as a G3P transporter (PubMed:32882062)...

## Biological Role

Component of sn-glycerol 3-phosphate / glycerophosphodiester ABC transporter (complex.ecocyc.ABC-34-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). Binds G3P and glycerophosphocholine, but not glycerol-2-phosphate (PubMed:23013274). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but as it was shown later by Wuttge et al that UgpB does not bind G2P, this transport activity is questioned (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304}.; FUNCTION: In the absence of G3P, UgpB can serve as a potent molecular chaperone that exhibits anti-aggregation activity against bile salt-induced protein aggregation (PubMed:32882062). The substrate G3P, which is known to accumulate in the later compartments of the digestive system, triggers a functional switch between UgpB's activity as a molecular chaperone and its activity as a G3P transporter (PubMed:32882062). Chaperone and G3P binding activities are likely mutually exclusive activities (PubMed:32882062). {ECO:0000269|PubMed:32882062}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-34-CPLX|complex.ecocyc.ABC-34-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3453|gene.b3453]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG80`
- `KEGG:ecj:JW3418;eco:b3453;ecoc:C3026_18700;`
- `GeneID:75059967;947962;`
- `GO:GO:0001407; GO:0015794; GO:0016020; GO:0022857; GO:0030288; GO:1902517`

## Notes

sn-glycerol-3-phosphate-binding periplasmic protein UgpB (Bile-responsive chaperone)
