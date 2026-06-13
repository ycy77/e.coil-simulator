---
entity_id: "protein.P0AGJ9"
entity_type: "protein"
name: "tyrS"
source_database: "UniProt"
source_id: "P0AGJ9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02006, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tyrS b1637 JW1629"
---

# tyrS

`protein.P0AGJ9`

## Static

- Type: `protein`
- Source: `UniProt:P0AGJ9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02006, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the attachment of L-tyrosine to tRNA(Tyr) in a two-step reaction: tyrosine is first activated by ATP to form Tyr-AMP and then transferred to the acceptor end of tRNA(Tyr) (PubMed:4292198, PubMed:4579631). Can also mischarge tRNA(Tyr) with D-tyrosine, leading to the formation of D-tyrosyl-tRNA(Tyr), which can be hydrolyzed by the D-aminoacyl-tRNA deacylase (PubMed:4292198). In vitro, can also use the non-natural amino acid azatyrosine (PubMed:11006270). {ECO:0000269|PubMed:11006270, ECO:0000269|PubMed:4292198, ECO:0000269|PubMed:4579631}. Tyrosine-tRNA ligase (TyrRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. TyrRS belongs to the Class IC aminoacyl tRNA synthetases . The enzyme is a homodimer in solution . TyrRS binds one molecule of tRNATyr per TyrRS dimer and has two binding sites for tyrosine with different dissociation constants . Other reports find two equivalent tyrosinyl-5'-AMP binding sites ; the binding data may require more complex analysis . The reaction mechanism of TyrRS has been studied . Aminoacylation proceeds via the aminoacyl adenylate pathway . TyrRS also aminoacylates tRNATyr with D-tyrosine ; the resulting D-Tyr-tRNATyr can be hydrolyzed by EC-3.1.1.96...

## Biological Role

Catalyzes L-tyrosine:tRNA(Tyr) ligase (AMP-forming) (reaction.R02918). Component of tyrosine—tRNA ligase (complex.ecocyc.TYRS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of L-tyrosine to tRNA(Tyr) in a two-step reaction: tyrosine is first activated by ATP to form Tyr-AMP and then transferred to the acceptor end of tRNA(Tyr) (PubMed:4292198, PubMed:4579631). Can also mischarge tRNA(Tyr) with D-tyrosine, leading to the formation of D-tyrosyl-tRNA(Tyr), which can be hydrolyzed by the D-aminoacyl-tRNA deacylase (PubMed:4292198). In vitro, can also use the non-natural amino acid azatyrosine (PubMed:11006270). {ECO:0000269|PubMed:11006270, ECO:0000269|PubMed:4292198, ECO:0000269|PubMed:4579631}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02918|reaction.R02918]] `KEGG` `database` - via EC:6.1.1.1
- `is_component_of` --> [[complex.ecocyc.TYRS-CPLX|complex.ecocyc.TYRS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1637|gene.b1637]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGJ9`
- `KEGG:ecj:JW1629;eco:b1637;ecoc:C3026_09405;`
- `GeneID:93775791;948855;`
- `GO:GO:0003723; GO:0004831; GO:0005524; GO:0005829; GO:0006437; GO:0016020; GO:0042803; GO:0043039`
- `EC:6.1.1.1`

## Notes

Tyrosine--tRNA ligase (EC 6.1.1.1) (Tyrosyl-tRNA synthetase) (TyrRS)
