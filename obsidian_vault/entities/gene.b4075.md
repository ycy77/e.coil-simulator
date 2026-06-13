---
entity_id: "gene.b4075"
entity_type: "gene"
name: "nrfF"
source_database: "NCBI RefSeq"
source_id: "gene-b4075"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4075"
  - "nrfF"
---

# nrfF

`gene.b4075`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4075`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfF (gene.b4075) is a gene entity. It encodes nrfF (protein.P32711). Encoded protein function: FUNCTION: Not required for the biosynthesis of any of the c-type cytochromes. Possible subunit of a heme lyase. {ECO:0000305|PubMed:9593308}. EcoCyc product frame: EG11949-MONOMER. EcoCyc synonyms: yjcM. Genomic coordinates: 4293163-4293546. EcoCyc protein note: NrfF is a periplasmic protein that is essential for NrfA activity. NrfA, NrfE and NrfG are presumed to be part of a heme lyase that adds heme groups to apocytochrome c552 . NrfF is predicted to be a bitopic inner membrane protein

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28), nsrR (protein.P0AF63). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32711|protein.P32711]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfF; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfF; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfF; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nrfF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfF; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfF; function=-+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=nrfF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013352,ECOCYC:EG11949,GeneID:948578`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4293163-4293546:+; feature_type=gene
