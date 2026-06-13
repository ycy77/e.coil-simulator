---
entity_id: "protein.P0A7E3"
entity_type: "protein"
name: "pyrE"
source_database: "UniProt"
source_id: "P0A7E3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrE b3642 JW3617"
---

# pyrE

`protein.P0A7E3`

## Static

- Type: `protein`
- Source: `UniProt:P0A7E3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of a ribosyl phosphate group from 5-phosphoribose 1-diphosphate to orotate, leading to the formation of orotidine monophosphate (OMP). {ECO:0000255|HAMAP-Rule:MF_01208, ECO:0000269|PubMed:8620002}.

## Biological Role

Component of orotate phosphoribosyltransferase (complex.ecocyc.OROPRIBTRANS-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a ribosyl phosphate group from 5-phosphoribose 1-diphosphate to orotate, leading to the formation of orotidine monophosphate (OMP). {ECO:0000255|HAMAP-Rule:MF_01208, ECO:0000269|PubMed:8620002}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.OROPRIBTRANS-CPLX|complex.ecocyc.OROPRIBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3642|gene.b3642]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7E3`
- `KEGG:ecj:JW3617;eco:b3642;ecoc:C3026_19735;`
- `GeneID:75173836;75202211;948157;`
- `GO:GO:0000287; GO:0004588; GO:0005737; GO:0005829; GO:0006207; GO:0006221; GO:0042803; GO:0044205; GO:0046132`
- `EC:2.4.2.10`

## Notes

Orotate phosphoribosyltransferase (OPRT) (OPRTase) (EC 2.4.2.10)
