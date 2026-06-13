---
entity_id: "protein.P0A9H5"
entity_type: "protein"
name: "btuR"
source_database: "UniProt"
source_id: "P0A9H5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btuR cobA b1270 JW1262"
---

# btuR

`protein.P0A9H5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9H5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Required for both de novo synthesis of the corrin ring for the assimilation of exogenous corrinoids. Participates in the adenosylation of a variety of incomplete and complete corrinoids (By similarity). {ECO:0000250}. E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . Sequence similarity and complementation of a cobA mutant in Salmonella typhimurium suggests that btuR encodes the cobinamide adenosyltransferase . Cobinamide adenosyltransferase catalyzes the synthesis of adenosylcobalamin from a cobalamin precursor transported into the cell . A btuR mutation leads to loss of repression of expression by externally supplied vitamin B12 and was therefore initially thought to encode a transcriptional repressor of btuB . However, it was later shown that a btuR mutation results in a decrease in the pool of intracellular adenosylcobalamin and is thus more likely involved in the conversion of vitamin B12 to adenosylcobalamin . Insertion mutants within btuR lead to an inability to utilize cobinamide under aerobic growth conditions . Laboratory evolution and overexpression experiments found that BtuR is required for growth in a HOMOCYSMETB12-MONOMER (MetH)-dependent strain with pseudocobalamin . BtuR: "B twelve uptake regulation"

## Biological Role

Catalyzes ATP:cobinamide Cobeta-adenosyltransferase (reaction.R07268), ATP:cob(II)alamin Cobeta-adenosyltransferase (reaction.R12183), BTUR2-RXN (reaction.ecocyc.BTUR2-RXN), COBALADENOSYLTRANS-RXN (reaction.ecocyc.COBALADENOSYLTRANS-RXN).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Required for both de novo synthesis of the corrin ring for the assimilation of exogenous corrinoids. Participates in the adenosylation of a variety of incomplete and complete corrinoids (By similarity). {ECO:0000250}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R07268|reaction.R07268]] `KEGG` `database` - via EC:2.5.1.17
- `catalyzes` --> [[reaction.R12183|reaction.R12183]] `KEGG` `database` - via EC:2.5.1.17
- `catalyzes` --> [[reaction.ecocyc.BTUR2-RXN|reaction.ecocyc.BTUR2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.COBALADENOSYLTRANS-RXN|reaction.ecocyc.COBALADENOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1270|gene.b1270]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9H5`
- `KEGG:ecj:JW1262;eco:b1270;ecoc:C3026_07440;`
- `GeneID:945839;`
- `GO:GO:0005524; GO:0005737; GO:0006779; GO:0008817; GO:0009236; GO:0019250`
- `EC:2.5.1.17`

## Notes

Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyltransferase) (Cobinamide/cobalamin adenosyltransferase)
