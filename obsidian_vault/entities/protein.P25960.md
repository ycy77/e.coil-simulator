---
entity_id: "protein.P25960"
entity_type: "protein"
name: "gspO"
source_database: "UniProt"
source_id: "P25960"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P22610}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P22610}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspO hofD hopD hopO yheC b3335 JW3297"
---

# gspO

`protein.P25960`

## Static

- Type: `protein`
- Source: `UniProt:P25960`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P22610}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P22610}.

## Enriched Summary

FUNCTION: Plays a role in type II pseudopili formation by proteolytically removing the leader sequence from substrate proteins and subsequently monomethylating the alpha-amino group of the newly exposed N-terminal phenylalanine. Substrates include proteins required for biogenesis of the type II general secretory apparatus. {ECO:0000305|PubMed:8655552}. In Escherichia coli, gspO is a member of an operon of genes (gspC-O) which are not normally expressed but are homologous to those encoding the secreton, or type II secretion machinery in Klebsiella oxytoca and Aeromonase hydrophila, among others . Although Escherichia coli K-12 does not secrete endogenous proteins, the gsp genes of E. coli are orthologs of those in other secretons , including those of the pullulanase (pul) secretion pathway of Klebsiella oxytoca. GspO encodes a protein similar to type IV prepilin peptidases, like pulO gene in K. oxytoca. Though it is under the control of a promoter that has very poor basal expression under laboratory growth conditions, when expressed from a stronger promoter, GspO promotes cleavage of prepilin peptidase substrates such as type IV prepilin from Neisseria gonorrhoaea and prePulG as well as PulH, PulI and PulJ from K. oxytoca , referred to as pseudopilins . gspO is capable of complementing the processing function in a pulO deletion mutant...

## Biological Role

Catalyzes 3.4.23.43-RXN (reaction.ecocyc.3.4.23.43-RXN).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Plays a role in type II pseudopili formation by proteolytically removing the leader sequence from substrate proteins and subsequently monomethylating the alpha-amino group of the newly exposed N-terminal phenylalanine. Substrates include proteins required for biogenesis of the type II general secretory apparatus. {ECO:0000305|PubMed:8655552}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.23.43-RXN|reaction.ecocyc.3.4.23.43-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3335|gene.b3335]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25960`
- `KEGG:ecj:JW3297;eco:b3335;ecoc:C3026_18115;`
- `GeneID:947840;`
- `GO:GO:0004190; GO:0005886; GO:0006465; GO:0008233; GO:0016740`
- `EC:2.1.1.-; 3.4.23.43`

## Notes

Prepilin leader peptidase/N-methyltransferase [Includes: Leader peptidase (EC 3.4.23.43) (Prepilin peptidase); N-methyltransferase (EC 2.1.1.-)]
