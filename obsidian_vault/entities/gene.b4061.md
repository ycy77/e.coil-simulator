---
entity_id: "gene.b4061"
entity_type: "gene"
name: "pdeC"
source_database: "NCBI RefSeq"
source_id: "gene-b4061"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4061"
  - "pdeC"
---

# pdeC

`gene.b4061`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4061`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeC (gene.b4061) is a gene entity. It encodes pdeC (protein.P32701). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (By similarity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Overexpression reduces biofilm formation (PubMed:19460094). {ECO:0000250|UniProtKB:P21514, ECO:0000269|PubMed:19460094}. EcoCyc product frame: EG11938-MONOMER. EcoCyc synonyms: yjcC. Genomic coordinates: 4275471-4277057. EcoCyc protein note: PdeC is a c-di-GMP-specific phosphodiesterase whose activity is implicated in modulating matrix formation in the deeper layers of E. coli biofilm. Overexpression of pdeC reduces biofilm formation . PdeC is an inner membrane protein with two predicted transmembrane domains which flank a predicted periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with phosphodiesterase activity . Purified PdeC reconstituted into nanodiscs exhibits c-di-GMP phosphodiesterase activity only in the presence of reducing agent (DTT) . The periplasmic CSS domain contains two cysteine residues which form a disulphide bond; the redox state of the periplasmic CSS domain controls phosphodiesterase activity; PdeC is highly active when the CSS domain is in the free thiol state...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32701|protein.P32701]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pdeC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013309,ECOCYC:EG11938,GeneID:948568`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4275471-4277057:+; feature_type=gene
