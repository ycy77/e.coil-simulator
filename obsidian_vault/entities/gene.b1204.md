---
entity_id: "gene.b1204"
entity_type: "gene"
name: "pth"
source_database: "NCBI RefSeq"
source_id: "gene-b1204"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1204"
  - "pth"
---

# pth

`gene.b1204`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1204`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pth (gene.b1204) is a gene entity. It encodes pth (protein.P0A7D1). Encoded protein function: FUNCTION: Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino acids incorporated), which drop off the ribosome during protein synthesis, or as a result of ribosome stalling (PubMed:4866985, PubMed:4898482, PubMed:9303320). {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000269|PubMed:4866985, ECO:0000269|PubMed:4898482, ECO:0000269|PubMed:9303320}.; FUNCTION: The hydrolysis rate of peptidyl-tRNAs depends on the peptide chain length, with peptidyl-tRNAs with up to 5 residues being a better substrate; Gly(4)-Phe-tRNA(Phe) is hydrolyzed faster than Gly(2)-Phe-tRNA(Phe) which is hydrolyzed faster than Gly-Phe-tRNA(Phe) (PubMed:4898482). Also acts on singly charged tRNAs including charged tRNA(Ile), tRNA(Leu), tRNA(Ser), tRNA(Thr) and tRNA(Val) (PubMed:4866985). Acts on charged tRNA(Lys) (PubMed:9303320). Unblocked charged tRNAs are very poor substrates, discrimination is mediated by Asn-11 which binds to the main-chain carbonyl of the penultimate residue (PubMed:21718701). Acts on charged tRNA(Ala) (PubMed:22923517). Involved in lambda inhibition of host protein synthesis (PubMed:1833189). Pth activity may, directly or indirectly, be the target for lambda bar RNA leading to rap cell death (PubMed:1833189)...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7D1|protein.P0A7D1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pth; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004043,ECOCYC:EG10785,GeneID:945765`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1257929-1258513:-; feature_type=gene
