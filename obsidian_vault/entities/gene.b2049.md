---
entity_id: "gene.b2049"
entity_type: "gene"
name: "cpsB"
source_database: "NCBI RefSeq"
source_id: "gene-b2049"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2049"
  - "cpsB"
---

# cpsB

`gene.b2049`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2049`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpsB (gene.b2049) is a gene entity. It encodes manC (protein.P24174). Encoded protein function: FUNCTION: Involved in the biosynthesis of the capsular polysaccharide colanic acid. EcoCyc product frame: MANNPGUANYLTRANGDP-MONOMER. EcoCyc synonyms: rfbM, manC, mni. Genomic coordinates: 2123084-2124520. EcoCyc protein note: Mannose-1-phosphate guanylyltransferase is involved in the biosynthesis of the capsular polysaccharide colanic acid. Colanic acid is a high molecular weight repeating polymer of glucose, galactose, fucose and glucuronic acid (see PWY-8243). The enzyme has only been assayed in crude extract . cpsB expression is positively regulated by the RcsCBA two-component signal transduction system . A lon mutation increases the half life of RcsA and thus increases cpsB expression . cpsB expression is increased by osmotic shock . The cpsB transcription level is decreased in rpoB mutants . In a metabolic engineering study, an E. coli mutant was constructed that included a deletion of manA and the cps gene cluster, and carried a plasmid harboring cpsG and cpsB from E. coli as well as another plasmid harboring msg from Rhodothermus marinus. This strain was used in the production of the osmolyte mannosylglycerate . Recombinant E. coli strains overexpressing E...

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24174|protein.P24174]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006791,ECOCYC:EG10161,GeneID:946580`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2123084-2124520:-; feature_type=gene
