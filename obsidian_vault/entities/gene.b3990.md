---
entity_id: "gene.b3990"
entity_type: "gene"
name: "thiH"
source_database: "NCBI RefSeq"
source_id: "gene-b3990"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3990"
  - "thiH"
---

# thiH

`gene.b3990`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3990`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiH (gene.b3990) is a gene entity. It encodes thiH (protein.P30140). Encoded protein function: FUNCTION: Catalyzes the radical-mediated cleavage of tyrosine to 2-iminoacetate and 4-cresol. {ECO:0000269|PubMed:17403671, ECO:0000269|PubMed:17969213}. EcoCyc product frame: THIH-MONOMER. EcoCyc synonyms: thiB. Genomic coordinates: 4190735-4191868. EcoCyc protein note: 2-Iminoacetate synthase (tyrosine lyase, ThiH) participates in the synthesis of the thiazole moiety of thiamine . ThiH cleaves the Cα-Cβ bond of TYR, forming CPD-12279 (dehydroglycine) and generating CPD-108 (p-cresol) as a by-product. 2-iminoacetate is one of the three substrates required for the thiazole cyclization reaction catalyzed by ThiG . ThiH is a radical SAM enzyme that utilizes a [4Fe-4S] cluster to reductively cleave S-ADENOSYLMETHIONINE to yield methionine and a 5'-deoxyadenosyl radical. The radical abstracts a phenolic hydrogen atom from TYR, which then undergoes Cα-Cβ bond cleavage . ThiG and ThiH purify in a large multimeric complex . Because CPD-12279 is unstable and undergoes hydrolysis to glyoxylate and ammonium, complex formation between ThiG and ThiH may ensure that it is passed directly to ThiG, where it is incorporated into the thiazole carboxylate . Growth of a thiH mutant requires the presence of thiazole or thiamine . Reviews:

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30140|protein.P30140]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013048,ECOCYC:EG11590,GeneID:948494`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4190735-4191868:-; feature_type=gene
