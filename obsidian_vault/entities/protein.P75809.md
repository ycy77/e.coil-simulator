---
entity_id: "protein.P75809"
entity_type: "protein"
name: "ybjI"
source_database: "UniProt"
source_id: "P75809"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybjI b0844 JW5113"
---

# ybjI

`protein.P75809`

## Static

- Type: `protein`
- Source: `UniProt:P75809`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of 5-amino-6-(5-phospho-D-ribitylamino)uracil, and thus could be involved in the riboflavin biosynthesis pathway (PubMed:24123841). Is also able to dephosphorylate flavin mononucleotide (FMN), erythrose 4-phosphate and other phosphoric acid esters (PubMed:15808744, PubMed:16990279, PubMed:24123841). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:24123841}. The identity of the enzyme(s) catalyzing the dephosphorylation of CPD-1086 in the riboflavin biosynthesis pathway was long unknown . have now shown that at least two enzymes, YbjI and YigB, can catalyze this reaction. YbjI was initially identified as an FMN phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. In addition, YbjI has some phosphatase activity against pyridoxal phosphate . The phosphatase activity of YbjI was first discovered in a high-throughput screen of purified proteins . Deletion of ybjI alone does not result in riboflavin auxotrophy .

## Biological Role

Catalyzes riboflavin-5-phosphate phosphohydrolase (reaction.R00548), 5-amino-6-(5-phospho-D-ribitylamino)uracil phosphohydrolase (reaction.R07280), RIBOPHOSPHAT-RXN (reaction.ecocyc.RIBOPHOSPHAT-RXN), RXN0-5187 (reaction.ecocyc.RXN0-5187). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of 5-amino-6-(5-phospho-D-ribitylamino)uracil, and thus could be involved in the riboflavin biosynthesis pathway (PubMed:24123841). Is also able to dephosphorylate flavin mononucleotide (FMN), erythrose 4-phosphate and other phosphoric acid esters (PubMed:15808744, PubMed:16990279, PubMed:24123841). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:24123841}.

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
- `encodes` <-- [[gene.b0844|gene.b0844]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75809`
- `KEGG:ecj:JW5113;eco:b0844;ecoc:C3026_05275;`
- `GeneID:945470;`
- `GO:GO:0000287; GO:0005829; GO:0009231; GO:0016791; GO:0043726`
- `EC:3.1.3.104`

## Notes

5-amino-6-(5-phospho-D-ribitylamino)uracil phosphatase YbjI (EC 3.1.3.104)
