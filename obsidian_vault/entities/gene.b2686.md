---
entity_id: "gene.b2686"
entity_type: "gene"
name: "emrB"
source_database: "NCBI RefSeq"
source_id: "gene-b2686"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2686"
  - "emrB"
---

# emrB

`gene.b2686`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2686`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

emrB (gene.b2686) is a gene entity. It encodes emrB (protein.P0AEJ0). Encoded protein function: FUNCTION: Part of the tripartite efflux system EmrAB-TolC (PubMed:12482849, PubMed:1409590, PubMed:33065135). The system confers resistance to antibiotics such as nalidixic acid and to various hydrophobic compounds, including CCCP, FCCP and 2,4-dinitrophenol (PubMed:12482849, PubMed:1409590, PubMed:33065135). {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590, ECO:0000269|PubMed:33065135}. EcoCyc product frame: EMRB-MONOMER. Genomic coordinates: 2812616-2814154. EcoCyc protein note: EmrB is the inner membrane subunit of a tripartite efflux pump that is implicated in the export of a variety of mainly hydrophobic compounds - carbonylcyanide m-chlorophenylhydrazone (CCCP), tetrachlorosalicyanide (TSA), nalidixate, phenylmercury acetate and others (see CPLX0-2121 for more details). emrB encodes a predicted integral inner membrane protein with 14 transmembrane domains; emrB is co-transcribed with emrA - predicted to encode a membrane fusion protein . emrB is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . Swimming motility is increased in the emrB Keio collection mutant (BW25113 ΔemrB::kan)...

## Biological Role

Repressed by mprA (protein.P0ACR9). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEJ0|protein.P0AEJ0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=emrB; function=+
- `represses` <-- [[protein.P0ACR9|protein.P0ACR9]] `RegulonDB` `S` - regulator=MprA; target=emrB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008840,ECOCYC:EG11439,GeneID:947167`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2812616-2814154:+; feature_type=gene
