---
entity_id: "protein.P0AAV4"
entity_type: "protein"
name: "pxpB"
source_database: "UniProt"
source_id: "P0AAV4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pxpB ybgJ b0711 JW0701"
---

# pxpB

`protein.P0AAV4`

## Static

- Type: `protein`
- Source: `UniProt:P0AAV4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000269|PubMed:28830929}. Overexpression of pxpBCA leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpB deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . A ΔpxpB mutant has aggravating genetic interactions with genes involved in DNA recombination . PxpB: "prokaryotic 5-oxoprolinase B"

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

- `encodes` <-- [[gene.b0711|gene.b0711]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAV4`
- `KEGG:ecj:JW0701;eco:b0711;ecoc:C3026_03555;`
- `GeneID:75170700;945311;`
- `GO:GO:0005524; GO:0017168`
- `EC:3.5.2.9`

## Notes

5-oxoprolinase subunit B (5-OPase subunit B) (EC 3.5.2.9) (5-oxoprolinase (ATP-hydrolyzing) subunit B)
