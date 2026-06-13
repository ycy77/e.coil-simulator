---
entity_id: "gene.b1309"
entity_type: "gene"
name: "ycjM"
source_database: "NCBI RefSeq"
source_id: "gene-b1309"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1309"
  - "ycjM"
---

# ycjM

`gene.b1309`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1309`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjM (gene.b1309) is a gene entity. It encodes ycjM (protein.P76041). Encoded protein function: FUNCTION: Catalyzes the reversible phosphorolysis of glucosylglycerate into alpha-D-glucose 1-phosphate (Glc1P) and D-glycerate (also called (R)-glycerate) (PubMed:28754708, PubMed:29684280). May be a regulator of intracellular levels of glucosylglycerate, a compatible solute that primarily protects organisms facing salt stress and very specific nutritional constraints (PubMed:28754708). Cannot catalyze the phosphorolysis of sucrose (PubMed:28754708). Does not act on other sugars such as alpha-D-galactose 1-phosphate, alpha-D-mannose 1-phosphate or beta-D-glucose 1-phosphate; in vitro D-erythronate can substitute for D-glycerate with a much lower efficiency (PubMed:29684280). {ECO:0000269|PubMed:28754708, ECO:0000269|PubMed:29684280}. EcoCyc product frame: G6647-MONOMER. EcoCyc synonyms: ggaP. Genomic coordinates: 1370216-1371895. EcoCyc protein note: YcjM and an enzyme from Meiothermus silvanus both belong to the same subfamily of the GH13_18 family of phosphorylases. The purified M. silvanus enzyme as well as overexpressed, but unpurified YcjM are able to catalyze synthesis of glucosylglycerol from glucose-1-phosphate and glycerol. YcjM showed no activity with sucrose and many other potential acceptor substrates...

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76041|protein.P76041]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004400,ECOCYC:G6647,GeneID:945659`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1370216-1371895:+; feature_type=gene
