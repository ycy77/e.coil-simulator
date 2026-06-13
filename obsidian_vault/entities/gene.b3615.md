---
entity_id: "gene.b3615"
entity_type: "gene"
name: "waaH"
source_database: "NCBI RefSeq"
source_id: "gene-b3615"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3615"
  - "waaH"
---

# waaH

`gene.b3615`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3615`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaH (gene.b3615) is a gene entity. It encodes yibD (protein.P11290). Encoded protein function: Uncharacterized glycosyltransferase YibD (EC 2.4.-.-) EcoCyc product frame: EG11266-MONOMER. EcoCyc synonyms: yibD. Genomic coordinates: 3789047-3790081. EcoCyc protein note: WaaH is a glucuronic acid transferase involved in modification of the core oligosaccharide in E. coli K-12. WaaH catalyses the addition of glucuronic acid to the third heptose of the inner core oligosaccharide . This modified lipopolysaccharide (LPS) is produced when E. coli is grown under phosphate limiting conditions with sub millimolar concentrations of Zn2+ and Fe3+ . The glucuronic acid modification coincides with the absence of phosphate on the second heptose, is absent in the LPS of waaC, waaO, waaP, waaG or waaQ deletion mutants but can be identified in waaR and waaB deletion mutants . The LPS of a phoB deletion mutant does not contain glucuronic acid . WaaH is membrane associated . Structural analysis of the modified LPS indicates that a β-glucuronate residue is attached to the O7 atom of the side chain heptose (heptose III) . Transcription of a waaH-lacZ promoter fusion is induced by growth in phosphate limited medium and abolished in a phoB deleted strain but not in a basR deleted strain . Two PhoB binding sites are located directly upstream of the waaH gene...

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11290|protein.P11290]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011826,ECOCYC:EG11266,GeneID:948140`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3789047-3790081:-; feature_type=gene
