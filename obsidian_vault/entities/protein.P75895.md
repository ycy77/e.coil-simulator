---
entity_id: "protein.P75895"
entity_type: "protein"
name: "rutD"
source_database: "UniProt"
source_id: "P75895"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutD ycdJ b1009 JW0994"
---

# rutD

`protein.P75895`

## Static

- Type: `protein`
- Source: `UniProt:P75895`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in pyrimidine catabolism (PubMed:16540542). May facilitate the hydrolysis of carbamate, a reaction that can also occur spontaneously (Probable). {ECO:0000269|PubMed:16540542, ECO:0000305|PubMed:33839153}.

## Biological Role

Component of putative aminoacrylate hydrolase RutD (complex.ecocyc.CPLX0-8303).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in pyrimidine catabolism (PubMed:16540542). May facilitate the hydrolysis of carbamate, a reaction that can also occur spontaneously (Probable). {ECO:0000269|PubMed:16540542, ECO:0000305|PubMed:33839153}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8303|complex.ecocyc.CPLX0-8303]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1009|gene.b1009]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75895`
- `KEGG:ecj:JW0994;eco:b1009;ecoc:C3026_06140;`
- `GeneID:946586;`
- `GO:GO:0006208; GO:0006212; GO:0016787; GO:0016811; GO:0019740; GO:0042803`
- `EC:3.5.1.-`

## Notes

Putative carbamate hydrolase RutD (EC 3.5.1.-) (Aminohydrolase)
