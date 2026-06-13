---
entity_id: "gene.b3162"
entity_type: "gene"
name: "deaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3162"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3162"
  - "deaD"
---

# deaD

`gene.b3162`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3162`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

deaD (gene.b3162) is a gene entity. It encodes deaD (protein.P0A9P6). Encoded protein function: FUNCTION: DEAD-box RNA helicase involved in various cellular processes at low temperature, including ribosome biogenesis, mRNA degradation and translation initiation. Exhibits RNA-stimulated ATP hydrolysis and RNA unwinding activity at low temperature. Involved in 50S ribosomal subunit assembly, acting after SrmB, and could also play a role in the biogenesis of the 30S ribosomal subunit. In addition, is involved in mRNA decay, via formation of a cold-shock degradosome with RNase E. Also stimulates translation of some mRNAs, probably at the level of initiation. {ECO:0000255|HAMAP-Rule:MF_00964, ECO:0000269|PubMed:10216955, ECO:0000269|PubMed:15148362, ECO:0000269|PubMed:15196029, ECO:0000269|PubMed:15554978, ECO:0000269|PubMed:17259309, ECO:0000269|PubMed:8552679}. EcoCyc product frame: EG10215-MONOMER. EcoCyc synonyms: csdA, mssB, rhlD. Genomic coordinates: 3305971-3307860.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9P6|protein.P0A9P6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=deaD; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010392,ECOCYC:EG10215,GeneID:947674`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3305971-3307860:-; feature_type=gene
