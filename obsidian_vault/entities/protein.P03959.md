---
entity_id: "protein.P03959"
entity_type: "protein"
name: "kdpA"
source_database: "UniProt"
source_id: "P03959"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00275, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:7896809}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00275, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:7896809}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdpA b0698 JW0686"
---

# kdpA

`protein.P03959`

## Static

- Type: `protein`
- Source: `UniProt:P03959`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00275, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:7896809}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00275, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:7896809}.

## Enriched Summary

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit binds the periplasmic potassium ions and delivers the ions to the membrane domain of KdpB through an intramembrane tunnel (PubMed:30478378, PubMed:34272288, PubMed:7896809). {ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:34272288, ECO:0000269|PubMed:7896809, ECO:0000269|PubMed:8499455}. KdpA is an innner membrane subunit of the potassium ion importing Kdp ATPase ; KdpA contains 12 predicted transmembrane regions and forms the K+ transporting channel of the complex; both periplasmic and cytoplasmic K+ binding sites have been identified . More recently, cryo-EM structures of the KdpFABC complex suggest a translocation pathway for K+ via KdpA and KdpB half-channels (and further ). KdpA contains 4 M1-P-M2 (MPM) transmembrane motifs and may be homologous to the transmembrane subunits of K+ symporters . In the crystal structure of KdpFA(G116R)BC, KdpA contains 10 transmembrane regions and a K+ ion is bound within a 'central selectivity filter' .

## Biological Role

Component of K+ transporting P-type ATPase (complex.ecocyc.ATPASE-1-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit binds the periplasmic potassium ions and delivers the ions to the membrane domain of KdpB through an intramembrane tunnel (PubMed:30478378, PubMed:34272288, PubMed:7896809). {ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:34272288, ECO:0000269|PubMed:7896809, ECO:0000269|PubMed:8499455}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ATPASE-1-CPLX|complex.ecocyc.ATPASE-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0698|gene.b0698]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03959`
- `KEGG:ecj:JW0686;eco:b0698;ecoc:C3026_03485;`
- `GeneID:946045;`
- `GO:GO:0005886; GO:0006813; GO:0008556; GO:0030955; GO:0031004; GO:0071805; GO:0098655; GO:1903103`

## Notes

Potassium-transporting ATPase potassium-binding subunit (ATP phosphohydrolase [potassium-transporting] A chain) (Potassium-binding and translocating subunit A) (Potassium-translocating ATPase A chain)
