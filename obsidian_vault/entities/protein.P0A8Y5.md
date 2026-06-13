---
entity_id: "protein.P0A8Y5"
entity_type: "protein"
name: "yidA"
source_database: "UniProt"
source_id: "P0A8Y5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yidA b3697 JW3674"
---

# yidA

`protein.P0A8Y5`

## Static

- Type: `protein`
- Source: `UniProt:P0A8Y5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of different sugar phosphates including erythrose-4-phosphate (Ery4P), ribose-5-phosphate (Ribu5P), fructose-1-phosphate (Fru1P), fructose-6-phosphate (Fru6P), glucose-6-P (Glu6P), and also imidodiphosphate (Imido-di-P) and acetyl phosphate (Acetyl-P). Selectively hydrolyzes alpha-D-glucose-1-phosphate (Glu1P) and has no activity with the beta form. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}. YidA is a promiscuous sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Its preferred substrate is erythrose-4-phosphate . YidA selectively hydrolyzes α-D-glucose-1-phosphate and has no activity with the β form . The reaction proceeds via the canonical phosphomonoester hydrolase mechanism, which involves breakage of the P-O bond, not the C1-O bond . The phosphatase activity of YidA was first discovered in a high-throughput screen of purified proteins . Mutagenesis of the predicted catalytic Asp residue in YidA results in loss of phosphatase activity . YidA does not catalyze phosphoryl transfer to a sugar acceptor .

## Biological Role

Catalyzes SUGAR-PHOSPHATASE-RXN (reaction.ecocyc.SUGAR-PHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Catalyzes the dephosphorylation of different sugar phosphates including erythrose-4-phosphate (Ery4P), ribose-5-phosphate (Ribu5P), fructose-1-phosphate (Fru1P), fructose-6-phosphate (Fru6P), glucose-6-P (Glu6P), and also imidodiphosphate (Imido-di-P) and acetyl phosphate (Acetyl-P). Selectively hydrolyzes alpha-D-glucose-1-phosphate (Glu1P) and has no activity with the beta form. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUGAR-PHOSPHATASE-RXN|reaction.ecocyc.SUGAR-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3697|gene.b3697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8Y5`
- `KEGG:ecj:JW3674;eco:b3697;ecoc:C3026_20040;`
- `GeneID:93778438;948204;`
- `GO:GO:0000287; GO:0005829; GO:0016791; GO:0050308`
- `EC:3.1.3.23`

## Notes

Sugar phosphatase YidA (EC 3.1.3.23)
