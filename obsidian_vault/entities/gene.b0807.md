---
entity_id: "gene.b0807"
entity_type: "gene"
name: "rlmF"
source_database: "NCBI RefSeq"
source_id: "gene-b0807"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0807"
  - "rlmF"
---

# rlmF

`gene.b0807`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0807`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmF (gene.b0807) is a gene entity. It encodes rlmF (protein.P75782). Encoded protein function: FUNCTION: Specifically methylates the adenine in position 1618 of 23S rRNA. {ECO:0000269|PubMed:18021804}. EcoCyc product frame: G6416-MONOMER. EcoCyc synonyms: ybiN. Genomic coordinates: 842332-843258. EcoCyc protein note: RlmF is the methyltransferase responsible for methylation of 23S rRNA at the N6 position of the A1618 nucleotide . In vitro, RlmF can methylate A1618 in LiCl ribosomal core particles (a model for early ribosomal assembly intermediates), but not in protein-free 23S rRNA or more fully assembled ribosomal particles . RlmF is most similar to several m2G methyltransferases and was thus expected to confer m2G1516 methyltransferase activity . Predicted catalytic residues and a predicted reaction mechanism are discussed . Both an rlmF null mutant and a strain overexpressing rlmF show a growth defect . RlmF: "rRNA large subunit methyltransferase F"

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75782|protein.P75782]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=rlmF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002757,ECOCYC:G6416,GeneID:944938`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:842332-843258:+; feature_type=gene
