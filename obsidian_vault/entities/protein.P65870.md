---
entity_id: "protein.P65870"
entity_type: "protein"
name: "queD"
source_database: "UniProt"
source_id: "P65870"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "queD ygcM b2765 JW2735"
---

# queD

`protein.P65870`

## Static

- Type: `protein`
- Source: `UniProt:P65870`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of 7,8-dihydroneopterin triphosphate (H2NTP) to 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) and acetaldehyde. Can also convert 6-pyruvoyltetrahydropterin (PPH4) and sepiapterin to CPH4; these 2 compounds are probably intermediates in the reaction from H2NTP. {ECO:0000269|PubMed:19231875}.

## Biological Role

Component of 6-carboxy-5,6,7,8-tetrahydropterin synthase (complex.ecocyc.CPLX0-8123).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of 7,8-dihydroneopterin triphosphate (H2NTP) to 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) and acetaldehyde. Can also convert 6-pyruvoyltetrahydropterin (PPH4) and sepiapterin to CPH4; these 2 compounds are probably intermediates in the reaction from H2NTP. {ECO:0000269|PubMed:19231875}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8123|complex.ecocyc.CPLX0-8123]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2765|gene.b2765]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P65870`
- `KEGG:ecj:JW2735;eco:b2765;`
- `GeneID:945123;`
- `GO:GO:0008270; GO:0008616; GO:0042802; GO:0070497`
- `EC:4.1.2.50`

## Notes

6-carboxy-5,6,7,8-tetrahydropterin synthase (CPH4 synthase) (EC 4.1.2.50) (Queuosine biosynthesis protein QueD)
