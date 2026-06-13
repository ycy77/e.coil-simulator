---
entity_id: "gene.b4477"
entity_type: "gene"
name: "dgoA"
source_database: "NCBI RefSeq"
source_id: "gene-b4477"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4477"
  - "dgoA"
---

# dgoA

`gene.b4477`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4477`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgoA (gene.b4477) is a gene entity. It encodes dgoA (protein.Q6BF16). Encoded protein function: FUNCTION: Involved in the degradation of galactose via the DeLey-Doudoroff pathway. Catalyzes the reversible, stereospecific retro-aldol cleavage of 2-keto-3-deoxy-6-phosphogalactonate (KDPGal) to pyruvate and D-glyceraldehyde-3-phosphate. In the synthetic direction, it catalyzes the addition of pyruvate to electrophilic aldehydes with re-facial selectivity. It can use a limited number of aldehyde substrates, including D-glyceraldehyde-3-phosphate (natural substrate), D-glyceraldehyde, glycolaldehyde, 2-pyridinecarboxaldehyde, D-ribose, D-erythrose and D-threose. It efficiently catalyzes aldol addition only using pyruvate as the nucleophilic component and accepts both stereochemical configurations at C2 of the electrophile. {ECO:0000269|PubMed:17981470, ECO:0000269|PubMed:324806}. EcoCyc product frame: DEHYDDEOXPHOSGALACT-ALDOL-MONOMER. EcoCyc synonyms: b3692, yidU. Genomic coordinates: 3872995-3873612. EcoCyc protein note: 2-oxo-3-deoxygalactonate 6-phosphate aldolase (KDPGal aldolase) catalyzes the final reaction in the degradation of D-galactonate, an aldol cleavage resulting in GA3P and pyruvate which enter central metabolism . Crystal structures of KDPGal aldolase have been determined...

## Biological Role

Repressed by dgoR (protein.P31460). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q6BF16|protein.Q6BF16]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=dgoA; function=+
- `represses` <-- [[protein.P31460|protein.P31460]] `RegulonDB` `C` - regulator=DgoR; target=dgoA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174107,ECOCYC:EG20049,GeneID:2847766`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3872995-3873612:-; feature_type=gene
