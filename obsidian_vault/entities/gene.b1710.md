---
entity_id: "gene.b1710"
entity_type: "gene"
name: "btuE"
source_database: "NCBI RefSeq"
source_id: "gene-b1710"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1710"
  - "btuE"
---

# btuE

`gene.b1710`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1710`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btuE (gene.b1710) is a gene entity. It encodes btuE (protein.P06610). Encoded protein function: FUNCTION: Non-specific peroxidase that can use thioredoxin or glutathione as a reducing agent. In vitro, utilizes preferentially thioredoxin A to decompose hydrogen peroxide as well as cumene-, tert-butyl-, and linoleic acid hydroperoxides, suggesting that it may have one or more organic hydroperoxide as its physiological substrate. {ECO:0000269|PubMed:20621065}. EcoCyc product frame: BTUE-MONOMER. Genomic coordinates: 1793558-1794109. EcoCyc protein note: BtuE is a relatively non-specific peroxidase that is able to utilize both thioredoxins as well as glutathione. Using thioredoxin as a reducing agent, the enzyme is able to decompose a variety of organic hydroperoxides . BtuE is encoded as part of the btuCED operon, which also encodes proteins that are part of a vitamin B12 transport system . Transposon insertions in the btuC and btuD regions conferred a deficiency in vitamin B12 utilization and transport . However, there are indications that BtuE (residing within the operon) is not required for transport. Transposon insertions in btuE were not complemented by plasmids carrying btuE alone, whereas insertions in btuC and btuD were effectively complemented by plasmids carrying the corresponding functional gene...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06610|protein.P06610]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=btuE; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005709,ECOCYC:EG10129,GeneID:945915`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1793558-1794109:-; feature_type=gene
