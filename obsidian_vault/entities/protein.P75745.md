---
entity_id: "protein.P75745"
entity_type: "protein"
name: "pxpC"
source_database: "UniProt"
source_id: "P75745"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pxpC ybgK b0712 JW0702"
---

# pxpC

`protein.P75745`

## Static

- Type: `protein`
- Source: `UniProt:P75745`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000269|PubMed:28830929}. Overexpression of pxpBCA leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpC deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . PxpC: "prokaryotic 5-oxoprolinase C"

## Biological Role

Catalyzes 5-oxo-L-proline amidohydrolase (ATP-hydrolysing) (reaction.R00251). Component of 5-oxoprolinase (complex.ecocyc.CPLX0-8249).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000269|PubMed:28830929}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00251|reaction.R00251]] `KEGG` `database` - via EC:3.5.2.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-8249|complex.ecocyc.CPLX0-8249]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0712|gene.b0712]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75745`
- `KEGG:ecj:JW0702;eco:b0712;ecoc:C3026_03560;`
- `GeneID:945317;`
- `GO:GO:0005524; GO:0005829; GO:0017168`
- `EC:3.5.2.9`

## Notes

5-oxoprolinase subunit C (5-OPase subunit C) (EC 3.5.2.9) (5-oxoprolinase (ATP-hydrolyzing) subunit C)
