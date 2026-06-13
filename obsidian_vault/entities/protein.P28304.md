---
entity_id: "protein.P28304"
entity_type: "protein"
name: "qorA"
source_database: "UniProt"
source_id: "P28304"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "qorA hcz qor qor1 b4051 JW4011"
---

# qorA

`protein.P28304`

## Static

- Type: `protein`
- Source: `UniProt:P28304`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Quinone oxidoreductase 1 (EC 1.6.5.5) (NADPH:quinone reductase 1) (Zeta-crystallin homolog protein) QorA is a putative NADPH-dependent quinone oxidoreductase that is structurally similar to Thermoplasma acidophilum glucose dehydrogenase and horse liver alcohol dehydrogenase . The enzyme has not been biochemically characterized. A crystal structure of the enzyme has been solved at 2.2 Å resolution . QorA may have physiologically relevant G7276 yffO mRNA binding activity .

## Biological Role

Catalyzes NADPH2:quinone oxidoreductase (reaction.R02364). Component of putative quinone oxidoreductase 1 (complex.ecocyc.QOR-CPLX).

## Annotation

Quinone oxidoreductase 1 (EC 1.6.5.5) (NADPH:quinone reductase 1) (Zeta-crystallin homolog protein)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02364|reaction.R02364]] `KEGG` `database` - via EC:1.6.5.5
- `is_component_of` --> [[complex.ecocyc.QOR-CPLX|complex.ecocyc.QOR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4051|gene.b4051]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28304`
- `KEGG:ecj:JW4011;eco:b4051;ecoc:C3026_21890;`
- `GeneID:948556;`
- `GO:GO:0003960; GO:0005829; GO:0008270; GO:0035925; GO:0042803; GO:0070402`
- `EC:1.6.5.5`

## Notes

Quinone oxidoreductase 1 (EC 1.6.5.5) (NADPH:quinone reductase 1) (Zeta-crystallin homolog protein)
