---
entity_id: "gene.b0812"
entity_type: "gene"
name: "dps"
source_database: "NCBI RefSeq"
source_id: "gene-b0812"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0812"
  - "dps"
---

# dps

`gene.b0812`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0812`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dps (gene.b0812) is a gene entity. It encodes dps (protein.P0ABT2). Encoded protein function: FUNCTION: During stationary phase, binds the chromosome non-specifically, forming a highly ordered and stable dps-DNA co-crystal within which chromosomal DNA is condensed and protected from diverse damages. It protects DNA from oxidative damage by sequestering intracellular Fe(2+) ion and storing it in the form of Fe(3+) oxyhydroxide mineral, which can be released after reduction. One hydrogen peroxide oxidizes two Fe(2+) ions, which prevents hydroxyl radical production by the Fenton reaction. Dps also protects the cell from UV and gamma irradiation, iron and copper toxicity, thermal stress and acid and base shocks. Also shows a weak catalase activity. {ECO:0000269|PubMed:10403254, ECO:0000269|PubMed:1340475, ECO:0000269|PubMed:15205421, ECO:0000269|PubMed:15534364}. EcoCyc product frame: EG11415-MONOMER. EcoCyc synonyms: pexB, vtm. Genomic coordinates: 848408-848911.

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), fis (protein.P0A6R3), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABT2|protein.P0ABT2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dps; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=dps; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=dps; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=dps; function=-
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=dps; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=dps; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002776,ECOCYC:EG11415,GeneID:945101`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:848408-848911:-; feature_type=gene
