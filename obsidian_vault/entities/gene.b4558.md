---
entity_id: "gene.b4558"
entity_type: "gene"
name: "lptM"
source_database: "NCBI RefSeq"
source_id: "gene-b4558"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4558"
  - "lptM"
---

# lptM

`gene.b4558`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4558`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptM (gene.b4558) is a gene entity. It encodes lptM (protein.P0ADN6). Encoded protein function: FUNCTION: Component of the lipopolysaccharide (LPS) transport (Lpt) pathway that promotes efficient assembly of the outer membrane LPS translocon (LptDE) by the BAM complex (PubMed:37821449). Facilitates oxidative maturation of LptD by stabilizing a conformation of the LPS translocon in which LptD can efficiently acquire native disulfide bonds, thereby activating the LPS translocon (PubMed:37821449). Might stabilize an active conformation of the LPS translocon by mimicking its natural substrate (PubMed:37821449). {ECO:0000269|PubMed:37821449}. EcoCyc product frame: MONOMER0-2693. EcoCyc synonyms: yifL. Genomic coordinates: 3994522-3994725. EcoCyc protein note: lptM (formerly yifL) encodes a lipoprotein that interacts with the CPLX0-7628 outer membrane lipopolysaccharide (LPS) translocon and promotes its efficient assembly at the BAM complex . LptM promotes EG11569-MONOMER LptD oxidative maturation; LptM acts synergistically with DISULFOXRED-MONOMER DsbA in promoting proper oxidative maturation of LptD. LptM stably associates with LptDE forming a 1:1:1 heterotrimeric complex; LptM binds to sites in both LptD and EG10855-MONOMER LptE that are important in coordinating LPS insertion into the outer membrane . LptM interacts with LptD to facilitate the later stages of LptD maturation...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADN6|protein.P0ADN6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lptM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285079,ECOCYC:G0-10471,GeneID:1450304`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3994522-3994725:+; feature_type=gene
