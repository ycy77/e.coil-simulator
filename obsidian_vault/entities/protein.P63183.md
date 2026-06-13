---
entity_id: "protein.P63183"
entity_type: "protein"
name: "kup"
source_database: "UniProt"
source_id: "P63183"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01522, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01522}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kup trkD b3747 JW5609"
---

# kup

`protein.P63183`

## Static

- Type: `protein`
- Source: `UniProt:P63183`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01522, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01522}.

## Enriched Summary

FUNCTION: Responsible for the low-affinity transport of potassium into the cell (PubMed:10214935, PubMed:11682179, PubMed:2649491, PubMed:28522840, PubMed:8226635). Likely operates as a K(+):H(+) symporter (PubMed:10214935, PubMed:11682179). Kup is probably the major potassium uptake system upon hyper-osmotic stress at a low pH (PubMed:10214935). Can also transport Cs(+) and Rb(+) (PubMed:2649491, PubMed:28522840). In the absence of potassium, Kup-mediated Cs(+) uptake partially supports cell growth, however, at a much lower rate than with sufficient K(+) (PubMed:28522840). This effect depends on the maintenance of basal levels of intracellular K(+) by other K(+) uptake transporters (PubMed:28522840). {ECO:0000269|PubMed:10214935, ECO:0000269|PubMed:11682179, ECO:0000269|PubMed:2649491, ECO:0000269|PubMed:28522840, ECO:0000269|PubMed:8226635}. Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkD (also called Kup) and TrkA* (also called Trk)], a high affinity system (ATPASE-1-CPLX "KdpFABC") and a non-saturable system TrkF (see also . Expression of cloned kup supports growth of strain TKW4205 (kdp- trkG- trkH- kup-) at 0.1mM K+...

## Biological Role

Catalyzes K+:proton symport (reaction.ecocyc.TRANS-RXN-3). Transports Potassium cation (molecule.C00238), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Responsible for the low-affinity transport of potassium into the cell (PubMed:10214935, PubMed:11682179, PubMed:2649491, PubMed:28522840, PubMed:8226635). Likely operates as a K(+):H(+) symporter (PubMed:10214935, PubMed:11682179). Kup is probably the major potassium uptake system upon hyper-osmotic stress at a low pH (PubMed:10214935). Can also transport Cs(+) and Rb(+) (PubMed:2649491, PubMed:28522840). In the absence of potassium, Kup-mediated Cs(+) uptake partially supports cell growth, however, at a much lower rate than with sufficient K(+) (PubMed:28522840). This effect depends on the maintenance of basal levels of intracellular K(+) by other K(+) uptake transporters (PubMed:28522840). {ECO:0000269|PubMed:10214935, ECO:0000269|PubMed:11682179, ECO:0000269|PubMed:2649491, ECO:0000269|PubMed:28522840, ECO:0000269|PubMed:8226635}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-3|reaction.ecocyc.TRANS-RXN-3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3747|gene.b3747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63183`
- `KEGG:ecj:JW5609;eco:b3747;ecoc:C3026_20300;`
- `GeneID:75173981;75205465;948255;`
- `GO:GO:0005886; GO:0006813; GO:0015079; GO:0015387; GO:0016020; GO:0071278; GO:0071805`

## Notes

Low affinity potassium transport system protein Kup (Kup system potassium uptake protein)
