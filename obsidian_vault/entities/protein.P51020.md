---
entity_id: "protein.P51020"
entity_type: "protein"
name: "mhpE"
source_database: "UniProt"
source_id: "P51020"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpE b0352 JW0343"
---

# mhpE

`protein.P51020`

## Static

- Type: `protein`
- Source: `UniProt:P51020`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the retro-aldol cleavage of 4-hydroxy-2-oxopentanoate to pyruvate and acetaldehyde. Is involved in the meta-cleavage pathway for the degradation of 3-phenylpropanoate. {ECO:0000269|PubMed:9758851}. 4-hydroxy-2-ketopentanoate aldolase (MhpE) is a stereospecific class I aldolase . The expression of MhpE is translationally coupled to MhpF, and interaction between the two proteins appears to be required for solubility of MhpE . E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving MhpE is used for the catabolism of 3-phenylpropionate . MhpE: "m-hydroxyphenylpropionate"

## Biological Role

Catalyzes 4-hydroxy-2-oxopentanoate pyruvate-lyase (acetaldehyde-forming) (reaction.R00750), MHPELY-RXN (reaction.ecocyc.MHPELY-RXN).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Catalyzes the retro-aldol cleavage of 4-hydroxy-2-oxopentanoate to pyruvate and acetaldehyde. Is involved in the meta-cleavage pathway for the degradation of 3-phenylpropanoate. {ECO:0000269|PubMed:9758851}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00750|reaction.R00750]] `KEGG` `database` - via EC:4.1.3.39
- `catalyzes` --> [[reaction.ecocyc.MHPELY-RXN|reaction.ecocyc.MHPELY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0352|gene.b0352]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P51020`
- `KEGG:ecj:JW0343;eco:b0352;ecoc:C3026_01735;ecoc:C3026_24895;`
- `GeneID:75202515;945012;`
- `GO:GO:0003852; GO:0008701; GO:0009098; GO:0019380; GO:0030145`
- `EC:4.1.3.39`

## Notes

4-hydroxy-2-oxovalerate aldolase (HOA) (EC 4.1.3.39) (4-hydroxy-2-keto-pentanoic acid aldolase) (4-hydroxy-2-oxopentanoate aldolase)
