---
entity_id: "gene.b1717"
entity_type: "gene"
name: "rpmI"
source_database: "NCBI RefSeq"
source_id: "gene-b1717"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1717"
  - "rpmI"
---

# rpmI

`gene.b1717`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1717`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmI (gene.b1717) is a gene entity. It encodes rpmI (protein.P0A7Q1). Encoded protein function: Large ribosomal subunit protein bL35 (50S ribosomal protein L35) (Ribosomal protein A) EcoCyc product frame: EG11231-MONOMER. Genomic coordinates: 1799802-1799999. EcoCyc protein note: The L35 protein is a component of the 50S subunit of the ribosome . L35 can be crosslinked to the spiramycin derivative dihydrospiramycin and may thus be located near the peptidyl transferase center . Profiles of ribosomes isolated from a ΔEG11232 rpmJ mutant show a minor peak at 40S that lacks the late assembly proteins L16 and L35 . Ribosomes isolated from a ΔEG11507 rlmE strain lack L16, L35 and L36 . Expression of rpmI is regulated at the posttranscriptional level by EG10881-MONOMER. Two mRNA regions, one located within infC and a second located close to the translation start site of rpmI, form a long-range RNA pseudoknot structure . Both the pseudoknot structure and a second stem-loop binding site are required for repression , and both sites share secondary structure similarity with the L20 binding site in rRNA . The two binding sites interact, and only one molecule of L20 binds to the regulatory region . Decreased translation of infC leads to increased L20-mediated repression of L35 expression; translating ribosomes may disrupt the RNA pseudoknot structure, thereby attenuating repression...

## Biological Role

Repressed by rplT (protein.P0A7L3). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Q1|protein.P0A7Q1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpmI; function=+
- `represses` <-- [[protein.P0A7L3|protein.P0A7L3]] `RegulonDB` `S` - regulator=RplT; target=rpmI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005732,ECOCYC:EG11231,GeneID:946349`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1799802-1799999:-; feature_type=gene
