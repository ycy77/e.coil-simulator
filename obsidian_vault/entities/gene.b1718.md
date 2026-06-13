---
entity_id: "gene.b1718"
entity_type: "gene"
name: "infC"
source_database: "NCBI RefSeq"
source_id: "gene-b1718"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1718"
  - "infC"
---

# infC

`gene.b1718`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1718`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

infC (gene.b1718) is a gene entity. It encodes infC (protein.P0A707). Encoded protein function: FUNCTION: One of the essential components for the initiation of protein synthesis. IF-3 binds to the 30S ribosomal subunit and shifts the equilibrium between 70S ribosomes and their 50S and 30S subunits in favor of the free subunits, thus enhancing the availability of 30S subunits on which protein synthesis initiation begins. {ECO:0000269|PubMed:22562136}. EcoCyc product frame: EG10506-MONOMER. EcoCyc synonyms: fit, srjA. Genomic coordinates: 1800096-1800638. EcoCyc protein note: IF-3 is one of three translation initiation factors in E. coli . It was also initially identified as a ribosomal dissociation factor . The interaction sites of IF-3 with the 30S subunit have been mapped . The A790G and U789C mutations in 16S rRNA decreases translation fidelity, which may be due to decreased affinity of the 30S subunit for IF-3 . The m2G966 and m5C967 residues of 16S rRNA appear to be important for interaction with IF-3 . After the 30S subunit has dissociated from the post-termination ribosome in a process that requires RRF, EF-G, and GTP hydrolysis, IF-3 binds and stimulates dissociation of deacylated tRNA and destabilizes binding of all tested tRNAs to the 30S subunit . IF-3 also destabilizes incorrect initiation ternary complexes...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A707|protein.P0A707]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=infC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005734,ECOCYC:EG10506,GeneID:946225`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1800096-1800638:-; feature_type=gene
