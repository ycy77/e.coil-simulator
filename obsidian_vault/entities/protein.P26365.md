---
entity_id: "protein.P26365"
entity_type: "protein"
name: "amiB"
source_database: "UniProt"
source_id: "P26365"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amiB yjeD b4169 JW4127"
---

# amiB

`protein.P26365`

## Static

- Type: `protein`
- Source: `UniProt:P26365`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}. amiB encodes a protein with N-acetylmuramoyl-L-alanine amidase activity. Murein sacculi isolated from a strain overexpressing amiB shows a significant decrease in the amount of high molecular weight murein; expression of amiB from a plasmid complements the chaining phenotype associated with deletion of the three N-acetylmuramoyl-L-alanine amidases NACMURLALAAMI1-MONOMER "AmiA", AmiB and G7458-MONOMER "AmiC" . Murein amidase activity produces stemless or a-denuded-peptidoglycan denuded glycans. Cells containing double amidase gene deletions (ΔamiAB, ΔamiAC and ΔamiBC) form septal peptidoglycan rings - thick dark bands of peptidoglycan between adjacent cells seen in the purified sacculi from chained cells . The murein amidases are necessary for the continued incorporation of peptidoglycan into the developing septum in E. coli . The divisome associated factor, EG12297-MONOMER "envC", activates AmiB and AmiA catalysed peptidoglycan cleavage in vitro...

## Biological Role

Catalyzes N-acetylmuramoyl-Ala amidohydrolase (reaction.R04112), RXN-16938 (reaction.ecocyc.RXN-16938).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04112|reaction.R04112]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` --> [[reaction.ecocyc.RXN-16938|reaction.ecocyc.RXN-16938]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4169|gene.b4169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26365`
- `KEGG:ecj:JW4127;eco:b4169;ecoc:C3026_22530;`
- `GeneID:93777652;948683;`
- `GO:GO:0008745; GO:0009253; GO:0030288; GO:0043093; GO:0051301; GO:0071555`
- `EC:3.5.1.28`

## Notes

N-acetylmuramoyl-L-alanine amidase AmiB (EC 3.5.1.28)
