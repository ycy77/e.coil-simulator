---
entity_id: "gene.b3991"
entity_type: "gene"
name: "thiG"
source_database: "NCBI RefSeq"
source_id: "gene-b3991"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3991"
  - "thiG"
---

# thiG

`gene.b3991`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3991`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiG (gene.b3991) is a gene entity. It encodes thiG (protein.P30139). Encoded protein function: FUNCTION: Catalyzes the rearrangement of 1-deoxy-D-xylulose 5-phosphate (DXP) to produce the thiazole phosphate moiety of thiamine. Sulfur is provided by the thiocarboxylate moiety of the carrier protein ThiS. In vitro, sulfur can be provided by H(2)S. {ECO:0000269|PubMed:12650933}. EcoCyc product frame: THIG-MONOMER. EcoCyc synonyms: thiB. Genomic coordinates: 4191865-4192635. EcoCyc protein note: 1-deoxy-D-xylulose 5-phosphate:thiol sulfurtransferase (ThiG) participates in the synthesis of the thiazole moiety of thiamine . ThiG is responsible for a complex cyclization reaction; formation of CPD-13575 requires 1-deoxyxylulose 5-phosphate, a sulfur atom from cysteine which is transferred via ThiS, and CPD-12279 (dehydroglycine) produced by the tyrosine lyase ThiH . ThiG purifies in a large multimeric complex with ThiH . Because CPD-12279 is unstable and undergoes hydrolysis to glyoxylate and ammonium, complex formation between ThiG and ThiH may ensure that it is passed directly from ThiH to ThiG . Growth of a thiG insertion mutant requires the presence of thiazole or thiamine...

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30139|protein.P30139]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013050,ECOCYC:EG11589,GeneID:948493`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4191865-4192635:-; feature_type=gene
