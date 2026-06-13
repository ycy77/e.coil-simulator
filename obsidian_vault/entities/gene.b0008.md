---
entity_id: "gene.b0008"
entity_type: "gene"
name: "talB"
source_database: "NCBI RefSeq"
source_id: "gene-b0008"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0008"
  - "talB"
---

# talB

`gene.b0008`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0008`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

talB (gene.b0008) is a gene entity. It encodes talB (protein.P0A870). Encoded protein function: FUNCTION: Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway. {ECO:0000269|PubMed:18687684, ECO:0000269|PubMed:7592346}. EcoCyc product frame: TRANSALDOLB-MONOMER. EcoCyc synonyms: yaaK. Genomic coordinates: 8238-9191. EcoCyc protein note: Transaldolase B is an enzyme of the non-oxidative branch of the pentose phosphate pathway. Along with transketolase, transaldolase creates a reversible link between the pentose phosphate pathway and glycolysis. It catalyzes the interconversion of glyceraldehyde-3-phosphate and sedoheptulose-7-phosphate to fructose-6-phosphate and erythrose-4-phosphate. The reversibility of this reaction and carbon flux through the pentose phosphate pathway has been addressed both experimentally (summarized in ) and theoretically . There are two closely related transaldolases in E. coli, encoded by talA and talB. Only transaldolase B has been biochemically characterized. TalB is a dimer in solution and in the crystal structure . Mutation of the R300 residue leads to the formation of catalytically active monomers . Catalytically important active site residues have been identified by site-directed mutagenesis...

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A870|protein.P0A870]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000027,ECOCYC:EG11556,GeneID:944748`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:8238-9191:+; feature_type=gene
