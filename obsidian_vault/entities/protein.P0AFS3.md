---
entity_id: "protein.P0AFS3"
entity_type: "protein"
name: "folM"
source_database: "UniProt"
source_id: "P0AFS3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folM ydgB b1606 JW1598"
---

# folM

`protein.P0AFS3`

## Static

- Type: `protein`
- Source: `UniProt:P0AFS3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of dihydromonapterin to tetrahydromonapterin. Also has lower activity with dihydrofolate. {ECO:0000269|PubMed:19897652}.

## Biological Role

Component of dihydromonapterin reductase (complex.ecocyc.CPLX0-8571).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of dihydromonapterin to tetrahydromonapterin. Also has lower activity with dihydrofolate. {ECO:0000269|PubMed:19897652}.

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8571|complex.ecocyc.CPLX0-8571]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1606|gene.b1606]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFS3`
- `KEGG:ecj:JW1598;eco:b1606;ecoc:C3026_09245;`
- `GeneID:949096;`
- `GO:GO:0004146; GO:0006730; GO:0009257; GO:0016491; GO:0042559; GO:0042802; GO:0046656; GO:0051289; GO:0071172`
- `EC:1.5.1.3; 1.5.1.50`

## Notes

Dihydromonapterin reductase (H(2)-MPt reductase) (EC 1.5.1.50) (Dihydrofolate reductase) (DHFR) (EC 1.5.1.3)
