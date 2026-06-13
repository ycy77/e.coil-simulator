---
entity_id: "gene.b4073"
entity_type: "gene"
name: "nrfD"
source_database: "NCBI RefSeq"
source_id: "gene-b4073"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4073"
  - "nrfD"
---

# nrfD

`gene.b4073`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4073`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfD (gene.b4073) is a gene entity. It encodes nrfD (protein.P32709). Encoded protein function: FUNCTION: Probably involved in the transfer of electrons from the quinone pool to the type-c cytochromes. EcoCyc product frame: NRFD-MONOMER. EcoCyc synonyms: yjcK. Genomic coordinates: 4290476-4291432. EcoCyc protein note: NrfD is a predicted inner membrane protein containing 8 conserved hydrophobic segments. It may be the naphthoquinol oxidase although a role as a proton pump has not been excluded .

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28), nsrR (protein.P0AF63). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32709|protein.P32709]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfD; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfD; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfD; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfD; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfD; function=-+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=nrfD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013348,ECOCYC:EG11947,GeneID:948580`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4290476-4291432:+; feature_type=gene
