---
entity_id: "protein.P0ADP0"
entity_type: "protein"
name: "yigB"
source_database: "UniProt"
source_id: "P0ADP0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yigB b3812 JW3785"
---

# yigB

`protein.P0ADP0`

## Static

- Type: `protein`
- Source: `UniProt:P0ADP0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of 5-amino-6-(5-phospho-D-ribitylamino)uracil, and thus could be involved in the riboflavin biosynthesis pathway (PubMed:24123841). Is also able to dephosphorylate flavin mononucleotide (FMN) and other phosphoric acid esters (PubMed:16990279, PubMed:24123841). YigB is important for the formation of dormant persister cells (PubMed:18519731). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:18519731, ECO:0000269|PubMed:24123841}. The identity of the enzyme(s) catalyzing the dephosphorylation of CPD-1086 in the riboflavin biosynthesis pathway was long unknown . have now shown that at least two enzymes, YigB and YbjI, can catalyze this reaction. YigB was initially identified as an FMN phosphatase that belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . yigB is important for formation of dormant persister cells; overexpression of yigB leads to increased tolerance to ofloxacin . Deletion of yigB alone does not result in riboflavin auxotrophy .

## Biological Role

Catalyzes riboflavin-5-phosphate phosphohydrolase (reaction.R00548), 5-amino-6-(5-phospho-D-ribitylamino)uracil phosphohydrolase (reaction.R07280), RIBOPHOSPHAT-RXN (reaction.ecocyc.RIBOPHOSPHAT-RXN), RXN0-5187 (reaction.ecocyc.RXN0-5187). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of 5-amino-6-(5-phospho-D-ribitylamino)uracil, and thus could be involved in the riboflavin biosynthesis pathway (PubMed:24123841). Is also able to dephosphorylate flavin mononucleotide (FMN) and other phosphoric acid esters (PubMed:16990279, PubMed:24123841). YigB is important for the formation of dormant persister cells (PubMed:18519731). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:18519731, ECO:0000269|PubMed:24123841}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00548|reaction.R00548]] `KEGG` `database` - via EC:3.1.3.102
- `catalyzes` --> [[reaction.R07280|reaction.R07280]] `KEGG` `database` - via EC:3.1.3.104
- `catalyzes` --> [[reaction.ecocyc.RIBOPHOSPHAT-RXN|reaction.ecocyc.RIBOPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5187|reaction.ecocyc.RXN0-5187]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3812|gene.b3812]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADP0`
- `KEGG:ecj:JW3785;eco:b3812;ecoc:C3026_20635;`
- `GeneID:93778131;948357;`
- `GO:GO:0000287; GO:0009231; GO:0016791; GO:0022611; GO:0043726`
- `EC:3.1.3.104`

## Notes

5-amino-6-(5-phospho-D-ribitylamino)uracil phosphatase YigB (EC 3.1.3.104)
