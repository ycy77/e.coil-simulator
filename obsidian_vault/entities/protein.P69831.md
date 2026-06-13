---
entity_id: "protein.P69831"
entity_type: "protein"
name: "gatC"
source_database: "UniProt"
source_id: "P69831"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gatC b2092 JW2076"
---

# gatC

`protein.P69831`

## Static

- Type: `protein`
- Source: `UniProt:P69831`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of GatA, GatB and GatC is involved in galactitol transport. {ECO:0000269|PubMed:8955298}. gatC sequenced from a wild-type isolate of E. coli, strain EC3132, encodes a very hydrophobic protein with similarity to Enzyme IIC of the fructose PTS . Resequencing of multiple isolates of the MG1655 strain has identified several genetic variations compared to the reference sequence, including a 2 bp insertion in gatC in strain ATCC700926 and CGSC7740 . The resulting frameshift in gatC results in truncation after 311 residues and is predicted to disrupt the function of the galactitol permease . Galactitol (also known as dulcitol) is a substrate in the Phenotype-Microarray-Media "Biolog phenotype microarray system" (PM1 well A12) and it is likely that differences in the growth phenotype of E. coli MG1655 on this particular carbon source are due to the genetic variation described above. This EcoliWiki page summarizes the sequence differences that have been reported.

## Biological Role

Component of galactitol-specific PTS enzyme II (complex.ecocyc.CPLX0-231).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of GatA, GatB and GatC is involved in galactitol transport. {ECO:0000269|PubMed:8955298}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-231|complex.ecocyc.CPLX0-231]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (0)

_None._

## External IDs

- `UniProt:P69831`
- `KEGG:ecj:JW2076;ecoc:C3026_11745;`
- `GeneID:75172213;`
- `GO:GO:0005886; GO:0009401; GO:0015577; GO:0015796; GO:0019402; GO:0090584; GO:1902495`

## Notes

PTS system galactitol-specific EIIC component (EIIC-Gat) (Galactitol permease IIC component)
