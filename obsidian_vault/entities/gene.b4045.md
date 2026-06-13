---
entity_id: "gene.b4045"
entity_type: "gene"
name: "yjbJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4045"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4045"
  - "yjbJ"
---

# yjbJ

`gene.b4045`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4045`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbJ (gene.b4045) is a gene entity. It encodes yjbJ (protein.P68206). Encoded protein function: UPF0337 protein YjbJ EcoCyc product frame: EG11928-MONOMER. Genomic coordinates: 4259237-4259446. EcoCyc protein note: YjbJ is a soluble protein with a four-helix bundle domain . YjbJ is one of a number of proteins that interacts with the PROP-MONOMER; however, it does not affect ProP localization or function . YjbJ is not required for growth on rich or minimal media. The effects of mutations on the rate of cell growth are observed to vary depending on the construction of the mutant allele . Structural characterization has been performed by NMR . YjbJ is found at high abundance in vivo . Expression is induced under osmotic stress imposed by NaCl in both aerobic and anaerobic conditions , and by acidic pH in the presence of cadmium . yjbJ belongs to the σS regulon .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), lrp (protein.P0ACJ0), fliZ (protein.P52627).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68206|protein.P68206]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yjbJ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=yjbJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013247,ECOCYC:EG11928,GeneID:948553`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4259237-4259446:+; feature_type=gene
