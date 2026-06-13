---
entity_id: "gene.b2750"
entity_type: "gene"
name: "cysC"
source_database: "NCBI RefSeq"
source_id: "gene-b2750"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2750"
  - "cysC"
---

# cysC

`gene.b2750`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2750`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysC (gene.b2750) is a gene entity. It encodes cysC (protein.P0A6J1). Encoded protein function: FUNCTION: Catalyzes the synthesis of activated sulfate. EcoCyc product frame: ADENYLYLSULFKIN-MONOMER. Genomic coordinates: 2873387-2873992. EcoCyc protein note: Adenylylsulfate kinase (CysC) is involved in the assimilation of sulfate and catalyzes the phosphorylation of adenosine 5-phosphosulfate (APS) to yield 3-phosphoadenosine 5-phosphosulfate (PAPS). The enzyme picks up MgATP first then binds to the substrate indicating the reaction is ordered sequential . The enzyme exhibits a complex steady-state kinetic behavior, showing a variation of ping-pong to sequential pathways as the APS concentration increases . Serine-109 has been identified as the residue that is phosphorylated when incubated with ATP . The enzyme exists predominantly as a homodimer, but a tetrameric form exists when the enzyme is dephosphorylated . cysC, along with cysN and cysD, resides in the sulfate activation operon .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6J1|protein.P0A6J1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009023,ECOCYC:EG10185,GeneID:947221`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2873387-2873992:-; feature_type=gene
