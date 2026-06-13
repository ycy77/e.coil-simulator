---
entity_id: "gene.b4287"
entity_type: "gene"
name: "fecE"
source_database: "NCBI RefSeq"
source_id: "gene-b4287"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4287"
  - "fecE"
---

# fecE

`gene.b4287`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4287`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecE (gene.b4287) is a gene entity. It encodes fecE (protein.P15031). Encoded protein function: FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:2651410). Binds ATP (PubMed:1526456). Probably responsible for energy coupling to the transport system (PubMed:1526456). {ECO:0000269|PubMed:1526456, ECO:0000269|PubMed:2651410}. EcoCyc product frame: FECE-MONOMER. Genomic coordinates: 4510690-4511457. EcoCyc protein note: fecE encodes a hydrophilic protein that is found in the membrane fraction; it contains conserved ATP-binding sites and is predicted to be the peripheral membrane, ATP-binding protein of the ferric dicitrate ABC transport system . Cloned, overexpressed FecE binds ATP .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by fecI (protein.P23484).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15031|protein.P15031]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P23484|protein.P23484]] `RegulonDB` `C` - sigma=sigma19; target=fecE; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014057,ECOCYC:EG10290,GeneID:948819`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4510690-4511457:-; feature_type=gene
