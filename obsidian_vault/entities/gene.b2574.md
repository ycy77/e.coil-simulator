---
entity_id: "gene.b2574"
entity_type: "gene"
name: "nadB"
source_database: "NCBI RefSeq"
source_id: "gene-b2574"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2574"
  - "nadB"
---

# nadB

`gene.b2574`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2574`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadB (gene.b2574) is a gene entity. It encodes nadB (protein.P10902). Encoded protein function: FUNCTION: Catalyzes the oxidation of L-aspartate to iminoaspartate, the first step in the de novo biosynthesis of NAD(+) (PubMed:11294641, PubMed:2187483, PubMed:2841129, PubMed:7033218, PubMed:8706749, PubMed:8706750). Can use either oxygen or fumarate as electron acceptors, which allows the enzyme to be functional under aerobic and anaerobic conditions (PubMed:11294641, PubMed:12200425, PubMed:8706750). In vivo, fumarate is used under anaerobic conditions, and oxygen is the predominant electron acceptor under aerobic conditions due to the lower fumarate levels (PubMed:20149100). In vitro, fumarate is a more efficient electron acceptor and is kinetically superior to oxygen (PubMed:12200425, PubMed:20149100). {ECO:0000269|PubMed:11294641, ECO:0000269|PubMed:12200425, ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:2187483, ECO:0000269|PubMed:2841129, ECO:0000269|PubMed:7033218, ECO:0000269|PubMed:8706749, ECO:0000269|PubMed:8706750}. EcoCyc product frame: L-ASPARTATE-OXID-MONOMER. EcoCyc synonyms: nic, nicB. Genomic coordinates: 2710420-2712042. EcoCyc protein note: L-aspartate oxidase (NadB) is the first enzyme in the de novo PYRIDNUCSYN-PWY pathway, catalyzing the FAD-dependent oxidation of L-aspartate to iminoaspartate...

## Biological Role

Repressed by nadR (protein.P27278).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10902|protein.P10902]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P27278|protein.P27278]] `RegulonDB` `S` - regulator=NadR; target=nadB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008471,ECOCYC:EG10631,GeneID:947049`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2710420-2712042:+; feature_type=gene
