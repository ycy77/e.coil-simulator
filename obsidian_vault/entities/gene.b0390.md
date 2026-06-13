---
entity_id: "gene.b0390"
entity_type: "gene"
name: "aroM"
source_database: "NCBI RefSeq"
source_id: "gene-b0390"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0390"
  - "aroM"
---

# aroM

`gene.b0390`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0390`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroM (gene.b0390) is a gene entity. It encodes aroM (protein.P0AE28). Encoded protein function: FUNCTION: This protein of unknown function is encoded by a gene that cotranscribes with the aroL gene, which codes for shikimate kinase II. EcoCyc product frame: EG10083-MONOMER. Genomic coordinates: 407428-408105. EcoCyc protein note: AroM is encoded in an operon together with AroL, shikimate kinase II . AroM is not required for growth on minimal medium, and its function is unknown . In a random transposon mutagenesis screen, aroM was indentified as a gene whose inactivation is beneficial for anaerobic hydrogen production from glycerol in early log phase. A ΔaroM mutant strain grows slightly faster than the parent strain under anaerobic conditions .

## Biological Role

Repressed by tyrR (protein.P07604), trpR (protein.P0A881). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE28|protein.P0AE28]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroM; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=aroM; function=-
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=aroM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001357,ECOCYC:EG10083,GeneID:945045`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:407428-408105:+; feature_type=gene
