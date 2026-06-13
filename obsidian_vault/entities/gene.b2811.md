---
entity_id: "gene.b2811"
entity_type: "gene"
name: "csdE"
source_database: "NCBI RefSeq"
source_id: "gene-b2811"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2811"
  - "csdE"
---

# csdE

`gene.b2811`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2811`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csdE (gene.b2811) is a gene entity. It encodes csdE (protein.P0AGF2). Encoded protein function: FUNCTION: Stimulates the cysteine desulfurase activity of CsdA. Contains a cysteine residue (Cys-61) that acts to accept sulfur liberated via the desulfurase activity of CsdA. May be able to transfer sulfur to TcdA/CsdL. Seems to support the function of TcdA in the generation of cyclic threonylcarbamoyladenosine at position 37 (ct(6)A37) in tRNAs that read codons beginning with adenine. Does not appear to participate in Fe/S biogenesis. {ECO:0000269|PubMed:15901727, ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255}. EcoCyc product frame: G7455-MONOMER. EcoCyc synonyms: ygdK. Genomic coordinates: 2944542-2944985. EcoCyc protein note: CsdA and CsdE combine to form the CSD sulfur transfer system. CsdA activity doubles in the presence of CsdE, which contains a cysteine residue (C61) that acts to accept sulfur liberated via the desulfinase activity of CsdA . A physiologically relevant sulfur acceptor from CsdE has not been identified yet. CsdE also interacts with and may be able to transfer sulfur to TcdA ; a transient physical interaction between CsdE and TcdA was also shown by NMR and crosslinking experiments . Additional proteins that interact with CsdE have been identified . The pKa of the C61 residue was determined to be 6.5...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGF2|protein.P0AGF2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009220,ECOCYC:G7455,GeneID:947274`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2944542-2944985:+; feature_type=gene
