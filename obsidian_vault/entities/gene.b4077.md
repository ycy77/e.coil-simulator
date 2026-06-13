---
entity_id: "gene.b4077"
entity_type: "gene"
name: "gltP"
source_database: "NCBI RefSeq"
source_id: "gene-b4077"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4077"
  - "gltP"
---

# gltP

`gene.b4077`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4077`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltP (gene.b4077) is a gene entity. It encodes gltP (protein.P21345). Encoded protein function: FUNCTION: Catalyzes the proton-dependent, binding-protein-independent transport of glutamate and aspartate (PubMed:1971622, PubMed:2537813, PubMed:28025687, PubMed:336628, PubMed:8596452). At least two protons are transported in symport with the substrate (PubMed:8596452). Binds glutamate and aspartate, and it has an approximately four-fold higher affinity for binding L-aspartate than L-glutamate in native membranes (PubMed:28025687). {ECO:0000269|PubMed:1971622, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:28025687, ECO:0000269|PubMed:336628, ECO:0000269|PubMed:8596452}. EcoCyc product frame: GLTP-MONOMER. Genomic coordinates: 4294481-4295794. EcoCyc protein note: E. coli contains four transporters for the uptake of glutamate (GltIJKL, GltP, GltS, and GadC) and five transporters for the uptake of aspartate (GltIJKL, GltP, DctA, DcuA, and DcuB). GltP accounts for approximately 60% of the total wild-type transport velocity of glutamate, and 52% of the total wild-type transport velocity of aspartate in aerobic growth with succinate and 40 mM NaCl . GltP is a proton dependent transporter for glutamate and aspartate. E...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21345|protein.P21345]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=gltP; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gltP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013357,ECOCYC:EG10405,GeneID:948591`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4294481-4295794:+; feature_type=gene
