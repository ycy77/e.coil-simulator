---
entity_id: "gene.b2622"
entity_type: "gene"
name: "intA"
source_database: "NCBI RefSeq"
source_id: "gene-b2622"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2622"
  - "intA"
---

# intA

`gene.b2622`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2622`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

intA (gene.b2622) is a gene entity. It encodes intA (protein.P32053). Encoded protein function: FUNCTION: Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. Part of the cryptic P4-like prophage CP4-57, it excises the prophage when overexpressed, which also requires integration host factor (encoded by ihfA and ihfB) (PubMed:7511583). Overexpression of AlpA leads to excision of the CP4-57 prophage, which inactivates ssrA (the gene upstream of the prophage) that encodes tmRNA which is required to rescue stalled ribosomes in a process known as trans-translation (PubMed:7511582). {ECO:0000269|PubMed:7511583}. EcoCyc product frame: EG11783-MONOMER. EcoCyc synonyms: intX, slpA. Genomic coordinates: 2756159-2757400. EcoCyc protein note: IntA (SlpA) is a prophage integrase. It is part of the CP4-57 cryptic prophage that is similar to bacteriophage P4. Overexpression of IntA leads to excision and loss of CP4-57 . Expression of intA is transcriptionally regulated by AlpA . Increased synthesis of IntA results in excision of the CP4-57 cryptic prophage, an event which inactivates the gene upstream of intA, ssrA, encoding SSRA-RNA . CP4-57: "cryptic P4-like prophage at min 57" SlpA: "suppressor of Lon-like protease"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32053|protein.P32053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008630,ECOCYC:EG11783,GeneID:946160`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2756159-2757400:+; feature_type=gene
