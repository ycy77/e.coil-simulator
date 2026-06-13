---
entity_id: "gene.b3606"
entity_type: "gene"
name: "trmL"
source_database: "NCBI RefSeq"
source_id: "gene-b3606"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3606"
  - "trmL"
---

# trmL

`gene.b3606`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3606`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trmL (gene.b3606) is a gene entity. It encodes trmL (protein.P0AGJ7). Encoded protein function: FUNCTION: Methylates the ribose at the nucleotide 34 wobble position in the two leucyl isoacceptors tRNA(Leu)(CmAA) and tRNA(Leu)(cmnm5UmAA). Catalyzes the methyl transfer from S-adenosyl-L-methionine to the 2'-OH of the wobble nucleotide. Recognition of the target requires a pyridine at position 34 and N(6)-(isopentenyl)-2-methylthioadenosine at position 37. {ECO:0000255|HAMAP-Rule:MF_01885, ECO:0000269|PubMed:20855540}. EcoCyc product frame: EG11888-MONOMER. EcoCyc synonyms: yibK. Genomic coordinates: 3781215-3781688. EcoCyc protein note: TrmL is the methyltransferase responsible for 2'-O-methylation of the wobble nucleotide 34 (cytidine or uridine) ribose in both tRNALeu isoacceptors . It also 2'-O-methylates a minor fraction of 5-methoxycarbonylmethoxy-modified U34 of serT-tRNA . TrmL showed no methyltransferase activity with certain synthetic tRNA substrates ; the enzyme requires the presence of the ms2i6 modification at the A37 nucleotide for activity . In addition, the A35 nucleotide functions as an identity element for substrate recognition by TrmL . TrmL only accepts pyrimidine nucleotides at the wobble position; additional identity elements within the anticodon loop were identified . TrmL belongs to the SPOUT superfamily of methyltransferases and is a dimer in solution...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGJ7|protein.P0AGJ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011790,ECOCYC:EG11888,GeneID:948119`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3781215-3781688:+; feature_type=gene
