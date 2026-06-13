---
entity_id: "gene.b4375"
entity_type: "gene"
name: "prfC"
source_database: "NCBI RefSeq"
source_id: "gene-b4375"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4375"
  - "prfC"
---

# prfC

`gene.b4375`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4375`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prfC (gene.b4375) is a gene entity. It encodes prfC (protein.P0A7I4). Encoded protein function: FUNCTION: Increases the formation of ribosomal termination complexes and stimulates activities of RF-1 and RF-2. It binds guanine nucleotides and has strong preference for UGA stop codons. It may interact directly with the ribosome. The stimulation of RF-1 and RF-2 is significantly reduced by GTP and GDP, but not by GMP. EcoCyc product frame: EG12114-MONOMER. EcoCyc synonyms: miaD, tos. Genomic coordinates: 4609414-4611003. EcoCyc protein note: Release factor 3 (RF3), a class II release factor, is a ribosome-dependent GTPase that stimulates the release of RF1 and RF2 from the ribosome after peptide chain termination. The action requires nucleotide exchange and hydrolysis of GTP. EG10762-MONOMER RF2 of E. coli K-12 contains threonine at position 246, which decreases its termination efficiency. Some physiological defects associated with the loss of RF3 discussed below appear to be due to the variant RF2 present in E. coli K-12 . The presence of RF3 alleviates the defects associated with the reduced-function RF2 allele . It was initially found that RF3 stimulates the release of the growing polypeptide chain at stop codons; unlike RF1 and RF2, it is not codon-specific . Rather, RF3 stimulates the activities of RF1 and RF2...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7I4|protein.P0A7I4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=prfC; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=prfC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014346,ECOCYC:EG12114,GeneID:948897`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4609414-4611003:+; feature_type=gene
