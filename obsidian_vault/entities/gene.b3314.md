---
entity_id: "gene.b3314"
entity_type: "gene"
name: "rpsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3314"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3314"
  - "rpsC"
---

# rpsC

`gene.b3314`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3314`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsC (gene.b3314) is a gene entity. It encodes rpsC (protein.P0A7V3). Encoded protein function: FUNCTION: Binds the lower part of the 30S subunit head. Binds mRNA in the 70S ribosome, positioning it for translation (By similarity). {ECO:0000250}.; FUNCTION: Plays a role in mRNA unwinding by the ribosome, possibly by forming part of a processivity clamp. {ECO:0000269|PubMed:15652481}. EcoCyc product frame: EG10902-MONOMER. Genomic coordinates: 3449182-3449883. EcoCyc protein note: The S3 protein, a component of the small subunit of the ribosome, is surface-accessible and located on the head of the 30S subunit . It can be crosslinked to rRNA and nascent peptides as well as to IF3 . S3 is the main target of modification by reaction with pyridoxal phosphate . The ribosome was found to have mRNA helicase activity, and mutations in the S3 and S4 subunits impair this activity . A low-resolution cryo-electron microscopy map of the ribosome containing S3 has been analyzed .

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7V3|protein.P0A7V3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsC; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rpsC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010848,ECOCYC:EG10902,GeneID:947814`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3449182-3449883:-; feature_type=gene
