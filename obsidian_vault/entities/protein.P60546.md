---
entity_id: "protein.P60546"
entity_type: "protein"
name: "gmk"
source_database: "UniProt"
source_id: "P60546"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gmk spoR b3648 JW3623"
---

# gmk

`protein.P60546`

## Static

- Type: `protein`
- Source: `UniProt:P60546`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Essential for recycling GMP and indirectly, cGMP. {ECO:0000269|PubMed:8390989}.

## Biological Role

Catalyzes ATP:GMP phosphotransferase (reaction.R00332). Component of guanylate kinase (complex.ecocyc.GUANYL-KIN-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Essential for recycling GMP and indirectly, cGMP. {ECO:0000269|PubMed:8390989}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00332|reaction.R00332]] `KEGG` `database` - via EC:2.7.4.8
- `is_component_of` --> [[complex.ecocyc.GUANYL-KIN-CPLX|complex.ecocyc.GUANYL-KIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3648|gene.b3648]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60546`
- `KEGG:ecj:JW3623;eco:b3648;ecoc:C3026_19765;`
- `GeneID:93778363;948163;`
- `GO:GO:0004385; GO:0005524; GO:0005829; GO:0042802`
- `EC:2.7.4.8`

## Notes

Guanylate kinase (EC 2.7.4.8) (GMP kinase)
