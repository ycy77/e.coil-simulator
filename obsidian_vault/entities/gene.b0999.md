---
entity_id: "gene.b0999"
entity_type: "gene"
name: "cbpM"
source_database: "NCBI RefSeq"
source_id: "gene-b0999"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0999"
  - "cbpM"
---

# cbpM

`gene.b0999`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0999`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbpM (gene.b0999) is a gene entity. It encodes cbpM (protein.P63264). Encoded protein function: FUNCTION: Interacts with CbpA and inhibits both the DnaJ-like co-chaperone activity and the DNA binding activity of CbpA. Together with CbpA, modulates the activity of the DnaK chaperone system. Does not inhibit the co-chaperone activity of DnaJ. EcoCyc product frame: EG12194-MONOMER. EcoCyc synonyms: yccD. Genomic coordinates: 1062550-1062855. EcoCyc protein note: CbpM specifically inhibits both the DNA binding and co-chaperone activity of CbpA in vitro and in vivo . The CbpM and CbpA proteins interact . The amino acid determinants within CbpM that are required for this interaction have been mapped . When CbpM is not bound to CbpA, it is a target for the Lon and ClpAP proteases . The cbpAM operon is maximally transcribed during the transition from exponential growth to stationary phase . CbpM accumulates in late stationary phase . CbpM: "CbpA modulator"

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63264|protein.P63264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cbpM; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=cbpM; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=cbpM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003377,ECOCYC:EG12194,GeneID:945597`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1062550-1062855:-; feature_type=gene
