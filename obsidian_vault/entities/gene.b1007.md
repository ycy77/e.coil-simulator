---
entity_id: "gene.b1007"
entity_type: "gene"
name: "rutF"
source_database: "NCBI RefSeq"
source_id: "gene-b1007"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1007"
  - "rutF"
---

# rutF

`gene.b1007`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1007`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutF (gene.b1007) is a gene entity. It encodes rutF (protein.P75893). Encoded protein function: FUNCTION: Catalyzes the reduction of FMN to FMNH2 which is used to reduce pyrimidine by RutA via the Rut pathway. In vitro, the flavin reductase Fre can substitute for the function of RutF, however, RutF is required for uracil utilization in vivo. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551}. EcoCyc product frame: G6518-MONOMER. EcoCyc synonyms: ycdH. Genomic coordinates: 1069860-1070354. EcoCyc protein note: E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutF functions as a flavin reductase whose activity is required for the first catalytic step, the flavin hydroperoxide-catalyzed ring opening by the RutA pyrimidine oxygenase . In vitro, the flavin reductase Fre can substitute for the function of RutF; however, RutF is required for uracil utilization in vivo . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutF insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutF: "pyrimidine utilization F" Reviews:

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75893|protein.P75893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutF; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutF; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003403,ECOCYC:G6518,GeneID:946594`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1069860-1070354:-; feature_type=gene
