---
entity_id: "gene.b0904"
entity_type: "gene"
name: "focA"
source_database: "NCBI RefSeq"
source_id: "gene-b0904"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0904"
  - "focA"
---

# focA

`gene.b0904`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0904`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

focA (gene.b0904) is a gene entity. It encodes focA (protein.P0AC23). Encoded protein function: FUNCTION: Involved in the bidirectional transport of formate during mixed-acid fermentation (PubMed:23335413, PubMed:24659605, PubMed:30247527, PubMed:33169422, PubMed:35084298, PubMed:35377837, PubMed:35390794, PubMed:8022272). Functions to maintain relatively constant intracellular formate levels during growth, using different mechanisms for efflux and uptake of the anion (PubMed:35377837). Has a strong preference for formate as a substrate in vivo and not other acidic fermentation products (PubMed:23335413). {ECO:0000269|PubMed:23335413, ECO:0000269|PubMed:24659605, ECO:0000269|PubMed:30247527, ECO:0000269|PubMed:33169422, ECO:0000269|PubMed:35084298, ECO:0000269|PubMed:35377837, ECO:0000269|PubMed:35390794, ECO:0000269|PubMed:8022272}. EcoCyc product frame: FOCA-MONOMER. EcoCyc synonyms: ycaE. Genomic coordinates: 953609-954466.

## Biological Role

Repressed by arcA (protein.P0A9Q1), narL (protein.P0AF28). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), fnr (protein.P0A9E5), arcA (protein.P0A9Q1), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC23|protein.P0AC23]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=focA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=focA; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=focA; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=focA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=focA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=focA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003073,ECOCYC:EG11258,GeneID:945513`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:953609-954466:-; feature_type=gene
