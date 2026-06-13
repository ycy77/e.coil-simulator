---
entity_id: "protein.P36937"
entity_type: "protein"
name: "kdpF"
source_database: "UniProt"
source_id: "P36937"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378, ECO:0000305|PubMed:10608856}; Single-pass membrane protein {ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdpF b4513 JW0687"
---

# kdpF

`protein.P36937`

## Static

- Type: `protein`
- Source: `UniProt:P36937`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378, ECO:0000305|PubMed:10608856}; Single-pass membrane protein {ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}.

## Enriched Summary

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894). This subunit may be involved in stabilization of the complex (PubMed:10608856). {ECO:0000269|PubMed:10608856, ECO:0000269|PubMed:23930894}. KdpF is a small membrane protein that is part of a potassium ion transporting P-type ATPase complex. KdpF may function to stabilise the transporter complex; inactivation of kdpF does not affect growth under low potassium conditions (0.1 mM K+) however the purified complex lacking KdpF exhibits significantly decreased K+-stimulated ATPase activity; addition of purified KdpF restores K+-stimulated ATPase activity to near wild type levels, as does the addition of E. coli lipids . KdpF is predicted to be a bitopic inner membrane protein .

## Biological Role

Component of K+ transporting P-type ATPase (complex.ecocyc.ATPASE-1-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894). This subunit may be involved in stabilization of the complex (PubMed:10608856). {ECO:0000269|PubMed:10608856, ECO:0000269|PubMed:23930894}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ATPASE-1-CPLX|complex.ecocyc.ATPASE-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4513|gene.b4513]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36937`
- `KEGG:ecj:JW0687;eco:b4513;ecoc:C3026_03490;`
- `GeneID:86945573;948946;`
- `GO:GO:0005886; GO:0006813; GO:0008556; GO:0031004; GO:0071805; GO:0098655; GO:1903103`

## Notes

Potassium-transporting ATPase KdpF subunit (ATP phosphohydrolase [potassium-transporting] F chain) (Potassium-binding and translocating subunit F) (Potassium-translocating ATPase F chain)
