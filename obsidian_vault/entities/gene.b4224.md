---
entity_id: "gene.b4224"
entity_type: "gene"
name: "chpS"
source_database: "NCBI RefSeq"
source_id: "gene-b4224"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4224"
  - "chpS"
---

# chpS

`gene.b4224`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4224`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chpS (gene.b4224) is a gene entity. It encodes chpS (protein.P08365). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. May be involved in the regulation of cell growth. It acts as a suppressor of the endoribonuclease (inhibitory function) of ChpB protein. Both ChpS and ChpB probably bind to the promoter region of the chpS-chpB operon to autoregulate their synthesis. {ECO:0000269|PubMed:16413033, ECO:0000269|PubMed:8226627}. EcoCyc product frame: EG11250-MONOMER. EcoCyc synonyms: chpBI, yjfB. Genomic coordinates: 4448447-4448698. EcoCyc protein note: ChpS is the antitoxin component of the ChpB-ChpS toxin-antitoxin system. See the the ChpB-ChpS complex entry for an explanAtion of ChpS's role in regulating this system.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08365|protein.P08365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=chpS; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=chpS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013820,ECOCYC:EG11250,GeneID:948739`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4448447-4448698:+; feature_type=gene
