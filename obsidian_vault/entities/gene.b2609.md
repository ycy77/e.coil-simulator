---
entity_id: "gene.b2609"
entity_type: "gene"
name: "rpsP"
source_database: "NCBI RefSeq"
source_id: "gene-b2609"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2609"
  - "rpsP"
---

# rpsP

`gene.b2609`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2609`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsP (gene.b2609) is a gene entity. It encodes rpsP (protein.P0A7T3). Encoded protein function: FUNCTION: In addition to being a ribosomal protein, S16 also has a cation-dependent endonuclease activity. {ECO:0000269|PubMed:8730873}.; FUNCTION: In-frame fusions with the ribosome maturation factor rimM suppress mutations in the latter (probably due to increased rimM expression) and are found in translationally active 70S ribosomes. {ECO:0000269|PubMed:11514519}. EcoCyc product frame: EG10915-MONOMER. Genomic coordinates: 2745937-2746185. EcoCyc protein note: The S16 protein is a component of the 30S subunit of the ribosome and is essential for viability . S16 interacts with the 5' domain of 16S rRNA . Binding of S16 to 16S rRNA is dependent on prior binding of S4 and S20 . Subsequent binding of S16 suppresses non-native assembly intermediates and drives a conformational switch at helix 3 of 16S rRNA, stabilizing the decoding center of the 30S subunit . Ensemble FRET experiments confirmed that S16 destabilizes the non-native S4-rRNA conformation . S16 was also shown to be a DNA-binding protein with Mg2+-Mn2+-dependent endonuclease activity . S16 preferentially binds to cruciform DNA structures; its endonuclease activity appears to be sequence-specific . S16 may bind Zn2+ . Expression of rpsP is induced 16-fold upon exposure of cells to the biocide polyhexamethylene biguanide .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7T3|protein.P0A7T3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008583,ECOCYC:EG10915,GeneID:947103`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2745937-2746185:-; feature_type=gene
