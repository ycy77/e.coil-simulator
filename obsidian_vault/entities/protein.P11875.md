---
entity_id: "protein.P11875"
entity_type: "protein"
name: "argS"
source_database: "UniProt"
source_id: "P11875"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argS b1876 JW1865"
---

# argS

`protein.P11875`

## Static

- Type: `protein`
- Source: `UniProt:P11875`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS) Arginine-tRNA ligase (ArgRS) is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. ArgRS belongs to the Class IA aminoacyl tRNA synthetases; apart from sequence motifs within the active site, the different enzymes show little similarity in their primary amino acid sequences . The kinetic mechanism of ArgRS has been investigated . ArgRS has been crystallized , and the structure of a complex with L-arginine has been solved at 2.9 Å resolution, elucidating the structural and fuctional role of active site residues . Conformational changes induced by interactions with its tRNA and arginine substrates have been studied , and specific interations with nucleotide residues in some tRNA species have been determined . Specificity determinants within tRNAArg that are important for recognition by ArgRS have been identified . The argS open reading frame uses the unusual initiation codon GUG and has a codon usage pattern which is typical for highly expressed genes . Several mutations in argS have been described. The MA5002 mutant carries an Arg134Ser mutation located close to the active site of ArgRS, leading to defects in enzymatic activity and Km value for ATP...

## Biological Role

Catalyzes ARGININE--TRNA-LIGASE-RXN (reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN|reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1876|gene.b1876]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11875`
- `KEGG:ecj:JW1865;eco:b1876;ecoc:C3026_10675;`
- `GeneID:75171948;946452;`
- `GO:GO:0004814; GO:0005524; GO:0005829; GO:0006420`
- `EC:6.1.1.19`

## Notes

Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS)
