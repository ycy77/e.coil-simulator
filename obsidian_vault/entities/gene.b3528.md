---
entity_id: "gene.b3528"
entity_type: "gene"
name: "dctA"
source_database: "NCBI RefSeq"
source_id: "gene-b3528"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3528"
  - "dctA"
---

# dctA

`gene.b3528`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3528`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dctA (gene.b3528) is a gene entity. It encodes dctA (protein.P0A830). Encoded protein function: FUNCTION: Responsible for the aerobic transport of the dicarboxylates fumarate, L- and D-malate and to a lesser extent succinate, from the periplasm across the inner membrane. {ECO:0000269|PubMed:17088549}. EcoCyc product frame: DCTA-MONOMER. Genomic coordinates: 3682161-3683447. EcoCyc protein note: DctA is required for dicarboxylate transport . DctA is a proton motive force-dependent C4-dicarboxylate transporter, responsible for the uptake of fumarate, succinate, L-aspartate and L- and D-malate under aerobic conditions, and also for the uptake of orotate, a pyrimidine precursor . The substrate recognition site of DctA is located on the outer surface of the inner membrane . DctA and DcuB function as co-sensors with DCUS-MONOMER "DcuS" - the sensor histidine kinase of the two-component system that controls the expression of genes required for C4-dicarboxylate degradation. DcuS requires the transport proteins DctA or DcuB for normal function. DctA interacts specifically with DcuS in vivo . DctA is predicted to contain eight transmembrane helices with the N and C-termini located in the cytoplasm. Residues important for interaction with DcuS are located in α-helix 8b...

## Biological Role

Activated by crp (protein.P0ACJ8), dcuR (protein.P0AD01).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A830|protein.P0A830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=dctA; function=+
- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=dctA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011527,ECOCYC:EG20044,GeneID:948039`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3682161-3683447:-; feature_type=gene
