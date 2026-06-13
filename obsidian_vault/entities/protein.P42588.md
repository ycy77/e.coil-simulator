---
entity_id: "protein.P42588"
entity_type: "protein"
name: "patA"
source_database: "UniProt"
source_id: "P42588"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "patA ygjG b3073 JW5510"
---

# patA

`protein.P42588`

## Static

- Type: `protein`
- Source: `UniProt:P42588`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the aminotransferase reaction from putrescine to 2-oxoglutarate, leading to glutamate and 4-aminobutanal, which spontaneously cyclizes to form 1-pyrroline (PubMed:12617754, PubMed:3510672). This is the first step in one of two pathways for putrescine degradation, where putrescine is converted into 4-aminobutanoate (gamma-aminobutyrate or GABA) via 4-aminobutanal, which allows E.coli to grow on putrescine as the sole nitrogen source (PubMed:22636776, PubMed:3510672). Also functions as a cadaverine transaminase in a a L-lysine degradation pathway to succinate that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:12617754, PubMed:30498244). Is also able to transaminate spermidine, in lower extent, but not ornithine. Alpha-ketobutyrate and pyruvate can also act as amino acceptors, although much less efficiently (PubMed:12617754). {ECO:0000269|PubMed:12617754, ECO:0000269|PubMed:22636776, ECO:0000269|PubMed:30498244, ECO:0000269|PubMed:3510672}.

## Biological Role

Catalyzes putrescine:2-oxoglutarate aminotransferase (reaction.R01155). Component of putrescine aminotransferase (complex.ecocyc.CPLX0-8159).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the aminotransferase reaction from putrescine to 2-oxoglutarate, leading to glutamate and 4-aminobutanal, which spontaneously cyclizes to form 1-pyrroline (PubMed:12617754, PubMed:3510672). This is the first step in one of two pathways for putrescine degradation, where putrescine is converted into 4-aminobutanoate (gamma-aminobutyrate or GABA) via 4-aminobutanal, which allows E.coli to grow on putrescine as the sole nitrogen source (PubMed:22636776, PubMed:3510672). Also functions as a cadaverine transaminase in a a L-lysine degradation pathway to succinate that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:12617754, PubMed:30498244). Is also able to transaminate spermidine, in lower extent, but not ornithine. Alpha-ketobutyrate and pyruvate can also act as amino acceptors, although much less efficiently (PubMed:12617754). {ECO:0000269|PubMed:12617754, ECO:0000269|PubMed:22636776, ECO:0000269|PubMed:30498244, ECO:0000269|PubMed:3510672}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01155|reaction.R01155]] `KEGG` `database` - via EC:2.6.1.82
- `is_component_of` --> [[complex.ecocyc.CPLX0-8159|complex.ecocyc.CPLX0-8159]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3073|gene.b3073]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42588`
- `KEGG:ecj:JW5510;eco:b3073;ecoc:C3026_16785;`
- `GeneID:947120;`
- `GO:GO:0005829; GO:0009447; GO:0019161; GO:0019477; GO:0030170; GO:0033094; GO:0042802; GO:0042803`
- `EC:2.6.1.29; 2.6.1.82`

## Notes

Putrescine aminotransferase (PAT) (PATase) (EC 2.6.1.82) (Cadaverine transaminase) (Diamine transaminase) (EC 2.6.1.29) (Putrescine transaminase) (Putrescine--2-oxoglutaric acid transaminase) (Putrescine:2-OG aminotransferase)
