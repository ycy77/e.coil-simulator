---
entity_id: "gene.b4565"
entity_type: "gene"
name: "sgcB"
source_database: "NCBI RefSeq"
source_id: "gene-b4565"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4565"
  - "sgcB"
---

# sgcB

`gene.b4565`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4565`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcB (gene.b4565) is a gene entity. It encodes sgcB (protein.P58035). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. {ECO:0000250}. EcoCyc product frame: MONOMER0-2121. Genomic coordinates: 4530255-4530533. EcoCyc protein note: sgcB contains an Enzyme IIB domain with a conserved cysteine residue (Cys8)

## Biological Role

Repressed by slyA (protein.P0A8W2). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P58035|protein.P58035]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcB; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285086,ECOCYC:G0-10241,GeneID:1450295`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4530255-4530533:-; feature_type=gene
