---
entity_id: "gene.b1432"
entity_type: "gene"
name: "insQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1432"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1432"
  - "insQ"
---

# insQ

`gene.b1432`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1432`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insQ (gene.b1432) is a gene entity. It encodes insQ (protein.P76102). Encoded protein function: FUNCTION: An RNA-guided dsDNA endonuclease. When guided by an RNA derived from the right-end element of its insertion sequence element (IS), cleaves DNA downstream of the transposon-associated motif (TAM). Cleaves supercoiled and linear DNA in a staggered manner 15-21 bases from the TAM yielding 5'-overhangs. Binds reRNA, an approximately 150 nucleotide base sRNA derived from the 3' end of its own gene, the right end (RE) of the insertion sequence (IS) plus sequence downstream of the IS. {ECO:0000250|UniProtKB:Q7DF80}.; FUNCTION: Not required for transposition of the insertion element. The corresponding transposase in strains MG1655 and W3110 is a truncated pseudogene (yncK). {ECO:0000305}. EcoCyc product frame: G6743-MONOMER. EcoCyc synonyms: ydcM, tnpB. Genomic coordinates: 1503657-1504865. EcoCyc protein note: The insertion sequence in which this gene is found (group IS609) is identified in the ISfinder database () as falling within IS family IS200/IS605. The IS609 group is also found in some other E. coli, such as substrain W3110 and the pathogenic substrain O157:H7, and some Shigella species...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76102|protein.P76102]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004778,ECOCYC:G6743,GeneID:944942`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1503657-1504865:+; feature_type=gene
