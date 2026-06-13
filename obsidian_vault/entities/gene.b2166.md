---
entity_id: "gene.b2166"
entity_type: "gene"
name: "psuK"
source_database: "NCBI RefSeq"
source_id: "gene-b2166"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2166"
  - "psuK"
---

# psuK

`gene.b2166`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2166`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

psuK (gene.b2166) is a gene entity. It encodes psuK (protein.P30235). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of pseudouridine to pseudouridine 5'-phosphate (PsiMP). {ECO:0000269|PubMed:18591240}. EcoCyc product frame: EG11646-MONOMER. EcoCyc synonyms: yeiC, pscK. Genomic coordinates: 2258355-2259296. EcoCyc protein note: E. coli strains B and W were shown to contain a pseudouridine kinase activity and are able to grow on pseudouridine as the sole source of pyrimidine . YeiC from the uropathogenic E. coli UTI89 is a pseudouridine kinase; yeiC is the most highly induced gene when UTI89 is grown on human urine . The crystal structures of apo-PsuK and PsuK complexed with Ψ or N1-methyl-pseudouridine (m1Ψ) were characterized from E. coli strain BL21 (DE3) . PscK: "pseudouridine catabolism, kinase" PsuK: "pseudouridine catabolism, kinase"

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30235|protein.P30235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=psuK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007168,ECOCYC:EG11646,GeneID:946664`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2258355-2259296:-; feature_type=gene
