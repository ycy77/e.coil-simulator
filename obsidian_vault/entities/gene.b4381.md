---
entity_id: "gene.b4381"
entity_type: "gene"
name: "deoC"
source_database: "NCBI RefSeq"
source_id: "gene-b4381"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4381"
  - "deoC"
---

# deoC

`gene.b4381`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4381`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

deoC (gene.b4381) is a gene entity. It encodes deoC (protein.P0A6L0). Encoded protein function: FUNCTION: Catalyzes a reversible aldol reaction between acetaldehyde and D-glyceraldehyde 3-phosphate to generate 2-deoxy-D-ribose 5-phosphate (PubMed:11598300, PubMed:17905878, PubMed:6749498). Can also catalyze the double aldol condensation of three acetaldehyde molecules, leading to the formation of 2,4,6-trideoxyhexose (Ref.5). {ECO:0000269|PubMed:11598300, ECO:0000269|PubMed:17905878, ECO:0000269|PubMed:6749498, ECO:0000269|Ref.5}. EcoCyc product frame: DEOXYRIBOSE-P-ALD-MONOMER. EcoCyc synonyms: tlr, dra, thyR. Genomic coordinates: 4617323-4618102. EcoCyc protein note: DeoC is a deoxyribose-phosphate aldolase which is part of the pathway that utilizes pyrimidine deoxyribonucleoside as a carbon and energy source. Deoxyribose-phosphate aldolase catalyzes the aldol reaction between the acetaldehyde donor and glyceraldehyde 3-phosphate acceptor to generate deoxyribose 5-phosphate. It belongs to the class I aldolases which form Schiff base intermediates. The purified enzyme may exist as both a monomer and a dimer. The enzyme exists as a monomer in Tris/HCl containing EDTA and as a dimer in phosphate buffer. The crystal structure of a covalent complex of deoxyribose phosphate aldolase with deoxyribose 5-phosphate was resolved to 1.05 Å...

## Biological Role

Repressed by modE (protein.P0A9G8), crp (protein.P0ACJ8), deoR (protein.P0ACK5), cytR (protein.P0ACN7). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6L0|protein.P0A6L0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoC; function=-+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=deoC; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoC; function=-+
- `represses` <-- [[protein.P0ACK5|protein.P0ACK5]] `RegulonDB` `S` - regulator=DeoR; target=deoC; function=-
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=deoC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014371,ECOCYC:EG10221,GeneID:948902`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4617323-4618102:+; feature_type=gene
