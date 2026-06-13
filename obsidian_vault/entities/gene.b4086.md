---
entity_id: "gene.b4086"
entity_type: "gene"
name: "alsC"
source_database: "NCBI RefSeq"
source_id: "gene-b4086"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4086"
  - "alsC"
---

# alsC

`gene.b4086`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4086`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alsC (gene.b4086) is a gene entity. It encodes alsC (protein.P32720). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system AlsBAC for D-allose; probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:9401019}. EcoCyc product frame: YJCV-MONOMER. EcoCyc synonyms: yjcV. Genomic coordinates: 4308489-4309469. EcoCyc protein note: alsC encodes the predicted integral membrane subunit of a D-allose ABC transporter . The alsC gene appears to be defective in E. coli K-12 strain W3110 which does not use D-allose as a carbon source

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32720|protein.P32720]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alsC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013392,ECOCYC:EG11958,GeneID:948594`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4308489-4309469:-; feature_type=gene
