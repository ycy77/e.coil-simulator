---
entity_id: "protein.P0AES9"
entity_type: "protein"
name: "hdeA"
source_database: "UniProt"
source_id: "P0AES9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00946, ECO:0000269|PubMed:17085547}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hdeA yhhC yhiB b3510 JW3478"
---

# hdeA

`protein.P0AES9`

## Static

- Type: `protein`
- Source: `UniProt:P0AES9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00946, ECO:0000269|PubMed:17085547}.

## Enriched Summary

FUNCTION: Required for optimal acid stress protection. Exhibits a chaperone-like activity only at pH below 3 by suppressing non-specifically the aggregation of denaturated periplasmic proteins. Important for survival of enteric bacteria in the acidic environment of the host stomach. Also promotes the solubilization at neutral pH of proteins that had aggregated in their presence at acidic pHs. May cooperate with other periplasmic chaperones such as DegP and SurA. {ECO:0000269|PubMed:15911614, ECO:0000269|PubMed:17085547, ECO:0000269|PubMed:18359765, ECO:0000269|PubMed:21892184}. HdeA is an energy-independent chaperone that protects periplasmic proteins from acid-induced aggregation; HdeA is an acid-activated conditionally disordered chaperone (see ). HdeA is estimated to be highly abundant in both the growth and stationary phase; HdeA appears to form multimers . hdeA is non-essential for growth in both minimal and rich media; the phenotype of hdeA insertion mutants varies depending on the specific position and/or orientation of the marker...

## Biological Role

Component of periplasmic acid stress chaperone HdeA (complex.ecocyc.CPLX0-801).

## Annotation

FUNCTION: Required for optimal acid stress protection. Exhibits a chaperone-like activity only at pH below 3 by suppressing non-specifically the aggregation of denaturated periplasmic proteins. Important for survival of enteric bacteria in the acidic environment of the host stomach. Also promotes the solubilization at neutral pH of proteins that had aggregated in their presence at acidic pHs. May cooperate with other periplasmic chaperones such as DegP and SurA. {ECO:0000269|PubMed:15911614, ECO:0000269|PubMed:17085547, ECO:0000269|PubMed:18359765, ECO:0000269|PubMed:21892184}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-801|complex.ecocyc.CPLX0-801]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3510|gene.b3510]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AES9`
- `KEGG:ecj:JW3478;eco:b3510;ecoc:C3026_19015;`
- `GeneID:93778475;948025;`
- `GO:GO:0006457; GO:0030288; GO:0042802; GO:0042803; GO:0044183; GO:0051082; GO:1990451`

## Notes

Acid stress chaperone HdeA (10K-S protein)
