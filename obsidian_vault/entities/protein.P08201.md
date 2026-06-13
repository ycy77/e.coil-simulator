---
entity_id: "protein.P08201"
entity_type: "protein"
name: "nirB"
source_database: "UniProt"
source_id: "P08201"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nirB b3365 JW3328"
---

# nirB

`protein.P08201`

## Static

- Type: `protein`
- Source: `UniProt:P08201`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Nitrite reductase (NADH) large subunit (EC 1.7.1.15) nirB encodes the catalytic subunit of nitrite reductase . Expression of nirB is downregulated in response to cobalt and upregulated upon exposure to silver nanoparticles . NirB: "nitrite reductase"

## Biological Role

Catalyzes ammonia:NAD+ oxidoreductase (reaction.R00787). Component of nitrite reductase - NADH dependent (complex.ecocyc.NITRITREDUCT-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

Nitrite reductase (NADH) large subunit (EC 1.7.1.15)

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00787|reaction.R00787]] `KEGG` `database` - via EC:1.7.1.15
- `is_component_of` --> [[complex.ecocyc.NITRITREDUCT-CPLX|complex.ecocyc.NITRITREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3365|gene.b3365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08201`
- `KEGG:ecj:JW3328;eco:b3365;ecoc:C3026_18275;`
- `GeneID:947868;`
- `GO:GO:0006113; GO:0009344; GO:0016491; GO:0020037; GO:0042128; GO:0046872; GO:0050660; GO:0050661; GO:0051537; GO:0051539; GO:0106316`
- `EC:1.7.1.15`

## Notes

Nitrite reductase (NADH) large subunit (EC 1.7.1.15)
