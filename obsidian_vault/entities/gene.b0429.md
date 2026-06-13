---
entity_id: "gene.b0429"
entity_type: "gene"
name: "cyoD"
source_database: "NCBI RefSeq"
source_id: "gene-b0429"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0429"
  - "cyoD"
---

# cyoD

`gene.b0429`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0429`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyoD (gene.b0429) is a gene entity. It encodes cyoD (protein.P0ABJ6). Encoded protein function: FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. EcoCyc product frame: CYOD-MONOMER. Genomic coordinates: 447717-448046. EcoCyc protein note: CyoD is subunit IV of the cytochrome bo3 complex. Subunit IV is required for a functional complex but its exact contribution remains uncertain The CyoD polypeptide contains three transmembrane helices . Deletion and cross-linking studies have suggested that subunit IV interacts with subunits I and III , which is confirmed by the crystal structure of the entire cytochrome bo terminal oxidase complex . cyoD belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABJ6|protein.P0ABJ6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cyoD; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=cyoD; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=cyoD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001487,ECOCYC:EG10181,GeneID:944918`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:447717-448046:-; feature_type=gene
