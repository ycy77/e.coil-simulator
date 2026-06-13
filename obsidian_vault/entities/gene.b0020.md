---
entity_id: "gene.b0020"
entity_type: "gene"
name: "nhaR"
source_database: "NCBI RefSeq"
source_id: "gene-b0020"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0020"
  - "nhaR"
---

# nhaR

`gene.b0020`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0020`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nhaR (gene.b0020) is a gene entity. It encodes nhaR (protein.P0A9G2). Encoded protein function: FUNCTION: Plays a role in the positive regulation of NhaA. {ECO:0000269|PubMed:1316901}. EcoCyc product frame: PD00474. EcoCyc synonyms: antO, yaaB. Genomic coordinates: 18715-19620.

## Biological Role

Repressed by carbon storage regulator CsrA (complex.ecocyc.CPLX0-7956), csrA (protein.P69913). Activated by rpoD (protein.P00579), nhaR (protein.P0A9G2), ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9G2|protein.P0A9G2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nhaR; function=+
- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=nhaR; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=nhaR; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7956|complex.ecocyc.CPLX0-7956]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=nhaR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000072,ECOCYC:EG11078,GeneID:944757`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:18715-19620:+; feature_type=gene
