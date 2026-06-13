---
entity_id: "gene.b0014"
entity_type: "gene"
name: "dnaK"
source_database: "NCBI RefSeq"
source_id: "gene-b0014"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0014"
  - "dnaK"
---

# dnaK

`gene.b0014`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0014`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaK (gene.b0014) is a gene entity. It encodes dnaK (protein.P0A6Y8). Encoded protein function: FUNCTION: Plays an essential role in the initiation of phage lambda DNA replication, where it acts in an ATP-dependent fashion with the DnaJ protein to release lambda O and P proteins from the preprimosomal complex. DnaK is also involved in chromosomal DNA replication, possibly through an analogous interaction with the DnaA protein. Also participates actively in the response to hyperosmotic shock. EcoCyc product frame: EG10241-MONOMER. EcoCyc synonyms: groPF, groPC, seg, grpF, grpC, groPAB. Genomic coordinates: 12163-14079. EcoCyc protein note: DnaK is a Hsp70 (heat shock protein 70 kDa) chaperone. It assists in a number of cytoplasmic cellular processes involved in a "protein quality control" network, including folding of nascent polypeptide chains , rescue of misfolded proteins and protein secretion . The chaperone action of DnaK is powered by ATP hydrolysis and assisted by partner chaperones CPLX0-8191 "DnaJ", EG12193-MONOMER CbpA, EG11570-MONOMER DjlA and the nucleotide exchange factor CPLX0-8192 "GrpE". The DnaK system contributes to control of the heat shock response in E. coli through its interaction with RPOH-MONOMER "σ32", the primary sigma factor controlling heat shock response during log phase growth (reviewed in )...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Y8|protein.P0A6Y8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=dnaK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000052,ECOCYC:EG10241,GeneID:944750`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:12163-14079:+; feature_type=gene
