---
entity_id: "protein.P0A6G3"
entity_type: "protein"
name: "pncC"
source_database: "UniProt"
source_id: "P0A6G3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pncC ygaD b2700 JW2670"
---

# pncC

`protein.P0A6G3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6G3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Has nicotinamidemononucleotide (NMN) aminohydrolase activity, not active on other substrates. {ECO:0000269|PubMed:21953451}.

## Biological Role

Component of NMN amidohydrolase (complex.ecocyc.CPLXECOLI-7943).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Has nicotinamidemononucleotide (NMN) aminohydrolase activity, not active on other substrates. {ECO:0000269|PubMed:21953451}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLXECOLI-7943|complex.ecocyc.CPLXECOLI-7943]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2700|gene.b2700]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6G3`
- `KEGG:ecj:JW2670;eco:b2700;ecoc:C3026_14865;`
- `GeneID:93779311;947169;`
- `GO:GO:0019159; GO:0019363`
- `EC:3.5.1.42`

## Notes

Nicotinamide-nucleotide amidohydrolase PncC (NMN amidohydrolase PncC) (EC 3.5.1.42) (NMN deamidase) (Nicotinamide-nucleotide amidase)
