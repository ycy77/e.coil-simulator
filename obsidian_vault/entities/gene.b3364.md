---
entity_id: "gene.b3364"
entity_type: "gene"
name: "tsgA"
source_database: "NCBI RefSeq"
source_id: "gene-b3364"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3364"
  - "tsgA"
---

# tsgA

`gene.b3364`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3364`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsgA (gene.b3364) is a gene entity. It encodes tsgA (protein.P60778). Encoded protein function: Protein TsgA EcoCyc product frame: YHFC-MONOMER. EcoCyc synonyms: yhfH, gutS, yhfC. Genomic coordinates: 3492568-3493749. EcoCyc protein note: TsgA has been implicated in the response of E. coli K-12 to the toxic elements tellurite and selenite. Transcription of tsgA is upregulated when cells are grown in the presence of sodium selenite or sodium tellurite . Expression of tsgA in wild-type E. coli K-12 had no effect on the sensitivity or resistance of the cells to selenite or tellurite . TsgA is a member of the Fucose:H+ symporter family within the Major Facilitator Superfamily (MFS) of transporters . Membrane topology predictions using experimentally determined C terminus locations indicate that TsgA has 12 transmembrane helices and the C-terminus is located in the cytoplasm . TsgA: tellurite, selenite responsive gene A

## Biological Role

Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60778|protein.P60778]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=tsgA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010997,ECOCYC:EG11262,GeneID:947869`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3492568-3493749:+; feature_type=gene
