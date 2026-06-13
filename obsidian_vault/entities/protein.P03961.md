---
entity_id: "protein.P03961"
entity_type: "protein"
name: "kdpC"
source_database: "UniProt"
source_id: "P03961"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00276, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00276, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdpC b0696 JW0684"
---

# kdpC

`protein.P03961`

## Static

- Type: `protein`
- Source: `UniProt:P03961`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00276, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00276, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}.

## Enriched Summary

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit acts as a catalytic chaperone that increases the ATP-binding affinity of the ATP-hydrolyzing subunit KdpB by the formation of a transient KdpB/KdpC/ATP ternary complex (PubMed:21711450). {ECO:0000269|PubMed:21711450, ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:8499455}. KdpC is an inner membrane subunit of a potassium ion transporting P-type ATPase complex. A non-polar ΔkdpC strain is unable to grow under low potassium ((G116R)BC, KdpC has a single transmembrane helix and a soluble domain located on the periplasmic side of the membrane .

## Biological Role

Component of K+ transporting P-type ATPase (complex.ecocyc.ATPASE-1-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit acts as a catalytic chaperone that increases the ATP-binding affinity of the ATP-hydrolyzing subunit KdpB by the formation of a transient KdpB/KdpC/ATP ternary complex (PubMed:21711450). {ECO:0000269|PubMed:21711450, ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:8499455}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ATPASE-1-CPLX|complex.ecocyc.ATPASE-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0696|gene.b0696]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03961`
- `KEGG:ecj:JW0684;eco:b0696;ecoc:C3026_03475;`
- `GeneID:947508;`
- `GO:GO:0005524; GO:0005886; GO:0006813; GO:0008556; GO:0031004; GO:0071805; GO:0098655; GO:1903103`

## Notes

Potassium-transporting ATPase KdpC subunit (ATP phosphohydrolase [potassium-transporting] C chain) (Potassium-binding and translocating subunit C) (Potassium-translocating ATPase C chain)
