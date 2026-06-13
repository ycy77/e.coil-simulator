---
entity_id: "protein.P29208"
entity_type: "protein"
name: "menC"
source_database: "UniProt"
source_id: "P29208"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menC b2261 JW2256"
---

# menC

`protein.P29208`

## Static

- Type: `protein`
- Source: `UniProt:P29208`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate (SHCHC) to 2-succinylbenzoate (OSB) (PubMed:10194342, PubMed:8335646). Does not show detectable N-acylamino acid racemase (NAAAR) activity with N-acetyl-S-methionine as substrate (PubMed:10194342). {ECO:0000269|PubMed:10194342, ECO:0000269|PubMed:8335646}. O-succinylbenzoate synthase catalyzes the formation of the first aromatic intermediate of the menaquinone biosynthetic pathway by dehydration of 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate . MenC belongs to the MLE subfamily of the enolase family of enzymes . Crystal structures of the ligand-free, mutant enzyme-substrate, and enzyme-product complexes have been solved, and a reaction mechanism has been proposed . Site-directed mutagenesis of two proposed active-site lysines, Lys133 and Lys235, yielded catalytically inactive enzymes . Review:

## Biological Role

Catalyzes O-SUCCINYLBENZOATE-COA-SYN-RXN (reaction.ecocyc.O-SUCCINYLBENZOATE-COA-SYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Converts 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate (SHCHC) to 2-succinylbenzoate (OSB) (PubMed:10194342, PubMed:8335646). Does not show detectable N-acylamino acid racemase (NAAAR) activity with N-acetyl-S-methionine as substrate (PubMed:10194342). {ECO:0000269|PubMed:10194342, ECO:0000269|PubMed:8335646}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.O-SUCCINYLBENZOATE-COA-SYN-RXN|reaction.ecocyc.O-SUCCINYLBENZOATE-COA-SYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2261|gene.b2261]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P29208`
- `KEGG:ecj:JW2256;eco:b2261;ecoc:C3026_12630;`
- `GeneID:946734;`
- `GO:GO:0000287; GO:0009234; GO:0016836; GO:0043748`
- `EC:4.2.1.113`

## Notes

o-succinylbenzoate synthase (OSB synthase) (OSBS) (EC 4.2.1.113) (4-(2'-carboxyphenyl)-4-oxybutyric acid synthase) (o-succinylbenzoic acid synthase)
