---
entity_id: "gene.b4637"
entity_type: "gene"
name: "uof"
source_database: "NCBI RefSeq"
source_id: "gene-b4637"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4637"
  - "uof"
---

# uof

`gene.b4637`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4637`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uof (gene.b4637) is a gene entity. It encodes uof (protein.A8DYP9). Encoded protein function: FUNCTION: Cotranscribed with fur, it is essential for fur translation. The fur ribosomal binding site (RBS) is occluded by the 5'-mRNA secondary structure, which is opened by uof translation. {ECO:0000269|PubMed:17268550}. EcoCyc product frame: MONOMER0-2801. Genomic coordinates: 710639-710725. EcoCyc protein note: Uof appears to function in an indirect role to regulate abundance of the iron-responsive transcriptional regulator Fur at the posttranscriptional level. It is not known whether the Uof peptide itself has a role in iron metabolism . Translation of uof may be regulated by iron-responsive decoding and is downregulated by the small RNA RyhB. Synthesis of Fur is translationally coupled to that of Uof and is therefore indirectly downregulated by RyhB as well . Uof: "upstream of fur" Reviews:

## Biological Role

Repressed by ryhB (gene.b4451). Activated by soxS (protein.P0A9E2), oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A8DYP9|protein.A8DYP9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=uof; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=uof; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=uof; function=-

## External IDs

- `Dbxref:ECOCYC:G0-10580,GeneID:5625562`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:710639-710725:-; feature_type=gene
