---
entity_id: "protein.P25889"
entity_type: "protein"
name: "preA"
source_database: "UniProt"
source_id: "P25889"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "preA yeiA b2147 JW2134"
---

# preA

`protein.P25889`

## Static

- Type: `protein`
- Source: `UniProt:P25889`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in pyrimidine base degradation. Catalyzes physiologically the reduction of uracil to 5,6-dihydrouracil (DHU) by using NADH as a specific cosubstrate. It also catalyzes the reverse reaction and the reduction of thymine to 5,6-dihydrothymine (DHT). {ECO:0000269|PubMed:18482579, ECO:0000269|PubMed:21169495}. PreA was shown to form a complex with PreT; PreAT has NAD+-dependent dihydropyrimidine dehydrogenase activity . PreA is expected to be the FMN-binding subunit . Based on sequence similarity, PreA was predicted to be a dihydrothymine/dihydropyrimidine dehydrogenase . PreA has similarity to the C-terminal half of mammalian dihydropyrimidine dehydrogenase . PreA is required for swarming motility . PreA:

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

- `encodes` <-- [[gene.b2147|gene.b2147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25889`
- `KEGG:ecj:JW2134;eco:b2147;ecoc:C3026_12030;`
- `GeneID:93775035;949037;`
- `GO:GO:0003954; GO:0004159; GO:0005737; GO:0006208; GO:0006210; GO:0006212; GO:0046872; GO:0051536; GO:0051539; GO:0071978; GO:0140690; GO:1990204`
- `EC:1.3.1.1`

## Notes

NAD-dependent dihydropyrimidine dehydrogenase subunit PreA (DPD) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase)
