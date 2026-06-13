---
entity_id: "protein.P0AFQ5"
entity_type: "protein"
name: "rutC"
source_database: "UniProt"
source_id: "P0AFQ5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutC ycdK b1010 JW0995"
---

# rutC

`protein.P0AFQ5`

## Static

- Type: `protein`
- Source: `UniProt:P0AFQ5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in pyrimidine catabolism (PubMed:16540542). Catalyzes the deamination of 3-aminoacrylate to malonic semialdehyde, a reaction that can also occur spontaneously (PubMed:33839153). RutC may facilitate the reaction and modulate the metabolic fitness, rather than catalyzing essential functions (PubMed:33839153). In vitro, can also deaminate 2-aminoacrylate (PubMed:33839153). {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:33839153}.

## Biological Role

Component of 3-aminoacrylate deaminase (complex.ecocyc.CPLX0-8589).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in pyrimidine catabolism (PubMed:16540542). Catalyzes the deamination of 3-aminoacrylate to malonic semialdehyde, a reaction that can also occur spontaneously (PubMed:33839153). RutC may facilitate the reaction and modulate the metabolic fitness, rather than catalyzing essential functions (PubMed:33839153). In vitro, can also deaminate 2-aminoacrylate (PubMed:33839153). {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:33839153}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8589|complex.ecocyc.CPLX0-8589]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1010|gene.b1010]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFQ5`
- `KEGG:ecj:JW0995;eco:b1010;ecoc:C3026_06145;`
- `GeneID:75171086;945599;`
- `GO:GO:0005829; GO:0006208; GO:0006212; GO:0019239; GO:0019740; GO:0042802`
- `EC:3.5.-.-`

## Notes

3-aminoacrylate deaminase RutC (3-AA deaminase) (EC 3.5.-.-)
