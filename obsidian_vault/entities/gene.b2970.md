---
entity_id: "gene.b2970"
entity_type: "gene"
name: "yghF"
source_database: "NCBI RefSeq"
source_id: "gene-b2970"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2970"
  - "yghF"
---

# yghF

`gene.b2970`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2970`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghF (gene.b2970) is a gene entity. It encodes yghF (protein.Q46834). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. {ECO:0000305}. EcoCyc product frame: G7537-MONOMER. EcoCyc synonyms: ecfA. Genomic coordinates: 3112054-3113049. EcoCyc protein note: YghF has homology to the GspC Type II secretion system protein from enterotoxigenic E. coli strain H10407 . In pathogenic (and some commensal) E. coli strains, GspC functions as part of a virulence associated type II secretion pathway - known as T2SSβ or T2SSH10407; examination of T2SSΒ encoding loci in various strains indicates that E. coli K-12 carries remnants of the pathway but has experienced a deletion which removed a large internal region of the T2SSβ encoding operon . yghF has a σE dependent promoter ; YghF was not identified as a member of the σE regulon in a later study . Ecf: "extracytoplasmic function"

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46834|protein.Q46834]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yghF; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yghF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009745,ECOCYC:G7537,GeneID:947469`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3112054-3113049:-; feature_type=gene
