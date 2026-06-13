---
entity_id: "gene.b0629"
entity_type: "gene"
name: "ybeF"
source_database: "NCBI RefSeq"
source_id: "gene-b0629"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0629"
  - "ybeF"
---

# ybeF

`gene.b0629`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0629`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeF (gene.b0629) is a gene entity. It encodes ybeF (protein.P30979). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YbeF EcoCyc product frame: EG11594-MONOMER. Genomic coordinates: 660425-661378. EcoCyc protein note: YbeF was predicted to be a LysR-type transcription factor . It contains a helix-turn-helix motif to bind DNA in its N-terminal domain. YbeF DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . It was predicted to regulate genes related to cell division . However, the effect of YbeF on the transcription of any gene has not yet been demonstrated . The transcriptional response to deletion of YbeF was characterized by RNA-seq in M9 minimal medium supplemented by 7 mM l-threonine . In the YbeF knockout mutant, the lrhA gene was downregulated and flhC was upregulated in comparison with the wild type, and it was proposed that YbeF could be involved in flagella biosynthesis. YbeF is a paralog of CitR with 30% identity. In systematic studies of oligomerization, it was shown that some members of the LysR family, like YbeF, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30979|protein.P30979]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002158,ECOCYC:EG11594,GeneID:945219`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:660425-661378:-; feature_type=gene
