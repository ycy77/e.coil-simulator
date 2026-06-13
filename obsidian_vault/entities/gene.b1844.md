---
entity_id: "gene.b1844"
entity_type: "gene"
name: "exoX"
source_database: "NCBI RefSeq"
source_id: "gene-b1844"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1844"
  - "exoX"
---

# exoX

`gene.b1844`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1844`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

exoX (gene.b1844) is a gene entity. It encodes exoX (protein.P0AEK0). Encoded protein function: FUNCTION: Capable of degrading both single-strand and double-strand DNA with 3' to 5' polarity. Has higher affinity for ssDNA ends than for dsDNA. EcoCyc product frame: G7016-MONOMER. EcoCyc synonyms: yobC. Genomic coordinates: 1926120-1926782. EcoCyc protein note: Exonuclease X is a DNA repair enzyme involved in mismatch repair, and is able to degrade both single-stranded and duplex DNA . Exonuclease X exhibits 3'-5' polarity, and has a high catalytic rate and affinity for single-stranded DNA . An exoX deletion mutant had increased sensitivity to UV irradiation in a background strain lacking several other DNA repair enzymes . A recJ, exoI, exoVII, and exoX mutant had no methyl-directed mismatch repair, had an increased mutation rate , and had a cold-sensitivity phenotype suppressible by mutations of genes involved in activities upstream of these four genes in methyl-directed mismatch repair . Each of the four proteins was able to perform complete mismatch repair without the aid of the other three . Overexpression of exoX can complement an exonuclease I mutation in UV damage repair . ExoX has also been shown to be involved in stabilization of tandem repeats due to its mismatch repair and single-strand exonuclease activities, helping to prevent deletion events .

## Biological Role

Repressed by ompR (protein.P0AA16).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEK0|protein.P0AEK0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=exoX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006131,ECOCYC:G7016,GeneID:946361`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1926120-1926782:+; feature_type=gene
