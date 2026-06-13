---
entity_id: "gene.b0366"
entity_type: "gene"
name: "tauB"
source_database: "NCBI RefSeq"
source_id: "gene-b0366"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0366"
  - "tauB"
---

# tauB

`gene.b0366`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0366`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tauB (gene.b0366) is a gene entity. It encodes tauB (protein.Q47538). Encoded protein function: FUNCTION: Part of the ABC transporter complex TauABC involved in taurine import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01714, ECO:0000269|PubMed:10781534, ECO:0000269|PubMed:8808933}. EcoCyc product frame: TAUB-MONOMER. EcoCyc synonyms: yaiQ, ssiB. Genomic coordinates: 386207-386974. EcoCyc protein note: TauB is the predicted ATP-binding subunit of a taurine uptake system; TauB contains sequence motifs conserved in ATP-binding cassette (ABC) proteins . tauBC in-frame deletion mutants are unable to grow with taurine as a sulfur source and show reduced growth with decanesulfonate as a sulfur source .

## Biological Role

Activated by cysB (protein.P0A9F3), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47538|protein.Q47538]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=tauB; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=tauB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001259,ECOCYC:G6218,GeneID:945027`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:386207-386974:+; feature_type=gene
