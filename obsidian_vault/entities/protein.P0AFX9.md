---
entity_id: "protein.P0AFX9"
entity_type: "protein"
name: "rseB"
source_database: "UniProt"
source_id: "P0AFX9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11777003, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}. Note=Partially associates with the inner membrane via RseA."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rseB b2571 JW2555"
---

# rseB

`protein.P0AFX9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFX9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11777003, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}. Note=Partially associates with the inner membrane via RseA.

## Enriched Summary

FUNCTION: Negatively modulates the activity of sigma-E (RpoE) by stabilizing RseA under non-stress conditions. Although not essential for association of sigma-E with Rsea it increases their affinity 2- to 3-fold. When bound to RseA it prevents proteolysis by DegS, which is probably relieved by lipopolysaccharide binding (LPS). {ECO:0000269|PubMed:10500101, ECO:0000269|PubMed:17360428, ECO:0000269|PubMed:21245315, ECO:0000269|PubMed:23687042, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}.

## Biological Role

Component of anti-sigma factor stabilizing protein RseB (complex.ecocyc.CPLX0-7648).

## Annotation

FUNCTION: Negatively modulates the activity of sigma-E (RpoE) by stabilizing RseA under non-stress conditions. Although not essential for association of sigma-E with Rsea it increases their affinity 2- to 3-fold. When bound to RseA it prevents proteolysis by DegS, which is probably relieved by lipopolysaccharide binding (LPS). {ECO:0000269|PubMed:10500101, ECO:0000269|PubMed:17360428, ECO:0000269|PubMed:21245315, ECO:0000269|PubMed:23687042, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7648|complex.ecocyc.CPLX0-7648]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2571|gene.b2571]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFX9`
- `KEGG:ecj:JW2555;eco:b2571;ecoc:C3026_14240;`
- `GeneID:75172685;75206265;947054;`
- `GO:GO:0005886; GO:0008289; GO:0030288; GO:0032885; GO:0042802; GO:0045152; GO:0045892; GO:0050821; GO:1903865`

## Notes

Sigma-E factor regulatory protein RseB
