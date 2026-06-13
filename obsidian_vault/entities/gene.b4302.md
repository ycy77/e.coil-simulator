---
entity_id: "gene.b4302"
entity_type: "gene"
name: "sgcA"
source_database: "NCBI RefSeq"
source_id: "gene-b4302"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4302"
  - "sgcA"
---

# sgcA

`gene.b4302`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4302`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcA (gene.b4302) is a gene entity. It encodes sgcA (protein.P39363). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. {ECO:0000250}. EcoCyc product frame: SGCA-MONOMER. EcoCyc synonyms: yjhL. Genomic coordinates: 4527549-4527980. EcoCyc protein note: sgcA contains an Enzyme IIA domain . Expression of sgcA is induced by acid stress .

## Biological Role

Repressed by slyA (protein.P0A8W2). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39363|protein.P39363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcA; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014100,ECOCYC:EG12554,GeneID:948831`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4527549-4527980:-; feature_type=gene
