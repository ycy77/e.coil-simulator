---
entity_id: "gene.b0212"
entity_type: "gene"
name: "gloB"
source_database: "NCBI RefSeq"
source_id: "gene-b0212"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0212"
  - "gloB"
---

# gloB

`gene.b0212`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0212`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gloB (gene.b0212) is a gene entity. It encodes gloB (protein.P0AC84). Encoded protein function: FUNCTION: Type II glyoxalase that catalyzes the hydrolysis of (R)-S-lactoylglutathione to (R)-lactate and glutathione (PubMed:17196158, PubMed:25670698). Is more efficient than the isozyme GloC, and plays a major contribution to methylglyoxal (MG) detoxification in E.coli (PubMed:25670698). The two isoenzymes have additive effects and ensure maximal MG degradation (PubMed:25670698). {ECO:0000269|PubMed:17196158, ECO:0000269|PubMed:25670698}. EcoCyc product frame: GLYOXII-MONOMER. EcoCyc synonyms: yafR. Genomic coordinates: 234027-234782. EcoCyc protein note: Glyoxalase II catalyzes the second of two sequential reactions in the conversion of methylglyoxal to D-lactate . The enzyme contains ~1.7 molecules of Zn2+ per active monomer. Co2+ and Mn2+ can substitute for Zn2+, but Ni2+ can not . A gloB null mutant accumulates S-lactoylglutathione upon methylglyoxal exposure and has a depleted glutathione pool. This leads to activation of the KefB potassium efflux system, which causes cytoplasmic acidification and protection against methylglyoxal toxicity. Conversely, overexpression of gloB leads to depletion of S-lactoylglutathione and increased sensitivity to methylglyoxal...

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC84|protein.P0AC84]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000707,ECOCYC:G6099,GeneID:944902`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:234027-234782:-; feature_type=gene
