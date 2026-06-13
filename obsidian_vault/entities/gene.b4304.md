---
entity_id: "gene.b4304"
entity_type: "gene"
name: "sgcC"
source_database: "NCBI RefSeq"
source_id: "gene-b4304"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4304"
  - "sgcC"
---

# sgcC

`gene.b4304`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4304`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcC (gene.b4304) is a gene entity. It encodes sgcC (protein.P39365). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}. EcoCyc product frame: SGCC-MONOMER. EcoCyc synonyms: yjhN. Genomic coordinates: 4528930-4530243. EcoCyc protein note: sgcC is predicted to encode a protein with 9 or 10 transmembrane helices; it shows sequence similarity to the Enzyme IIC domain of the galactitol PTS .

## Biological Role

Repressed by slyA (protein.P0A8W2), glaR (protein.P37338). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39365|protein.P39365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcC; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcC; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=sgcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014105,ECOCYC:EG12556,GeneID:946849`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4528930-4530243:-; feature_type=gene
