---
entity_id: "protein.P46854"
entity_type: "protein"
name: "aaaT"
source_database: "UniProt"
source_id: "P46854"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aaaT yhhY b3441 JW3405"
---

# aaaT

`protein.P46854`

## Static

- Type: `protein`
- Source: `UniProt:P46854`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the N-acetylation of L-phenylalanine and L-methionine using acetyl-CoA as acetyl donor in vitro. Cannot accept L-tyrosine as substrate and propionyl-CoA, succinyl-CoA or (S)-methylmalonyl-CoA as acyl donors (PubMed:27941785). Is also able to acetylate and thus detoxify several nonhydrolyzable aminoacyl adenylates, but not the processed form of the peptide-nucleotide antibiotic microcin C (McC). When overproduced, provides complete resistance to leucyl sulfamoyl adenylate (LSA) and partial resistance to alanyl sulfamoyl adenylate (ASA) and phenylalanyl sulfamoyl adenylate (FSA). Therefore, may protect bacteria from various toxic aminoacyl nucleotides, either exogenous or those generated inside the cell during normal metabolism (PubMed:25002546). {ECO:0000269|PubMed:25002546, ECO:0000269|PubMed:27941785}. YhhY is an acetyltransferase that is able to detoxify nonhydrolyzable aminoacyl adenylates. In vitro, YhhY is able to acetylate the synthetic aminoacyl sulfamoyl adenylates LSA and ISA, but not DSA and ESA . Transcription of yhhY is regulated by Fur .

## Biological Role

Catalyzes acetyl-CoA:L-phenylalanine N-acetyltransferase (reaction.R00693).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the N-acetylation of L-phenylalanine and L-methionine using acetyl-CoA as acetyl donor in vitro. Cannot accept L-tyrosine as substrate and propionyl-CoA, succinyl-CoA or (S)-methylmalonyl-CoA as acyl donors (PubMed:27941785). Is also able to acetylate and thus detoxify several nonhydrolyzable aminoacyl adenylates, but not the processed form of the peptide-nucleotide antibiotic microcin C (McC). When overproduced, provides complete resistance to leucyl sulfamoyl adenylate (LSA) and partial resistance to alanyl sulfamoyl adenylate (ASA) and phenylalanyl sulfamoyl adenylate (FSA). Therefore, may protect bacteria from various toxic aminoacyl nucleotides, either exogenous or those generated inside the cell during normal metabolism (PubMed:25002546). {ECO:0000269|PubMed:25002546, ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R00693|reaction.R00693]] `KEGG` `database` - via EC:2.3.1.53

## Incoming Edges (1)

- `encodes` <-- [[gene.b3441|gene.b3441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46854`
- `KEGG:ecj:JW3405;eco:b3441;ecoc:C3026_18645;`
- `GeneID:75202285;947943;`
- `GO:GO:0008080; GO:0016747; GO:0050176; GO:0103045`
- `EC:2.3.1.-; 2.3.1.53`

## Notes

L-amino acid N-acetyltransferase AaaT (L-methionine N-acetyltransferase) (EC 2.3.1.-) (L-phenylalanine N-acetyltransferase) (EC 2.3.1.53)
