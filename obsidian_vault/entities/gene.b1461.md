---
entity_id: "gene.b1461"
entity_type: "gene"
name: "pptA"
source_database: "NCBI RefSeq"
source_id: "gene-b1461"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1461"
  - "pptA"
---

# pptA

`gene.b1461`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1461`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pptA (gene.b1461) is a gene entity. It encodes pptA (protein.P31992). Encoded protein function: FUNCTION: Can use enol isomers of phenylpyruvate, 2-hydroxy-2,4-pentadienoate and (p-hydroxyphenyl)pyruvate as substrates. {ECO:0000269|PubMed:12356301}. EcoCyc product frame: EG11761-MONOMER. EcoCyc synonyms: ydcE. Genomic coordinates: 1533052-1533285. EcoCyc protein note: YdcE is a member of subfamily 5 of the 4-oxalocrotonate tautomerase (4-OT) superfamily. Although it catalyzes an efficient tautomerase reaction using 2-hydroxy-2,4-pentadienoate and related substrates, YdcE does not appear to have 4-OT-like activity with 2-hydroxymuconate or 2-oxo-3-hexenedioate . Crystal structures of YdcE alone, in complex with the inhibitor (E)-2-fluoro-p-hydroxycinnamate, and in complex with N-(2-hydroxyethyl)piperazine-N'-2-ethanesulfonic acid (HEPES) and benzoate have been solved. While many 4-OTs are hexameric, YdcE forms homodimers. The potential active sites and reaction mechanism are discussed, as are the implications of the enzyme structure with respect to the active site and the reaction mechanism . YdcE accumulates in the presence of the antifouling agent zosteric acid . Review:

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31992|protein.P31992]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004875,ECOCYC:EG11761,GeneID:945731`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1533052-1533285:+; feature_type=gene
