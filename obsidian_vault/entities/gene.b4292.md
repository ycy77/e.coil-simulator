---
entity_id: "gene.b4292"
entity_type: "gene"
name: "fecR"
source_database: "NCBI RefSeq"
source_id: "gene-b4292"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4292"
  - "fecR"
---

# fecR

`gene.b4292`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4292`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecR (gene.b4292) is a gene entity. It encodes fecR (protein.P23485). Encoded protein function: FUNCTION: Required for transcriptional activation of the fecABCDE operon by sigma factor FecI (PubMed:2254251, PubMed:7752886). Undergoes sequential cleavage to produce an N-terminal cytoplasmic fragment which is released from the membrane and binds to FecI, allowing it to activate transcription of the fecABCDE operon which mediates ferric citrate transport (PubMed:33865858). In the absence of citrate, FecR inactivates FecI (PubMed:2254251). {ECO:0000269|PubMed:2254251, ECO:0000269|PubMed:33865858, ECO:0000269|PubMed:7752886}. EcoCyc product frame: EG10292-MONOMER. Genomic coordinates: 4516764-4517717. EcoCyc protein note: FecR is an inner membrane protein which participates in a trans-envelope signaling pathway to the iron starvation responsive, extracytoplasmic function (ECF) sigma factor, PD00440 FecI; FecR transmits a signal that is initiated by ferric chloride binding to the TonB-dependent outer membrane transporter EG10286-MONOMER FecA; FecR and FecI constitute a non-canonical anti-sigma factor/sigma factor pair; the molecular details of signal transmission remain unclear (see ). FecR is required for FecI-mediated transcriptional regulation of the fec-encoded ferric citrate transport genes (fecABCD); ; (and see )...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), slyA (protein.P0A8W2), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23485|protein.P23485]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=fecR; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=fecR; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014070,ECOCYC:EG10292,GeneID:949104`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4516764-4517717:-; feature_type=gene
