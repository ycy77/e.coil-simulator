---
entity_id: "gene.b4041"
entity_type: "gene"
name: "plsB"
source_database: "NCBI RefSeq"
source_id: "gene-b4041"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4041"
  - "plsB"
---

# plsB

`gene.b4041`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4041`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

plsB (gene.b4041) is a gene entity. It encodes plsB (protein.P0A7A7). Encoded protein function: FUNCTION: Catalyzes the transfer of an acyl group from acyl-ACP to glycerol-3-phosphate (G3P) to form lysophosphatidic acid (LPA). This enzyme can utilize either acyl-CoA or acyl-ACP as the fatty acyl donor. {ECO:0000269|PubMed:17645809, ECO:0000269|PubMed:6997313}. EcoCyc product frame: GLYCEROL-3-P-ACYLTRANSFER-MONOMER. Genomic coordinates: 4254043-4256466. EcoCyc protein note: Membrane-bound glycerol-3-phosphate acyltransferase (PlsB) catalyzes the first committed step in phospholipid biosynthesis and is thought to function in close proximity to the succeeding enzyme 1-ACYLGLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsC) . It is specific for acylation at position 1 of GLYCEROL-3P and can utilize either fatty acyl-acyl carrier protein (acyl-ACP) or fatty acyl-coenzyme A (acyl-CoA) thioesters as acyl donors to form ACYL-SN-GLYCEROL-3P. Fatty acids that are endogenously synthesized are attached to ACP and exogenously added fatty acids are attached to CoA . In E. coli phospholipids the sn 1 position is occupied mainly by either palmitate, or cis-vaccenate, whereas the sn 2 position is predominantly palmitoleate, or cis-vaccenate. This is thought to result from the substrate preferences of the PlsB and PlsC enzymes...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7A7|protein.P0A7A7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=plsB; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013232,ECOCYC:EG10740,GeneID:948541`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4254043-4256466:-; feature_type=gene
