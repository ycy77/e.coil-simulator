---
entity_id: "protein.P0A6R0"
entity_type: "protein"
name: "fabH"
source_database: "UniProt"
source_id: "P0A6R0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01815}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabH b1091 JW1077"
---

# fabH

`protein.P0A6R0`

## Static

- Type: `protein`
- Source: `UniProt:P0A6R0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01815}.

## Enriched Summary

FUNCTION: Catalyzes the condensation reaction of fatty acid synthesis by the addition to an acyl acceptor of two carbons from malonyl-ACP. Catalyzes the first condensation reaction which initiates fatty acid synthesis and may therefore play a role in governing the total rate of fatty acid production. Possesses both acetoacetyl-ACP synthase and acetyl transacylase activities. Has some substrate specificity for acetyl-CoA. Its substrate specificity determines the biosynthesis of straight-chain of fatty acids instead of branched-chain (PubMed:10629181, PubMed:7592873, PubMed:8631920, PubMed:8910376). Can also use propionyl-CoA, with lower efficiency (PubMed:10629181, PubMed:8631920). {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8631920, ECO:0000269|PubMed:8910376}.

## Biological Role

Component of 3-oxoacyl-[acyl carrier protein] synthase 3 (complex.ecocyc.CPLX0-252).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation reaction of fatty acid synthesis by the addition to an acyl acceptor of two carbons from malonyl-ACP. Catalyzes the first condensation reaction which initiates fatty acid synthesis and may therefore play a role in governing the total rate of fatty acid production. Possesses both acetoacetyl-ACP synthase and acetyl transacylase activities. Has some substrate specificity for acetyl-CoA. Its substrate specificity determines the biosynthesis of straight-chain of fatty acids instead of branched-chain (PubMed:10629181, PubMed:7592873, PubMed:8631920, PubMed:8910376). Can also use propionyl-CoA, with lower efficiency (PubMed:10629181, PubMed:8631920). {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8631920, ECO:0000269|PubMed:8910376}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-252|complex.ecocyc.CPLX0-252]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1091|gene.b1091]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6R0`
- `KEGG:ecj:JW1077;eco:b1091;ecoc:C3026_06600;`
- `GeneID:93776317;946003;`
- `GO:GO:0004315; GO:0005829; GO:0006631; GO:0030497; GO:0033818`
- `EC:2.3.1.180`

## Notes

Beta-ketoacyl-[acyl-carrier-protein] synthase III (Beta-ketoacyl-ACP synthase III) (KAS III) (EC 2.3.1.180) (3-oxoacyl-[acyl-carrier-protein] synthase 3) (3-oxoacyl-[acyl-carrier-protein] synthase III) (EcFabH)
