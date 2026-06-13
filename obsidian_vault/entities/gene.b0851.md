---
entity_id: "gene.b0851"
entity_type: "gene"
name: "nfsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0851"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0851"
  - "nfsA"
---

# nfsA

`gene.b0851`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0851`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfsA (gene.b0851) is a gene entity. It encodes nfsA (protein.P17117). Encoded protein function: FUNCTION: Catalyzes the reduction of nitroaromatic compounds using NADPH. Has a broad electron acceptor specificity. Reduces nitrofurazone by a ping-pong bi-bi mechanism possibly to generate a two-electron transfer product. Major oxygen-insensitive nitroreductase in E.coli. {ECO:0000269|PubMed:8755878}. EcoCyc product frame: EG11261-MONOMER. EcoCyc synonyms: mda18, mdaA, ybjB. Genomic coordinates: 891184-891906. EcoCyc protein note: The nfsA-encoded nitroreductase is the major oxygen-insensitive nitroreductase present in E. coli. NfsA uses only NADPH and has broad electron acceptor specificity . The physiologically relevant substrates may be quinones . Nitroreductases can be used as prodrug activators in cancer therapy . NfsA catalyzes the reduction of nitrocompounds using a ping-pong Bi-Bi mechanism, transferring two electrons . The mechanism for two-electron reduction of quinones is most consistent with a single-step hydride transfer . Turnover of the enzyme is limited by the oxidative half-reaction . The reduction of nitrocompounds to hydroxylamines occurs via a nitroso intermediate; ascorbate inhibition patterns suggest that the reduction of the nitroso intermediate occurs directly by NADPH rather than enzymatically...

## Biological Role

Repressed by sdsN (gene.b4719), oxyR (protein.P0ACQ4). Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17117|protein.P17117]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nfsA; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=nfsA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=nfsA; function=+
- `represses` <-- [[gene.b4719|gene.b4719]] `RegulonDB` `S` - regulator=SdsN; target=nfsA; function=-
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=nfsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002900,ECOCYC:EG11261,GeneID:945483`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:891184-891906:+; feature_type=gene
