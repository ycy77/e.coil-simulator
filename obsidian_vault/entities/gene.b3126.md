---
entity_id: "gene.b3126"
entity_type: "gene"
name: "garL"
source_database: "NCBI RefSeq"
source_id: "gene-b3126"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3126"
  - "garL"
---

# garL

`gene.b3126`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3126`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

garL (gene.b3126) is a gene entity. It encodes garL (protein.P23522). Encoded protein function: FUNCTION: Catalyzes the reversible retro-aldol cleavage of both 5-keto-4-deoxy-D-glucarate and 2-keto-3-deoxy-D-glucarate to pyruvate and tartronic semialdehyde (PubMed:9772162, Ref.5). In vitro, can catalyze the aldolisation reaction between hydroxypyruvate (HPA) or pyruvate (PA) and D-glyceraldehyde (D-GA) (Ref.7). The condensation of hydroxypyruvate and D-glyceraldehyde produces 2-dehydro-D-gluconate as the major product (Ref.7). The condensation of pyruvate and D-glyceraldehyde produces 2-dehydro-3-deoxy-L-galactonate as the major product and 2-dehydro-3-deoxy-D-gluconate (Ref.7). {ECO:0000269|PubMed:9772162, ECO:0000269|Ref.5, ECO:0000269|Ref.7}. EcoCyc product frame: KDGALDOL-MONOMER. EcoCyc synonyms: yhaF. Genomic coordinates: 3272787-3273557. EcoCyc protein note: α-dehydro-β-deoxy-D-glucarate aldolase cleaves both 5-dehydro-4-deoxy- and 2-dehydro-3-deoxy-D-glucarate, thereby continuing the catabolism of D-glucarate and D-galactarate . Crystal structures of the enzyme alone and in complex with pyruvate have been solved. The enzyme is a hexamer that may be assembled by association of three dimers .

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23522|protein.P23522]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=garL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010276,ECOCYC:EG10016,GeneID:947630`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3272787-3273557:-; feature_type=gene
