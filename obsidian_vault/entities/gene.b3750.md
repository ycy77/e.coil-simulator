---
entity_id: "gene.b3750"
entity_type: "gene"
name: "rbsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3750"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3750"
  - "rbsC"
---

# rbsC

`gene.b3750`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3750`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsC (gene.b3750) is a gene entity. It encodes rbsC (protein.P0AGI1). Encoded protein function: FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:6327617}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from D.dadantii strain 3937 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. EcoCyc product frame: RBSC-MONOMER. EcoCyc synonyms: rbsP, rbsT. Genomic coordinates: 3935288-3936253. EcoCyc protein note: RbsC is predicted to be the inner membrane subunit of an ATP-dependent ribose uptake system . Topology analysis suggests that it contains 6 transmembrane regions with the N and C-termini located in the cytoplasm...

## Biological Role

Repressed by dsrA (gene.b1954), rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGI1|protein.P0AGI1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsC; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012261,ECOCYC:EG10816,GeneID:948262`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3935288-3936253:+; feature_type=gene
