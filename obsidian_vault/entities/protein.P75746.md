---
entity_id: "protein.P75746"
entity_type: "protein"
name: "pxpA"
source_database: "UniProt"
source_id: "P75746"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pxpA ybgL b0713 JW0703"
---

# pxpA

`protein.P75746`

## Static

- Type: `protein`
- Source: `UniProt:P75746`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000255|HAMAP-Rule:MF_00691, ECO:0000269|PubMed:28830929}. Overexpression of pxpBCA leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpA deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . While wild-type E. coli shows significantly decreased swarming motility upon exposure to volatile organic compounds (VOCs) produced by Bacillus subtilis, a pxpA null mutant shows no significant difference in swarming motility upon VOC treatment . PxpA: "prokaryotic 5-oxoprolinase A"

## Biological Role

Catalyzes 5-oxo-L-proline amidohydrolase (ATP-hydrolysing) (reaction.R00251). Component of 5-oxoprolinase (complex.ecocyc.CPLX0-8249).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000255|HAMAP-Rule:MF_00691, ECO:0000269|PubMed:28830929}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00251|reaction.R00251]] `KEGG` `database` - via EC:3.5.2.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-8249|complex.ecocyc.CPLX0-8249]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0713|gene.b0713]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75746`
- `KEGG:ecj:JW0703;eco:b0713;ecoc:C3026_03565;`
- `GeneID:945318;`
- `GO:GO:0005524; GO:0005975; GO:0017168`
- `EC:3.5.2.9`

## Notes

5-oxoprolinase subunit A (5-OPase subunit A) (EC 3.5.2.9) (5-oxoprolinase (ATP-hydrolyzing) subunit A)
