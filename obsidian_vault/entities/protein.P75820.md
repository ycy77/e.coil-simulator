---
entity_id: "protein.P75820"
entity_type: "protein"
name: "amiD"
source_database: "UniProt"
source_id: "P75820"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amiD ybjR b0867 JW0851"
---

# amiD

`protein.P75820`

## Static

- Type: `protein`
- Source: `UniProt:P75820`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}.

## Enriched Summary

N-acetylmuramoyl-L-alanine amidase AmiD (EC 3.5.1.28) AmiD is an N-acetylmuramic acid-L-alanine amidase responsible for cleaving the bond between muramic acid and L-alanine within murein, muropeptides, and anhydro-muropeptides. AmiD is an outer membrane lipoprotein . nagB nagZ ampD amiD mutants are unable to release murein tripeptide from GlcNAc-anhMurNAc-tripeptide while the nagB nagZ ampD mutant is able to do so . Assays of purified AmiD show it prefers GlcNAc-anhMurNAc-peptides or GlcNAc-MurNAc-peptides as substrates over those lacking GlcNAc . Purified AmiD was shown to hydrolyse peptidoglycan fragments that have at least three amino acids in their peptide chains and the enzyme activity was inhibited by its substrate in vitro . Review:

## Biological Role

Catalyzes N-acetylmuramoyl-Ala amidohydrolase (reaction.R04112), RXN0-5225 (reaction.ecocyc.RXN0-5225). Bound by Zinc cation (molecule.C00038).

## Annotation

N-acetylmuramoyl-L-alanine amidase AmiD (EC 3.5.1.28)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04112|reaction.R04112]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` --> [[reaction.ecocyc.RXN0-5225|reaction.ecocyc.RXN0-5225]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0867|gene.b0867]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75820`
- `KEGG:ecj:JW0851;eco:b0867;ecoc:C3026_05395;`
- `GeneID:945494;`
- `GO:GO:0008270; GO:0008745; GO:0009253; GO:0009254; GO:0009279; GO:0009392; GO:0019867; GO:0071555`
- `EC:3.5.1.28`

## Notes

N-acetylmuramoyl-L-alanine amidase AmiD (EC 3.5.1.28)
