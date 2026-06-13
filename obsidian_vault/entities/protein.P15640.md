---
entity_id: "protein.P15640"
entity_type: "protein"
name: "purD"
source_database: "UniProt"
source_id: "P15640"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purD b4005 JW3969"
---

# purD

`protein.P15640`

## Static

- Type: `protein`
- Source: `UniProt:P15640`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of phosphoribosylamine to glycinamide ribonucleotide, an enzymatic step in purine biosynthesis pathway. {ECO:0000269|PubMed:2182115}. Phosphoribosylamine—glycine ligase (glycinamide ribonucleotide synthetase, GAR synthetase) catalyzes the ligation of glycine to 5-phospho-β-D-ribosyl-amine (PRA) to produce 5-phospho-ribosyl-glycineamide (GAR) in the second step of the E. coli purine de novo biosynthesis pathway. Its kinetic mechanism for substrate binding and product release has been described as sequential and ordered. PRA was suggested to bind first, followed by ATP and glycine, with phosphate leaving first, followed by ADP and GAR. However, PRA is unstable and can hydrolyze to ribose-5-phosphate and ammonia under physiological conditions . A hypothetical docking and channeling model for the transfer of PRA from PurF to the PurD monomer has been proposed . A recombinant, poly-His-tagged Pro294Leu mutant enzyme was crystallized and its structure determined at 1.6 Å resolution . Review: Jensen, K.F., G. Dandanell, B. Hove-Jensen, and M. Willemoes (2008) "Nucleotides, Nucleosides and Nucleobases" EcoSal 3.6.2

## Biological Role

Catalyzes 5-phospho-D-ribosylamine:glycine ligase (ADP-forming) (reaction.R04144), GLYRIBONUCSYN-RXN (reaction.ecocyc.GLYRIBONUCSYN-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible conversion of phosphoribosylamine to glycinamide ribonucleotide, an enzymatic step in purine biosynthesis pathway. {ECO:0000269|PubMed:2182115}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04144|reaction.R04144]] `KEGG` `database` - via EC:6.3.4.13
- `catalyzes` --> [[reaction.ecocyc.GLYRIBONUCSYN-RXN|reaction.ecocyc.GLYRIBONUCSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4005|gene.b4005]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15640`
- `KEGG:ecj:JW3969;eco:b4005;ecoc:C3026_21630;`
- `GeneID:948504;`
- `GO:GO:0004637; GO:0005524; GO:0006164; GO:0006189; GO:0006974; GO:0009113; GO:0016887; GO:0046872`
- `EC:6.3.4.13`

## Notes

Phosphoribosylamine--glycine ligase (EC 6.3.4.13) (GARS) (Glycinamide ribonucleotide synthetase) (Phosphoribosylglycinamide synthetase)
