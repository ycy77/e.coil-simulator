---
entity_id: "gene.b3118"
entity_type: "gene"
name: "tdcA"
source_database: "NCBI RefSeq"
source_id: "gene-b3118"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3118"
  - "tdcA"
---

# tdcA

`gene.b3118`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3118`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcA (gene.b3118) is a gene entity. It encodes tdcA (protein.P0ACQ7). Encoded protein function: FUNCTION: Transcriptional activator for the tdcABCDE operon. {ECO:0000269|PubMed:8413189}. EcoCyc product frame: PD00268. Genomic coordinates: 3266127-3267065. EcoCyc protein note: During anaerobiosis, TdcA participates in controlling genes (tdc operon) involved in transport and metabolism of threonine and serine . Inhibition of tdcA expression by CRISPRi reduced cellular fitness under treatment with the antibiotics carbonyl cyanide 3-chlorophenylhydrazone (CCCP) or pyocyanin . TdcA belongs to the LysR family of transcriptional regulators, and like the other members of this family, it has a helix-turn-helix motif in the N-terminal domain for DNA binding . Although interaction between TdcA and the regulatory region of the tdc operon has not been demonstrated, it has been suggested that TdcA recognizes and binds to an inverted repeat located upstream of the operon . tdcA is the first gene in the tdcABCDEFG operon, which is autoactivated by TdcA. This operon is divergently transcribed with the tdcR gene, whose product also activates the transcription of the operon . TdcA probably interacts with TdcR to activate transcription , and they appear to function together with CRP and IHF, proteins that bend the DNA, for this activation...

## Biological Role

Repressed by nac (protein.Q47005). Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACQ7|protein.P0ACQ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcA; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcA; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tdcA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010252,ECOCYC:EG10989,GeneID:947494`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3266127-3267065:-; feature_type=gene
