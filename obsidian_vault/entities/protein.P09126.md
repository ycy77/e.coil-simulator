---
entity_id: "protein.P09126"
entity_type: "protein"
name: "hemD"
source_database: "UniProt"
source_id: "P09126"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemD b3804 JW3776"
---

# hemD

`protein.P09126`

## Static

- Type: `protein`
- Source: `UniProt:P09126`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes cyclization of the linear tetrapyrrole, hydroxymethylbilane, to the macrocyclic uroporphyrinogen III. {ECO:0000250}. Uroporphyrinogen III synthase catalyzes the cyclization of hydroxymethylbilane with inversion of ring D to form uroporphyrinogen III, the last common intermediate in the heme and corrin (B-12) pathways . Uroporphyrinogen III synthase forms a complex with hydroxymethylbilane synthase . The hemD gene which encodes uroporphyrinogen III synthase has been cloned, and the product has been overexpressed, purified and characterized . The hemD gene is adjacent to hemC and both genes appear to be transcribed by the same promoter . A group of hemin requiring mutants had defects in uroporphyrinogen III synthase .

## Biological Role

Catalyzes hydroxymethylbilane hydro-lyase(cyclizing) (reaction.R03165), UROGENIIISYN-RXN (reaction.ecocyc.UROGENIIISYN-RXN).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes cyclization of the linear tetrapyrrole, hydroxymethylbilane, to the macrocyclic uroporphyrinogen III. {ECO:0000250}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03165|reaction.R03165]] `KEGG` `database` - via EC:4.2.1.75
- `catalyzes` --> [[reaction.ecocyc.UROGENIIISYN-RXN|reaction.ecocyc.UROGENIIISYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3804|gene.b3804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09126`
- `KEGG:ecj:JW3776;eco:b3804;ecoc:C3026_20595;`
- `GeneID:948587;`
- `GO:GO:0004852; GO:0006780; GO:0006782`
- `EC:4.2.1.75`

## Notes

Uroporphyrinogen-III synthase (UROS) (EC 4.2.1.75) (Hydroxymethylbilane hydrolyase [cyclizing]) (Uroporphyrinogen-III cosynthase)
