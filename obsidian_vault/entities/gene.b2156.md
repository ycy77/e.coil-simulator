---
entity_id: "gene.b2156"
entity_type: "gene"
name: "lysP"
source_database: "NCBI RefSeq"
source_id: "gene-b2156"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2156"
  - "lysP"
---

# lysP

`gene.b2156`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2156`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysP (gene.b2156) is a gene entity. It encodes lysP (protein.P25737). Encoded protein function: FUNCTION: Permease involved in lysine uptake (PubMed:1315732, PubMed:24056175). In addition, functions as a lysine sensor that mediates the lysine-dependent regulation of the transcriptional activator CadC (PubMed:18086202, PubMed:24056175). In the absence of lysine, or at low lysine concentrations, LysP inhibits CadC by an interaction with the transmembrane domain of CadC. In the presence of lysine, LysP loses its ability to interact with and inhibit CadC, and acts as a lysine permease (PubMed:18086202, PubMed:24056175). {ECO:0000269|PubMed:1315732, ECO:0000269|PubMed:18086202, ECO:0000269|PubMed:24056175}. EcoCyc product frame: LYSP-MONOMER. EcoCyc synonyms: cadR. Genomic coordinates: 2247063-2248532. EcoCyc protein note: LysP is a lysine-specific transporter which mediates the uptake of lysine for biosynthetic purposes and functions as a co-sensor for lysine in the lysine dependent acid-resistance (LDAR) system*. lysP encodes a lysine-specific transporter which contributes to lysine uptake when cells are grown aerobically at neutral pH; LysP mediated lysine uptake increases under anaerobic conditions in media of low pH with added lysine...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by argP (protein.P0A8S1), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25737|protein.P25737]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `C` - regulator=ArgP; target=lysP; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=lysP; function=-+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=lysP; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=lysP; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lysP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007131,ECOCYC:EG11337,GeneID:946667`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2247063-2248532:-; feature_type=gene
