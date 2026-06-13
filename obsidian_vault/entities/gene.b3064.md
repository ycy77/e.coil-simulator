---
entity_id: "gene.b3064"
entity_type: "gene"
name: "tsaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3064"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3064"
  - "tsaD"
---

# tsaD

`gene.b3064`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3064`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsaD (gene.b3064) is a gene entity. It encodes tsaD (protein.P05852). Encoded protein function: FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaE and TsaB. TsaD likely plays a direct catalytic role in this reaction. May also be involved in the metabolism of glycated proteins, but does not show sialoglycoprotease activity against glycophorin A. {ECO:0000269|PubMed:20824107, ECO:0000269|PubMed:21183954, ECO:0000269|PubMed:22378793}. EcoCyc product frame: EG11171-MONOMER. EcoCyc synonyms: gcp, ygjD. Genomic coordinates: 3209530-3210543. EcoCyc protein note: TsaD is involved in the biosynthesis of the threonylcarbamoyladenosine (t6A) residue at position 37 of ANN-decoding tRNAs. A mixture of purified G7698-MONOMER TsaC, TsaD, G6991-MONOMER TsaB, and EG11757-MONOMER TsaE proteins catalyzes formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . The three essential proteins TsaE, TsaB and TsaD form an interaction network. TsaD interacts with TsaB, but not with TsaE. Purified TsaD can oligomerize, with the major form being a dimer...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05852|protein.P05852]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010058,ECOCYC:EG11171,GeneID:947578`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3209530-3210543:-; feature_type=gene
