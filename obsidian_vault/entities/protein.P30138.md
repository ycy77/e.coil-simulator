---
entity_id: "protein.P30138"
entity_type: "protein"
name: "thiF"
source_database: "UniProt"
source_id: "P30138"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiF b3992 JW3956"
---

# thiF

`protein.P30138`

## Static

- Type: `protein`
- Source: `UniProt:P30138`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the adenylation by ATP of the carboxyl group of the C-terminal glycine of sulfur carrier protein ThiS.

## Biological Role

Component of sulfur carrier protein ThiS adenylyltransferase (complex.ecocyc.CPLX0-8558).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the adenylation by ATP of the carboxyl group of the C-terminal glycine of sulfur carrier protein ThiS.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8558|complex.ecocyc.CPLX0-8558]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3992|gene.b3992]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30138`
- `KEGG:ecj:JW3956;eco:b3992;ecoc:C3026_21565;`
- `GeneID:75205510;948500;`
- `GO:GO:0004792; GO:0005524; GO:0005737; GO:0005829; GO:0008146; GO:0008270; GO:0008641; GO:0009228; GO:0009229; GO:0016779; GO:0042803; GO:0052837; GO:0070733; GO:1902503; GO:1990228`
- `EC:2.7.7.73`

## Notes

Sulfur carrier protein ThiS adenylyltransferase (EC 2.7.7.73)
