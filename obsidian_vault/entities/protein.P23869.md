---
entity_id: "protein.P23869"
entity_type: "protein"
name: "ppiB"
source_database: "UniProt"
source_id: "P23869"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1606970, ECO:0000269|PubMed:2007139}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppiB b0525 JW0514"
---

# ppiB

`protein.P23869`

## Static

- Type: `protein`
- Source: `UniProt:P23869`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1606970, ECO:0000269|PubMed:2007139}.

## Enriched Summary

FUNCTION: PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. {ECO:0000269|PubMed:1606970, ECO:0000269|PubMed:2007139}. PpiB is a single-domain peptidyl-prolyl cis-trans-isomerase (PPIase) that is the main contributor to PPIase activity in the cytoplasm . PPIases catalyze the conformational isomerization of prolyl residues in peptides; cis-trans isomerization of prolyl peptide bonds is a slow step in protein folding. PpiB was shown to improve the efficiency of bovine protein disulfide isomerase as a catalyst of oxidative protein folding and to catalyze the refolding of denatured type III collagen . Unlike the eukaryotic cyclophilins, PpiB activity is only inhibited by high concentrations of cyclosporin A or FK506 . Putative substrates of PpiB activity, including DnaK, PflB and Pta, have been identified . Consistent with its role as the major cytoplasmic PPIase, PpiB has a large number of substrates . Crystal structures in two different conformations and a solution structure of PpiB have been determined. Refolding kinetics of the protein have been studied . Amino acid residues that are important for PpiB function have been identified . A mutant in the potential active site residue R43 was assayed for potential substrate binding and PPIase activity...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

FUNCTION: PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. {ECO:0000269|PubMed:1606970, ECO:0000269|PubMed:2007139}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0525|gene.b0525]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23869`
- `KEGG:ecj:JW0514;eco:b0525;ecoc:C3026_02575;`
- `GeneID:949038;`
- `GO:GO:0003755; GO:0005829; GO:0006457`
- `EC:5.2.1.8`

## Notes

Peptidyl-prolyl cis-trans isomerase B (PPIase B) (EC 5.2.1.8) (Rotamase B)
