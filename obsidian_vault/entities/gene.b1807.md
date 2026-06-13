---
entity_id: "gene.b1807"
entity_type: "gene"
name: "tsaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1807"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1807"
  - "tsaB"
---

# tsaB

`gene.b1807`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1807`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsaB (gene.b1807) is a gene entity. It encodes tsaB (protein.P76256). Encoded protein function: FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaD and TsaE. TsaB seems to play an indirect role in the t(6)A biosynthesis pathway, possibly in regulating the core enzymatic function of TsaD. In fact, can act as a protease that specifically degrades TsaD in vitro; therefore TsaB may post-translationally regulate cellular pools of TsaD via proteolytic degradation. Does not show sialoglycoprotease activity against glycophorin A. {ECO:0000269|PubMed:19376873, ECO:0000269|PubMed:22378793}. EcoCyc product frame: G6991-MONOMER. EcoCyc synonyms: yeaZ. Genomic coordinates: 1890572-1891267. EcoCyc protein note: TsaB is involved in the biosynthesis of the threonylcarbamoyladenosine (t6A) residue at position 37 of ANN-decoding tRNAs. A mixture of purified G7698-MONOMER TsaC, EG11171-MONOMER TsaD, TsaB, and EG11757-MONOMER TsaE proteins catalyzes formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . The three essential proteins TsaE, TsaB and TsaD form an interaction network...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76256|protein.P76256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006013,ECOCYC:G6991,GeneID:946304`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1890572-1891267:-; feature_type=gene
