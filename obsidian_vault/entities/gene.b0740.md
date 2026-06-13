---
entity_id: "gene.b0740"
entity_type: "gene"
name: "tolB"
source_database: "NCBI RefSeq"
source_id: "gene-b0740"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0740"
  - "tolB"
---

# tolB

`gene.b0740`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0740`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tolB (gene.b0740) is a gene entity. It encodes tolB (protein.P0A855). Encoded protein function: FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:17233825). TolB occupies a key intermediary position in the Tol-Pal system because it communicates directly with both membrane-embedded components, Pal in the outer membrane and TolA in the inner membrane (PubMed:19696740). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of some colicins A (PubMed:11994151, PubMed:2687247, PubMed:7929011). {ECO:0000269|PubMed:11994151, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:19696740, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000305|PubMed:2687247, ECO:0000305|PubMed:7929011}. EcoCyc product frame: EG11008-MONOMER. EcoCyc synonyms: lky, lkyA, tol-3. Genomic coordinates: 777740-779032. EcoCyc protein note: TolB is a periplasmic component of the Tol-Pal system - a group of interacting proteins which span the cell envelope of E. coli K-12...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator Fis (complex.ecocyc.CPLX0-7705), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A855|protein.P0A855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7705|complex.ecocyc.CPLX0-7705]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tolB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002517,ECOCYC:EG11008,GeneID:945429`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:777740-779032:+; feature_type=gene
