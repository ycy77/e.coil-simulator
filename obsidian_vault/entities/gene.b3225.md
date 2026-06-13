---
entity_id: "gene.b3225"
entity_type: "gene"
name: "nanA"
source_database: "NCBI RefSeq"
source_id: "gene-b3225"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3225"
  - "nanA"
---

# nanA

`gene.b3225`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3225`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanA (gene.b3225) is a gene entity. It encodes nanA (protein.P0A6L4). Encoded protein function: FUNCTION: Catalyzes the reversible aldol cleavage of N-acetylneuraminic acid (sialic acid; Neu5Ac) to form pyruvate and N-acetylmannosamine (ManNAc) via a Schiff base intermediate (PubMed:12711733, PubMed:1646603, PubMed:24521460, PubMed:33895133). Experiments show the true substrate is aceneuramate (linearized Neu5Ac), which forms spontaneously at alkaline pH (PubMed:33895133). Linear aceneuramate can be provided by NanQ (PubMed:33895133). Can also cleave other substrates such as N-glycollylneuraminic acid (GcNeu), but not colominic acid or 2-oxocarboxylic acids such as 2-oxohexanoic acid, 2-oxo-octanoic acid, 2-oxo-3-deoxyoctanoic acid and 2-oxononanoic acid (PubMed:1646603). {ECO:0000269|PubMed:12711733, ECO:0000269|PubMed:1646603, ECO:0000269|PubMed:24521460, ECO:0000269|PubMed:33895133}. EcoCyc product frame: ACNEULY-MONOMER. Genomic coordinates: 3372683-3373576. EcoCyc protein note: N-acetylneuraminate lyase (NanA) is part of the PWY0-1324 pathway, where it catalyzes the formation of N-acetylmannosamine and pyruvate from the linear (aldehydo) form of N-acetylneuraminate (NeuNAc) . The enzyme is classified as a Schiff base-forming Class I aldolase . NeuNAc, the substrate of NanA, exists predominantly in the β-anomeric (cyclic) form in solution...

## Biological Role

Repressed by fis (protein.P0A6R3), nanR (protein.P0A8W0), nac (protein.Q47005). Activated by crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6L4|protein.P0A6L4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nanA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nanA; function=-
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nanA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010579,ECOCYC:EG10637,GeneID:947742`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3372683-3373576:-; feature_type=gene
