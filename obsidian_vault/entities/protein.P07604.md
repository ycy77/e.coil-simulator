---
entity_id: "protein.P07604"
entity_type: "protein"
name: "tyrR"
source_database: "UniProt"
source_id: "P07604"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tyrR b1323 JW1316"
---

# tyrR

`protein.P07604`

## Static

- Type: `protein`
- Source: `UniProt:P07604`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Dual transcriptional regulator of the TyrR regulon, which includes a number of genes coding for proteins involved in the biosynthesis or transport of the three aromatic amino acids, phenylalanine, tyrosine and tryptophan (PubMed:14614536, PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:4887504, PubMed:7798138, PubMed:7961453, PubMed:8449883). These three aromatic amino acids act as effectors which bind to the TyrR protein to form an active regulatory protein (PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:7961453, PubMed:8106498). Modulates the expression of at least eight unlinked transcription units, including aroF, aroG, aroLM, aroP, mtr, tyrA, tyrB and tyrP (PubMed:14614536, PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:4887504, PubMed:7798138, PubMed:7961453, PubMed:8449883). In most cases TyrR acts as a repressor, but positive effects have been observed on the tyrP gene, which is repressed in the presence of tyrosine and activated at high phenylalanine concentrations (PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:7798138, PubMed:8407813, PubMed:8449883). Is also involved in activation, but not repression, of mtr expression in association with phenylalanine or tyrosine (PubMed:2061290, PubMed:8407813, PubMed:8449883)...

## Biological Role

Component of DNA-binding transcriptional repressor TyrR-L-tyrosine (complex.ecocyc.MONOMER0-162), DNA-binding transcriptional repressor TyrR-L-phenylalanine (complex.ecocyc.MONOMER0-163).

## Annotation

FUNCTION: Dual transcriptional regulator of the TyrR regulon, which includes a number of genes coding for proteins involved in the biosynthesis or transport of the three aromatic amino acids, phenylalanine, tyrosine and tryptophan (PubMed:14614536, PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:4887504, PubMed:7798138, PubMed:7961453, PubMed:8449883). These three aromatic amino acids act as effectors which bind to the TyrR protein to form an active regulatory protein (PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:7961453, PubMed:8106498). Modulates the expression of at least eight unlinked transcription units, including aroF, aroG, aroLM, aroP, mtr, tyrA, tyrB and tyrP (PubMed:14614536, PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:4887504, PubMed:7798138, PubMed:7961453, PubMed:8449883). In most cases TyrR acts as a repressor, but positive effects have been observed on the tyrP gene, which is repressed in the presence of tyrosine and activated at high phenylalanine concentrations (PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:7798138, PubMed:8407813, PubMed:8449883). Is also involved in activation, but not repression, of mtr expression in association with phenylalanine or tyrosine (PubMed:2061290, PubMed:8407813, PubMed:8449883). Acts by binding specifically to TyrR boxes in the promoter region of the target genes (PubMed:10197993, PubMed:1860819, PubMed:7961453, PubMed:8449883, PubMed:8947567). {ECO:0000269|PubMed:10197993, ECO:0000269|PubMed:14614536, ECO:0000269|PubMed:15049824, ECO:0000269|PubMed:1860819, ECO:0000269|PubMed:2061290, ECO:0000269|PubMed:334742, ECO:0000269|PubMed:4399341, ECO:0000269|PubMed:4887504, ECO:0000269|PubMed:7798138, ECO:0000269|PubMed:7961453, ECO:0000269|PubMed:8106498, ECO:0000269|PubMed:8407813, ECO:0000269|PubMed:8449883, ECO:0000269|PubMed:8947567}.

## Outgoing Edges (14)

- `activates` --> [[gene.b0048|gene.b0048]] `RegulonDB` `C` - regulator=TyrR; target=folA; function=+
- `activates` --> [[gene.b1907|gene.b1907]] `RegulonDB` `C` - regulator=TyrR; target=tyrP; function=-+
- `activates` --> [[gene.b3161|gene.b3161]] `RegulonDB` `C` - regulator=TyrR; target=mtr; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-162|complex.ecocyc.MONOMER0-162]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-163|complex.ecocyc.MONOMER0-163]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0112|gene.b0112]] `RegulonDB` `C` - regulator=TyrR; target=aroP; function=-
- `represses` --> [[gene.b0388|gene.b0388]] `RegulonDB` `C` - regulator=TyrR; target=aroL; function=-
- `represses` --> [[gene.b0389|gene.b0389]] `RegulonDB` `C` - regulator=TyrR; target=yaiA; function=-
- `represses` --> [[gene.b0390|gene.b0390]] `RegulonDB` `C` - regulator=TyrR; target=aroM; function=-
- `represses` --> [[gene.b0754|gene.b0754]] `RegulonDB` `C` - regulator=TyrR; target=aroG; function=-
- `represses` --> [[gene.b1907|gene.b1907]] `RegulonDB` `C` - regulator=TyrR; target=tyrP; function=-+
- `represses` --> [[gene.b2600|gene.b2600]] `RegulonDB` `S` - regulator=TyrR; target=tyrA; function=-
- `represses` --> [[gene.b2601|gene.b2601]] `RegulonDB` `S` - regulator=TyrR; target=aroF; function=-
- `represses` --> [[gene.b4054|gene.b4054]] `RegulonDB` `C` - regulator=TyrR; target=tyrB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1323|gene.b1323]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07604`
- `KEGG:ecj:JW1316;eco:b1323;ecoc:C3026_07745;`
- `GeneID:75171448;945879;`
- `GO:GO:0000987; GO:0001216; GO:0003677; GO:0005524; GO:0005829; GO:0006355; GO:0032993; GO:0045892; GO:0045893`

## Notes

HTH-type transcriptional regulatory protein TyrR
