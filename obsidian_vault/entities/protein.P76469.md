---
entity_id: "protein.P76469"
entity_type: "protein"
name: "rhmA"
source_database: "UniProt"
source_id: "P76469"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhmA yfaU b2245 JW2239"
---

# rhmA

`protein.P76469`

## Static

- Type: `protein`
- Source: `UniProt:P76469`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible retro-aldol cleavage of 2-keto-3-deoxy-L-rhamnonate (KDR) to pyruvate and lactaldehyde. 2-keto-3-deoxy-L-mannonate, 2-keto-3-deoxy-L-lyxonate and 4-hydroxy-2-ketoheptane-1,7-dioate (HKHD) are also reasonably good substrates, although 2-keto-3-deoxy-L-rhamnonate is likely to be the physiological substrate (PubMed:18754683, PubMed:18754693). In vitro, can catalyze the aldolisation reaction between hydroxypyruvate (HPA) or pyruvate (PA) and D-glyceraldehyde (D-GA) (Ref.6). The condensation of hydroxypyruvate and D-glyceraldehyde produces (3R,4S,5R)-3,4,5,6-tetrahydroxy-2-oxohexanoate as the major product, 2-dehydro-D-gluconate and 2-dehydro-D-galactonate (Ref.6). The condensation of pyruvate and D-glyceraldehyde produces 2-dehydro-3-deoxy-L-galactonate as the major product and 2-dehydro-3-deoxy-D-gluconate (Ref.6). {ECO:0000269|PubMed:18754683, ECO:0000269|PubMed:18754693, ECO:0000269|Ref.6}. YfaU is a 2-keto-3-deoxy-L-rhamnonate aldolase which catalyzes a retro-aldol reaction with somewhat relaxed substrate specificity . Crystal structures of the enzyme alone and in a product complex with Mg2+-pyruvate have been solved, showing a trimer of domain-swapped dimers with (β/α)8 barrel subunits typical of the divalent metal ion-dependent class II aldolases. The architecture of the active site and a predicted catalytic mechanism are discussed...

## Biological Role

Component of 2-keto-3-deoxy-L-rhamnonate aldolase (complex.ecocyc.CPLX0-7723).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible retro-aldol cleavage of 2-keto-3-deoxy-L-rhamnonate (KDR) to pyruvate and lactaldehyde. 2-keto-3-deoxy-L-mannonate, 2-keto-3-deoxy-L-lyxonate and 4-hydroxy-2-ketoheptane-1,7-dioate (HKHD) are also reasonably good substrates, although 2-keto-3-deoxy-L-rhamnonate is likely to be the physiological substrate (PubMed:18754683, PubMed:18754693). In vitro, can catalyze the aldolisation reaction between hydroxypyruvate (HPA) or pyruvate (PA) and D-glyceraldehyde (D-GA) (Ref.6). The condensation of hydroxypyruvate and D-glyceraldehyde produces (3R,4S,5R)-3,4,5,6-tetrahydroxy-2-oxohexanoate as the major product, 2-dehydro-D-gluconate and 2-dehydro-D-galactonate (Ref.6). The condensation of pyruvate and D-glyceraldehyde produces 2-dehydro-3-deoxy-L-galactonate as the major product and 2-dehydro-3-deoxy-D-gluconate (Ref.6). {ECO:0000269|PubMed:18754683, ECO:0000269|PubMed:18754693, ECO:0000269|Ref.6}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7723|complex.ecocyc.CPLX0-7723]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2245|gene.b2245]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76469`
- `KEGG:ecj:JW2239;eco:b2245;ecoc:C3026_12545;`
- `GeneID:948054;`
- `GO:GO:0000287; GO:0005737; GO:0016151; GO:0016832; GO:0034214; GO:0042802; GO:0061677; GO:0106099`
- `EC:4.1.2.53`

## Notes

2-keto-3-deoxy-L-rhamnonate aldolase (KDR aldolase) (EC 4.1.2.53) (2-dehydro-3-deoxyrhamnonate aldolase) (2-keto-3-deoxy acid sugar aldolase)
