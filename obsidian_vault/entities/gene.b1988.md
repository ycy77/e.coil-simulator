---
entity_id: "gene.b1988"
entity_type: "gene"
name: "nac"
source_database: "NCBI RefSeq"
source_id: "gene-b1988"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1988"
  - "nac"
---

# nac

`gene.b1988`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1988`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nac (gene.b1988) is a gene entity. It encodes nac (protein.Q47005). Encoded protein function: FUNCTION: Transcriptional activator for the hut, put and ure operons and repressor for the gdh and gltB operons in response to nitrogen limitation. Negative regulator of its own expression (By similarity). {ECO:0000250}. EcoCyc product frame: G7072-MONOMER. Genomic coordinates: 2061016-2061933. EcoCyc protein note: Nac, "Nitrogen assimilation control," regulates, without a coeffector, genes involved in nitrogen metabolism under nitrogen-limiting conditions . The genes regulated by Nac are transcribed by RNA polymerase σ70. By using synthetic gene circuits, it was suggested that Nac shows stabilization of RNA polymerase (RNAP) at a downstream repressing position, while activation at upstream positions occurs without stabilization . The genes regulated by Nac are coupled to the nitrogen regulatory (Ntr) system, which is σ54 dependent, through Nac, whose transcription is activated by NtrC . Using DNA microarray analyses, it was shown that Nac could affect the expression of 25 genes . This transcriptional regulator is negatively autoregulated and is expressed under nitrogen-limiting conditions . Inhibition of nac expression by CRISPRi reduced cellular fitness under treatment with the antibiotic pyocyanin...

## Biological Role

Repressed by nac (protein.Q47005). Activated by NtrC phosphorylated dimer (complex.ecocyc.CPLX0-8566), lrp (protein.P0ACJ0), glnG (protein.P0AFB8), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47005|protein.Q47005]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=nac; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=nac; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `C` - regulator=Nac; target=nac; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006594,ECOCYC:G7072,GeneID:946501`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2061016-2061933:-; feature_type=gene
