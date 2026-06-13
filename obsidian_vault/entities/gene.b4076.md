---
entity_id: "gene.b4076"
entity_type: "gene"
name: "nrfG"
source_database: "NCBI RefSeq"
source_id: "gene-b4076"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4076"
  - "nrfG"
---

# nrfG

`gene.b4076`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4076`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfG (gene.b4076) is a gene entity. It encodes nrfG (protein.P32712). Encoded protein function: FUNCTION: Required for formate-dependent nitrite reduction. Not required for the biosynthesis of any of the c-type cytochromes nor for the secretion of the periplasmic cytochromes. {ECO:0000305|PubMed:9593308}. EcoCyc product frame: EG11950-MONOMER. EcoCyc synonyms: yjcN, aidC. Genomic coordinates: 4293543-4294139. EcoCyc protein note: NrfG is essential for NrfA activity. It, along with NrfE amd NrfF, is presumed to be part of a heme lyase that adds heme groups to apocytochrome c552 . NrfG is predicted to be a bitopic inner membrane protein

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32712|protein.P32712]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfG; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfG; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfG; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nrfG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfG; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfG; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0013354,ECOCYC:EG11950,GeneID:948592`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4293543-4294139:+; feature_type=gene
