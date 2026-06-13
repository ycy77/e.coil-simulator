---
entity_id: "protein.P76440"
entity_type: "protein"
name: "preT"
source_database: "UniProt"
source_id: "P76440"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "preT yeiT b2146 JW2133"
---

# preT

`protein.P76440`

## Static

- Type: `protein`
- Source: `UniProt:P76440`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in pyrimidine base degradation. Catalyzes physiologically the reduction of uracil to 5,6-dihydrouracil (DHU) by using NADH as a specific cosubstrate. It also catalyzes the reverse reaction and the reduction of thymine to 5,6-dihydrothymine (DHT). {ECO:0000269|PubMed:18482579, ECO:0000269|PubMed:21169495}. PreT was shown to form a complex with PreA; PreAT has NAD+-dependent dihydropyrimidine dehydrogenase activity . PreT is expected to be the FAD-binding subunit . Based on sequence similarity, PreT was predicted to be a dihydrothymine dehydrogenase or glutamate synthase . PreT has similarity to the N-terminal half of mammalian dihydropyrimidine dehydrogenase . Expression of preT is 20-fold higher in a biofilm than during exponential growth in liquid culture . PreT:

## Biological Role

Catalyzes 5,6-dihydrouracil:NAD+ oxidoreductase (reaction.R00977). Component of dihydropyrimidine dehydrogenase (NAD+) (complex.ecocyc.CPLX0-7788).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in pyrimidine base degradation. Catalyzes physiologically the reduction of uracil to 5,6-dihydrouracil (DHU) by using NADH as a specific cosubstrate. It also catalyzes the reverse reaction and the reduction of thymine to 5,6-dihydrothymine (DHT). {ECO:0000269|PubMed:18482579, ECO:0000269|PubMed:21169495}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00977|reaction.R00977]] `KEGG` `database` - via EC:1.3.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7788|complex.ecocyc.CPLX0-7788]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2146|gene.b2146]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76440`
- `KEGG:ecj:JW2133;eco:b2146;ecoc:C3026_12025;`
- `GeneID:949049;`
- `GO:GO:0003954; GO:0004159; GO:0006208; GO:0006210; GO:0006212; GO:0016491; GO:0051536; GO:0140690; GO:1990204`
- `EC:1.3.1.1`

## Notes

NAD-dependent dihydropyrimidine dehydrogenase subunit PreT (DPD) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase)
