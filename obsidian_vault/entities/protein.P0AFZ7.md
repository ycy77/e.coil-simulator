---
entity_id: "protein.P0AFZ7"
entity_type: "protein"
name: "trkH"
source_database: "UniProt"
source_id: "P0AFZ7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trkH b3849 JW5576"
---

# trkH

`protein.P0AFZ7`

## Static

- Type: `protein`
- Source: `UniProt:P0AFZ7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Low-affinity potassium transport system. Interacts with Trk system potassium uptake protein TrkA. Requires TrkE (sapD) for transport activity, 20% more uptake is seen with both SapD and SapF (PubMed:11700350). Transport in the absence of SapD and SapF is dependent on a high membrane potential and a high cytoplasmic ATP concentration, suggesting this protein may be able to interact with other ATP-binding proteins (PubMed:11700350). Can transport potassium and rubidium (PubMed:7896723). {ECO:0000250, ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:7896723}. TrkH is a Na+-independent potassium ion transporter that functions as a major K+-uptake system; TrkH-mediated potassium uptake is able to support growth in low K+ medium (0.1mM K+) in the absence of other potassium uptake systems . Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkA (also called Trk) and TrkD (also called Kup)], a high affinity system (Kdp) and a non-saturable system TrkF (see also . Although initially thought to be a single system TrkA/Trk activity was later shown to result from the activity of two K+ transporters which were named TRKG-MONOMER "TrkG" and TRKH-MONOMER "TrkH" . trkG trkH double null mutations abolish saturable K+ uptake in a strain lacking ATPASE-1-CPLX "Kdp" and KUP-MONOMER "TrkD" mediated potassium transport...

## Biological Role

Catalyzes K+:proton symport (reaction.ecocyc.TRANS-RXN-3).

## Annotation

FUNCTION: Low-affinity potassium transport system. Interacts with Trk system potassium uptake protein TrkA. Requires TrkE (sapD) for transport activity, 20% more uptake is seen with both SapD and SapF (PubMed:11700350). Transport in the absence of SapD and SapF is dependent on a high membrane potential and a high cytoplasmic ATP concentration, suggesting this protein may be able to interact with other ATP-binding proteins (PubMed:11700350). Can transport potassium and rubidium (PubMed:7896723). {ECO:0000250, ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:7896723}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-3|reaction.ecocyc.TRANS-RXN-3]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3849|gene.b3849]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFZ7`
- `KEGG:ecj:JW5576;eco:b3849;ecoc:C3026_20810;`
- `GeneID:93778088;948333;`
- `GO:GO:0005267; GO:0005886; GO:0015079; GO:0015379; GO:0030955; GO:0071805`

## Notes

Trk system potassium uptake protein TrkH
