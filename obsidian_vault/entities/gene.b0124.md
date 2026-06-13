---
entity_id: "gene.b0124"
entity_type: "gene"
name: "gcd"
source_database: "NCBI RefSeq"
source_id: "gene-b0124"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0124"
  - "gcd"
---

# gcd

`gene.b0124`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0124`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcd (gene.b0124) is a gene entity. It encodes gcd (protein.P15877). Encoded protein function: FUNCTION: GDH is probably involved in energy conservation rather than in sugar metabolism. {ECO:0000305|PubMed:8509415}. EcoCyc product frame: GLUCDEHYDROG-MONOMER. Genomic coordinates: 138835-141225. EcoCyc protein note: Glucose dehydrogenase (Gcd) is a membrane-bound enzyme. Its role in glucose utilization is not fully clear, because under ordinary conditions it exists as an apoprotein. The enzyme requires the cofactor pyrroloquinoline quinone (PQQ) for activity, yet E. coli lacks the ability to synthesize PQQ . However, E. coli exhibits chemotaxis towards environmental PQQ , and may thus use an externally supplied cofactor. PQQ is transported across the outer membrane by the TonB-dependent transporter G6762-MONOMER PqqU . Once functional, the enzyme is able to oxidize glucose and feed electrons into the respiratory chain , but does not generate a proton motive force . The topological structure of Gcd within the membrane has been investigated and revealed five N-terminal membrane-spanning segments, with the N-terminus located in the cytoplasm and the C-terminus is located in the periplasm . The C-terminal periplasmic domain binds PQQ, contains the catalytic activity and is able to interact with ubiquinone in the cytoplasmic membrane...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15877|protein.P15877]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gcd; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gcd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000433,ECOCYC:EG10369,GeneID:944830`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:138835-141225:-; feature_type=gene
