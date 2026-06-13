---
entity_id: "gene.b2245"
entity_type: "gene"
name: "yfaU"
source_database: "NCBI RefSeq"
source_id: "gene-b2245"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2245"
  - "yfaU"
---

# yfaU

`gene.b2245`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2245`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfaU (gene.b2245) is a gene entity. It encodes rhmA (protein.P76469). Encoded protein function: FUNCTION: Catalyzes the reversible retro-aldol cleavage of 2-keto-3-deoxy-L-rhamnonate (KDR) to pyruvate and lactaldehyde. 2-keto-3-deoxy-L-mannonate, 2-keto-3-deoxy-L-lyxonate and 4-hydroxy-2-ketoheptane-1,7-dioate (HKHD) are also reasonably good substrates, although 2-keto-3-deoxy-L-rhamnonate is likely to be the physiological substrate (PubMed:18754683, PubMed:18754693). In vitro, can catalyze the aldolisation reaction between hydroxypyruvate (HPA) or pyruvate (PA) and D-glyceraldehyde (D-GA) (Ref.6). The condensation of hydroxypyruvate and D-glyceraldehyde produces (3R,4S,5R)-3,4,5,6-tetrahydroxy-2-oxohexanoate as the major product, 2-dehydro-D-gluconate and 2-dehydro-D-galactonate (Ref.6). The condensation of pyruvate and D-glyceraldehyde produces 2-dehydro-3-deoxy-L-galactonate as the major product and 2-dehydro-3-deoxy-D-gluconate (Ref.6). {ECO:0000269|PubMed:18754683, ECO:0000269|PubMed:18754693, ECO:0000269|Ref.6}. EcoCyc product frame: G7158-MONOMER. Genomic coordinates: 2358042-2358845. EcoCyc protein note: YfaU is a 2-keto-3-deoxy-L-rhamnonate aldolase which catalyzes a retro-aldol reaction with somewhat relaxed substrate specificity...

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76469|protein.P76469]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007431,ECOCYC:G7158,GeneID:948054`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2358042-2358845:-; feature_type=gene
