---
entity_id: "gene.b3725"
entity_type: "gene"
name: "pstB"
source_database: "NCBI RefSeq"
source_id: "gene-b3725"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3725"
  - "pstB"
---

# pstB

`gene.b3725`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3725`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pstB (gene.b3725) is a gene entity. It encodes pstB (protein.P0AAH0). Encoded protein function: FUNCTION: Part of the ABC transporter complex PstSACB involved in phosphate import. Responsible for energy coupling to the transport system. EcoCyc product frame: PSTB-MONOMER. EcoCyc synonyms: phoT. Genomic coordinates: 3907593-3908366. EcoCyc protein note: PstB is the ATP-binding subunit of a high affinity phosphate specific uptake system; PstB contains signature motifs conserved in ATP binding cassette (ABC) proteins . PstB interacts directly with PhoU and this interaction is implicated in signal transduction to PhoR; PstB, PhoU and PhoR may form a phosphate-sensing complex at the cell membrane . pstB belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639). Activated by phoB (protein.P0AFJ5), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAH0|protein.P0AAH0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=pstB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pstB; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012179,ECOCYC:EG10783,GeneID:948240`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3907593-3908366:-; feature_type=gene
