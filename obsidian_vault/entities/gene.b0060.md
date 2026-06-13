---
entity_id: "gene.b0060"
entity_type: "gene"
name: "polB"
source_database: "NCBI RefSeq"
source_id: "gene-b0060"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0060"
  - "polB"
---

# polB

`gene.b0060`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0060`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

polB (gene.b0060) is a gene entity. It encodes polB (protein.P21189). Encoded protein function: FUNCTION: Thought to be involved in DNA repair and/or mutagenesis. Its processivity is enhanced by the beta sliding clamp (dnaN) and clamp loader (PubMed:1534562, PubMed:1999435). {ECO:0000269|PubMed:1534562, ECO:0000269|PubMed:1999435}. EcoCyc product frame: EG10747-MONOMER. EcoCyc synonyms: dinA. Genomic coordinates: 63429-65780. EcoCyc protein note: DNA polymerase II (Pol II) is a combined polymerase and exonuclease involved in replication restart following UV exposure, translesion synthesis and nucleotide excision repair. Pol II catalyzes both a DNA polymerase activity and a 3' to 5' exonuclease activity . Pol II is also required for rapid restart of DNA replication following UV irradiation . In addition to its role in translesion bypass, discussed below, Pol II is required for a nucleotide excision repair pathway that fixes DNA crosslinks . Pol II also plays a role in surviving thymine dimers and avoiding the mutagenic effects of agents such as peroxide . Pol II tends to make more errors in replication of AT-rich sequences, which differs from the behavior of most other DNA polymerases . Pol II allows replication to bypass some kinds of DNA lesions. Under certain conditions Pol II is required for bypass of abasic lesions...

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21189|protein.P21189]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=polB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000202,ECOCYC:EG10747,GeneID:944779`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:63429-65780:-; feature_type=gene
