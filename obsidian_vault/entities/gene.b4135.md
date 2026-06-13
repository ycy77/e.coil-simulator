---
entity_id: "gene.b4135"
entity_type: "gene"
name: "dicD"
source_database: "NCBI RefSeq"
source_id: "gene-b4135"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4135"
  - "dicD"
---

# dicD

`gene.b4135`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4135`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dicD (gene.b4135) is a gene entity. It encodes yjdC (protein.P0ACU7). Encoded protein function: HTH-type transcriptional regulator YjdC EcoCyc product frame: EG12176-MONOMER. EcoCyc synonyms: yjdC, cutA3. Genomic coordinates: 4362733-4363308. EcoCyc protein note: DicD, previously named YjdC, is involved in division control . It which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the RutR family of transcription factors . Upstream of the dicD gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the dicD gene is affected by heat stress . In E. coli BL21(DE3), DicD protein levels were found to be increased in response to the thiol-specific oxidant 2-hydroxyethyl disulfide and guanidine hydrochloride . Interconnectivity between the dicD gene and the gene encoding the TF DicA was found . Deletion of the dicD gene rescued the growth defect of a dicA hypomorphic allele mutant strain. In a dicA hypomorphic allele mutant strain, the dicD transcript showed a 3-fold decrease relative to the wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACU7|protein.P0ACU7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013537,ECOCYC:EG12176,GeneID:948650`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4362733-4363308:-; feature_type=gene
