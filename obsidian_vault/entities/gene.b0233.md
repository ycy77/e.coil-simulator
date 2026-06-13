---
entity_id: "gene.b0233"
entity_type: "gene"
name: "yafO"
source_database: "NCBI RefSeq"
source_id: "gene-b0233"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0233"
  - "yafO"
---

# yafO

`gene.b0233`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0233`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafO (gene.b0233) is a gene entity. It encodes yafO (protein.Q47157). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A translation-dependent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome by subsequent expression of antitoxin YafN. Overexpression causes cleavage of a number of mRNAs in a ribosome-dependent fashion. YafO binding to the 50S ribosomal subunit in the translation complex induces mRNA cleavage 3' to the region protected by the ribosome; YafO alone is not able to digest mRNA. {ECO:0000269|PubMed:19617347, ECO:0000269|PubMed:19943910}. EcoCyc product frame: G6117-MONOMER. Genomic coordinates: 252301-252699. EcoCyc protein note: YafO is the toxin of the YafO-YafN toxin-antitoxin system, acting as a ribosome-dependent mRNA interferase. It is a a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems . When it is associated with the ribosome, YafO inhibits protein synthesis by cleaving mRNAs downstream of the translation initiation site . YafO alone does not have endoribonuclease activity . An analysis of the targets and site specificity of YafO showed quite weak cleavage site specificity and limited codon position preference...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47157|protein.Q47157]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yafO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000795,ECOCYC:G6117,GeneID:944916`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:252301-252699:+; feature_type=gene
