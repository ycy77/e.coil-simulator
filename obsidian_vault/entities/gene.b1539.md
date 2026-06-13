---
entity_id: "gene.b1539"
entity_type: "gene"
name: "ydfG"
source_database: "NCBI RefSeq"
source_id: "gene-b1539"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1539"
  - "ydfG"
---

# ydfG

`gene.b1539`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1539`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfG (gene.b1539) is a gene entity. It encodes ydfG (protein.P39831). Encoded protein function: FUNCTION: NADP-dependent dehydrogenase with broad substrate specificity acting on 3-hydroxy acids. Catalyzes the NADP-dependent oxidation of L-allo-threonine to L-2-amino-3-keto-butyrate, which is spontaneously decarboxylated into aminoacetone. Also acts on D-threonine, L-serine, D-serine, D-3-hydroxyisobutyrate, L-3-hydroxyisobutyrate, D-glycerate and L-glycerate (PubMed:12535615). Able to catalyze the reduction of the malonic semialdehyde to 3-hydroxypropionic acid. YdfG is apparently supplementing RutE, the presumed malonic semialdehyde reductase involved in pyrimidine degradation since both are able to detoxify malonic semialdehyde (PubMed:20400551). {ECO:0000269|PubMed:12535615, ECO:0000269|PubMed:20400551}. EcoCyc product frame: EG12345-MONOMER. Genomic coordinates: 1627517-1628263. EcoCyc protein note: The ydfG gene belongs to the short-chain dehydrogenase/reductase (SDR) family and encodes a homotetrameric NADP+-dependent 3-hydroxy acid dehydrogenase, also called a serine dehydrogenase (SerDH). The high Km for NADP+ indicates that the enzyme acts in the reductive direction in vivo . A ydfG deletion mutant only grows poorly with uridine as the sole source of nitrogen, likely due to toxicity of the pathway intermediate, malonic semialdehyde...

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39831|protein.P39831]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005137,ECOCYC:EG12345,GeneID:946085`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1627517-1628263:+; feature_type=gene
