---
entity_id: "gene.b1265"
entity_type: "gene"
name: "trpL"
source_database: "NCBI RefSeq"
source_id: "gene-b1265"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1265"
  - "trpL"
---

# trpL

`gene.b1265`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1265`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpL (gene.b1265) is a gene entity. It encodes trpL (protein.P0AD92). Encoded protein function: FUNCTION: This protein is involved in control of the biosynthesis of tryptophan. EcoCyc product frame: EG11274-MONOMER. EcoCyc synonyms: trpEE. Genomic coordinates: 1323038-1323082. EcoCyc protein note: The TrpL leader peptide is a key component in the attenuation system that controls expression of the trpLEDCBA operon in response to tryptophan availability . trpL occurs within a 130-nucleotide region at the beginning of the trp operon . The TrpL peptide contains tandem tryptophan residues that serve as the regulatory region during attenuation . Review:

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rydC (gene.b4597), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD92|protein.P0AD92]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=trpL; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpL; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=trpL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004246,ECOCYC:EG11274,GeneID:945856`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1323038-1323082:-; feature_type=gene
