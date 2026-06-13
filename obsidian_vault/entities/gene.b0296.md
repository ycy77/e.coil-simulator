---
entity_id: "gene.b0296"
entity_type: "gene"
name: "ykgM"
source_database: "NCBI RefSeq"
source_id: "gene-b0296"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0296"
  - "ykgM"
---

# ykgM

`gene.b0296`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0296`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgM (gene.b0296) is a gene entity. It encodes ykgM (protein.P0A7N1). Encoded protein function: Large ribosomal subunit protein bL31B (50S ribosomal protein L31 type B) EcoCyc product frame: G6167-MONOMER. Genomic coordinates: 312514-312777. EcoCyc protein note: Ribosomal protein L31B (YkgM) was first identified as a precursor of RpmE, the EG10889-MONOMER, in E. coli strain W3110 and then recognized as a paralog of RpmE . It is present in stationary phase ribosomes , in ribosomes prepared from a ΔrpmE zur::IS2 mutant, and it functionally substitutes for L31 . Under lower-temperature growth conditions and in growth competition experiments, L31 confers higher fitness than L31B. In addition, L31B-containing ribosomes show reduced processivity and increased frame shifting . The expression of the gene ykgM is repressed by the protein YkgM, but it is not clear at which expression level this regulation happens; it could be at the level of transcription, mRNA stability, or translation at more than one level . This regulation involves a hairpin structure in the ykgM mRNA and the N-terminal domain of YkgM . YkgM has lost the predicted metal-binding "zinc ribbon" motif and was shown to lack bound Zn2+, in contrast to L31 . The authors propose a model where YkgM can provide the function of L31 in the ribosome under zinc-limited conditions...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7N1|protein.P0A7N1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001021,ECOCYC:G6167,GeneID:944960`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:312514-312777:-; feature_type=gene
