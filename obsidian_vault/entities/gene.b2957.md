---
entity_id: "gene.b2957"
entity_type: "gene"
name: "ansB"
source_database: "NCBI RefSeq"
source_id: "gene-b2957"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2957"
  - "ansB"
---

# ansB

`gene.b2957`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2957`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ansB (gene.b2957) is a gene entity. It encodes ansB (protein.P00805). Encoded protein function: L-asparaginase 2 (EC 3.5.1.1) (L-asparaginase II) (L-ASNase II) (L-asparagine amidohydrolase II) (Colaspase) EcoCyc product frame: ANSB-MONOMER. Genomic coordinates: 3099682-3100728.

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fnr (protein.P0A9E5), lrp (protein.P0ACJ0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00805|protein.P00805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ansB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ansB; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ansB; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ansB; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ansB; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ansB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009700,ECOCYC:EG10046,GeneID:947454`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3099682-3100728:-; feature_type=gene
