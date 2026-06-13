---
entity_id: "gene.b0345"
entity_type: "gene"
name: "lacI"
source_database: "NCBI RefSeq"
source_id: "gene-b0345"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0345"
  - "lacI"
---

# lacI

`gene.b0345`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0345`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lacI (gene.b0345) is a gene entity. It encodes lacI (protein.P03023). Encoded protein function: FUNCTION: Repressor of the lactose operon. Binds allolactose as an inducer. EcoCyc product frame: PD00763. Genomic coordinates: 366428-367510. EcoCyc protein note: The Lactose inhibitor," LacI, is a DNA-binding transcription factor that represses transcription of the operon involved in transport and catabolism of lactose . In the absence of allolactose, LacI represses the lac operon by preventing open promoter complex formation for transcription . In this repression system, LacI binds to three operators, and formation of a repressor loop between two of them is critical . This repressor binds in tandem to inverted repeat sequences that are 21 nucleotides long and possess conserved motifs . LacI is negatively autoregulated when it binds to two DNA-binding sites, one located downstream of the lacI gene and the other one located in the coding sequence for the C terminus of LacI. The protein when bound to these sites forms a loop that inhibits the transcription elongation, thus producing truncated proteins that are tagged for degradation by the small peptide SsrA...

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03023|protein.P03023]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lacI; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=lacI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001189,ECOCYC:EG10525,GeneID:945007`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:366428-367510:-; feature_type=gene
