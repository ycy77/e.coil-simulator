---
entity_id: "protein.P22188"
entity_type: "protein"
name: "murE"
source_database: "UniProt"
source_id: "P22188"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murE b0085 JW0083"
---

# murE

`protein.P22188`

## Static

- Type: `protein`
- Source: `UniProt:P22188`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the addition of meso-diaminopimelic acid to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (UMAG) in the biosynthesis of bacterial cell-wall peptidoglycan. Is also able to use many meso-diaminopimelate analogs as substrates, although much less efficiently, but not L-lysine. {ECO:0000269|PubMed:11124264, ECO:0000269|PubMed:2269304, ECO:0000269|PubMed:3905407}. UDP-N-acetylmuramoylalanyl-D-glutamate 2,6-diaminopimelate ligase (MurE) catalyzes the addition of the third amino acid, meso-diaminopimelate, to the peptide moiety of the monomer unit of peptidoglycan . The enzyme's ability to use the LL-DAP isomer at a low level leads to the incorporation of LL-DAP into peptidoglycan in a DIAMINOPIMEPIM-MONOMER (dapF) mutant . A crystal structure of the enzyme has been solved at 2Å resolution, allowing the identification of residues involved in catalysis. The Lys224 residue within the active site is carbamylated , and this modification appears to be required for enzymatic activity . Temperature-sensitive murE mutants have been isolated , and the genetic defects of the murE1 allele has been identified . In a dapA mutant, cystathionine or lanthionine will substitute for diaminopimelate . Repression of murE expression with a synthetic small RNA leads to increased production of cadaverine in an engineered strain...

## Biological Role

Catalyzes UDP-N-acetylmuramoyl-L-alanyl-D-glutamate:(L)-meso-2,6-diaminoheptanedioate gamma-ligase (ADP-forming); (reaction.R02788), UDP-NACMURALGLDAPLIG-RXN (reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the addition of meso-diaminopimelic acid to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (UMAG) in the biosynthesis of bacterial cell-wall peptidoglycan. Is also able to use many meso-diaminopimelate analogs as substrates, although much less efficiently, but not L-lysine. {ECO:0000269|PubMed:11124264, ECO:0000269|PubMed:2269304, ECO:0000269|PubMed:3905407}.

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02788|reaction.R02788]] `KEGG` `database` - via EC:6.3.2.13
- `catalyzes` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0085|gene.b0085]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22188`
- `KEGG:ecj:JW0083;eco:b0085;ecoc:C3026_00330;`
- `GeneID:944791;`
- `GO:GO:0000287; GO:0005524; GO:0005829; GO:0008360; GO:0008765; GO:0009252; GO:0051301; GO:0071555`
- `EC:6.3.2.13`

## Notes

UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme) (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase) (UDP-N-acetylmuramyl-tripeptide synthetase)
