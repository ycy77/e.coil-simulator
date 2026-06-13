---
entity_id: "gene.b4074"
entity_type: "gene"
name: "nrfE"
source_database: "NCBI RefSeq"
source_id: "gene-b4074"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4074"
  - "nrfE"
---

# nrfE

`gene.b4074`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4074`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfE (gene.b4074) is a gene entity. It encodes nrfE (protein.P32710). Encoded protein function: FUNCTION: May be required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase. {ECO:0000305|PubMed:15919996}. EcoCyc product frame: EG11948-MONOMER. EcoCyc synonyms: yjcL. Genomic coordinates: 4291512-4293170. EcoCyc protein note: NrfE is a membrane-spanning protein that is essential for NrfA activity. NrfE, NrfF and NrfG are presumed to part of a heme lyase that adds heme groups to apocytrochrome c552 (NrfA) .

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28), nsrR (protein.P0AF63). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32710|protein.P32710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfE; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfE; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfE; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfE; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfE; function=-+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=nrfE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013350,ECOCYC:EG11948,GeneID:948579`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4291512-4293170:+; feature_type=gene
