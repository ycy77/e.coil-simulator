---
entity_id: "protein.P0A8A4"
entity_type: "protein"
name: "ppsR"
source_database: "UniProt"
source_id: "P0A8A4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppsR ydiA b1703 JW1693"
---

# ppsR

`protein.P0A8A4`

## Static

- Type: `protein`
- Source: `UniProt:P0A8A4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Bifunctional serine/threonine kinase and phosphorylase involved in the regulation of the phosphoenolpyruvate synthase (PEPS) by catalyzing its phosphorylation/dephosphorylation. {ECO:0000255|HAMAP-Rule:MF_01062, ECO:0000269|PubMed:20044937}.

## Biological Role

Component of phosphoenolpyruvate synthetase regulatory protein (complex.ecocyc.CPLX0-7837).

## Annotation

FUNCTION: Bifunctional serine/threonine kinase and phosphorylase involved in the regulation of the phosphoenolpyruvate synthase (PEPS) by catalyzing its phosphorylation/dephosphorylation. {ECO:0000255|HAMAP-Rule:MF_01062, ECO:0000269|PubMed:20044937}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7837|complex.ecocyc.CPLX0-7837]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1703|gene.b1703]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8A4`
- `KEGG:ecj:JW1693;eco:b1703;ecoc:C3026_09755;`
- `GeneID:93775866;946207;`
- `GO:GO:0004672; GO:0004674; GO:0004721; GO:0005524; GO:0005829; GO:0016776; GO:0030234; GO:0043531`
- `EC:2.7.11.33; 2.7.4.28`

## Notes

Phosphoenolpyruvate synthase regulatory protein (PEP synthase regulatory protein) (PSRP) (EC 2.7.11.33) (EC 2.7.4.28) (Pyruvate, water dikinase regulatory protein)
