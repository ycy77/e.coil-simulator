---
entity_id: "gene.b2066"
entity_type: "gene"
name: "udk"
source_database: "NCBI RefSeq"
source_id: "gene-b2066"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2066"
  - "udk"
---

# udk

`gene.b2066`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2066`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

udk (gene.b2066) is a gene entity. It encodes udk (protein.P0A8F4). Encoded protein function: Uridine kinase (EC 2.7.1.48) (Cytidine monophosphokinase) (Uridine monophosphokinase) EcoCyc product frame: UDK-MONOMER. Genomic coordinates: 2142307-2142948. EcoCyc protein note: Uridine-cytidine kinase phosphorylates both uridine and cytidine; GTP and dGTP are the most efficient phosphate donors . Uridine-cytidine kinase was found to have a molecular weight of 90,000 by gel filtration and is thus likely not monomeric . Overexpression of uridine-cytidine kinase inhibits growth of the bacteriophage T7, particularly in a T7 gp0.7 mutant , due to inadequate inhibition of host RNA polymerase . Overexpression of Udk mimics the absence of Gp2 during T7 infection .

## Biological Role

Activated by rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8F4|protein.P0A8F4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `S` - regulator=RbsR; target=udk; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006840,ECOCYC:EG11701,GeneID:946597`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2142307-2142948:-; feature_type=gene
