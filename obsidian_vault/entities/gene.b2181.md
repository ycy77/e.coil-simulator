---
entity_id: "gene.b2181"
entity_type: "gene"
name: "yejG"
source_database: "NCBI RefSeq"
source_id: "gene-b2181"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2181"
  - "yejG"
---

# yejG

`gene.b2181`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2181`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yejG (gene.b2181) is a gene entity. It encodes yejG (protein.P0AD21). Encoded protein function: Uncharacterized protein YejG EcoCyc product frame: EG12042-MONOMER. Genomic coordinates: 2277893-2278237. EcoCyc protein note: Overexpression of YejG leads to slightly increased resistance to the aminoglycoside antibiotics apramycin, sisomicin and tobramycin . A solution structure of YejG shows that the protein has a stucture similar to the RNA recognition motif domain III of EG10360-MONOMER. However, YejG does not appear to co-purify with the ribosome or bind to nucleic acids . Expression of yejG is slightly upregulated in response to treatment with citral, and a ΔyejG mutant is inhibited more strongly by citral .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD21|protein.P0AD21]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yejG; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yejG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yejG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007214,ECOCYC:EG12042,GeneID:945319`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2277893-2278237:-; feature_type=gene
