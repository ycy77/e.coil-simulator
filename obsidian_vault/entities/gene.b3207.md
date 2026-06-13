---
entity_id: "gene.b3207"
entity_type: "gene"
name: "yrbL"
source_database: "NCBI RefSeq"
source_id: "gene-b3207"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3207"
  - "yrbL"
---

# yrbL

`gene.b3207`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3207`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yrbL (gene.b3207) is a gene entity. It encodes yrbL (protein.P64610). Encoded protein function: Uncharacterized protein YrbL EcoCyc product frame: G7667-MONOMER. Genomic coordinates: 3348452-3349084. EcoCyc protein note: Transcription of yrbL is regulated by Mg2+ via the PhoP/PhoQ system . A mutant with a constitutively active EvgA/EvgS two-component system shows enhanced expression of yrbL . APORNAP-CPLX pausing during elongation at consensus sequence elements has been studied using yrbL .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), basR (protein.P30843). Activated by soxS (protein.P0A9E2), soxR (protein.P0ACS2), phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64610|protein.P64610]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=yrbL; function=+
- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `S` - regulator=SoxR; target=yrbL; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=yrbL; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yrbL; function=-
- `represses` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=yrbL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010528,ECOCYC:G7667,GeneID:947910`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3348452-3349084:+; feature_type=gene
