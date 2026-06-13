---
entity_id: "gene.b4072"
entity_type: "gene"
name: "nrfC"
source_database: "NCBI RefSeq"
source_id: "gene-b4072"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4072"
  - "nrfC"
---

# nrfC

`gene.b4072`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4072`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfC (gene.b4072) is a gene entity. It encodes nrfC (protein.P0AAK7). Encoded protein function: FUNCTION: Probably involved in the transfer of electrons from the quinone pool to the type-c cytochromes. EcoCyc product frame: NRFC-MONOMER. EcoCyc synonyms: yjcJ. Genomic coordinates: 4289808-4290479. EcoCyc protein note: NrfC is predicted to be membrane bound. It contains 16 conserved cysteine residues and thus is likely to be an Fe-S protein. NrfC contains a double arginine signal sequence .

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28), nsrR (protein.P0AF63). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAK7|protein.P0AAK7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfC; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfC; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfC; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfC; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfC; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfC; function=-+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=nrfC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013346,ECOCYC:EG11946,GeneID:948581`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4289808-4290479:+; feature_type=gene
