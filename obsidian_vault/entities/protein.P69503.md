---
entity_id: "protein.P69503"
entity_type: "protein"
name: "apt"
source_database: "UniProt"
source_id: "P69503"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "apt b0469 JW0458"
---

# apt

`protein.P69503`

## Static

- Type: `protein`
- Source: `UniProt:P69503`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes a salvage reaction resulting in the formation of AMP, that is energically less costly than de novo synthesis. Adenine phosphoribosyltransferase is a purine salvage enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from PRPP to the N9 position of adenine to yield AMP. APRT is one of three E. coli phosphoribosyltransferases (PRTases) that participate in purine salvage, Gpt, Hpt and Apt . Enzyme activity is induced by growth on purines, amethopterin, and thymine and is higher in stationary phase cultures. The enzyme is subject to negative regulation by uncyclized nucleoside 5'-phosphates and end product inhibition . Adenine phosphoribosyltransferase is cytoplasmic , but can be found associated with isolated membrane vesicles . Apt: "adenine phosphoribosyltransferase"

## Biological Role

Catalyzes AMP:diphosphate phospho-D-ribosyltransferase (reaction.R00190). Component of adenine phosphoribosyltransferase (complex.ecocyc.ADENPRIBOSYLTRAN-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes a salvage reaction resulting in the formation of AMP, that is energically less costly than de novo synthesis.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00190|reaction.R00190]] `KEGG` `database` - via EC:2.4.2.7
- `is_component_of` --> [[complex.ecocyc.ADENPRIBOSYLTRAN-CPLX|complex.ecocyc.ADENPRIBOSYLTRAN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0469|gene.b0469]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69503`
- `KEGG:ecj:JW0458;eco:b0469;ecoc:C3026_02305;`
- `GeneID:93776981;945113;`
- `GO:GO:0000287; GO:0003999; GO:0005829; GO:0006166; GO:0006168; GO:0042803; GO:0044209`
- `EC:2.4.2.7`

## Notes

Adenine phosphoribosyltransferase (APRT) (EC 2.4.2.7)
