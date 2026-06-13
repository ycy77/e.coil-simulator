---
entity_id: "gene.b0511"
entity_type: "gene"
name: "allW"
source_database: "NCBI RefSeq"
source_id: "gene-b0511"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0511"
  - "allW"
---

# allW

`gene.b0511`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0511`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allW (gene.b0511) is a gene entity. It encodes ybbW (protein.P75712). Encoded protein function: FUNCTION: Uptake of allantoin into the cell. {ECO:0000250|UniProtKB:P94575}. EcoCyc product frame: B0511-MONOMER. EcoCyc synonyms: allP, glxB2, ybbW. Genomic coordinates: 537633-539087. EcoCyc protein note: E. coli is able to utilize allantoin as a source of nitrogen under anaerobic conditions . allW, located within an allantoin utilization gene cluster, encodes an allantoin transporter that relies on binding to allB-encoded CPLX-64 for activity; AllW-AllB physical association is enhanced in the presence of glyoxylate . AllW and AllB constitute a functional 'membrane transport metabolon' . AllW (formerly YbbW) has sequence similarity to the allantoin permease of Saccharomyces cerevisiae . Accumulation of the cationic fluorescent dye 3,3'-dipropylthiadicarbocyanine iodide (diS-C3) is greater in ybbW knockout cells compared to wild type . In the Transporter Classification Database AllW is a member of the Nucleobase:Cation Symporter-1 (NCS1) family within the Amino Acid-Polyamine-Organocation (APC) superfamily.

## Biological Role

Repressed by allR (protein.P0ACN4). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75712|protein.P75712]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=allW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=allW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001764,ECOCYC:G6280,GeneID:945138`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:537633-539087:+; feature_type=gene
